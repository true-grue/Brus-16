// Author: Peter Sovietov
#define SDL_MAIN_USE_CALLBACKS 1
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>
#include "brus16_cpu.h"
#include "brus16_sfx.h"

#ifndef ZOOM
#define ZOOM 2
#endif
#define FPS 60
#define CYCLES_PER_FRAME 400000
#define SAMPLES_PER_FRAME (44100 / FPS)

struct EMU {
    struct CPU cpu;
    struct SFX sfx;
    SDL_Window *window;
    SDL_Renderer *renderer;
    SDL_AudioStream *stream;
    SDL_FRect rects[RECT_NUM];
    uint8_t rect_colors[RECT_NUM * 3];
    uint64_t last_ticks;
    uint64_t ticks_acc;
};

const SDL_Scancode scancodes[KEY_NUM][2] = {
    {SDL_SCANCODE_UP, SDL_SCANCODE_W}, 
    {SDL_SCANCODE_DOWN, SDL_SCANCODE_S},
    {SDL_SCANCODE_LEFT, SDL_SCANCODE_A},
    {SDL_SCANCODE_RIGHT, SDL_SCANCODE_D},
    {SDL_SCANCODE_Z, SDL_SCANCODE_1},
    {SDL_SCANCODE_X, SDL_SCANCODE_2},
    {SDL_SCANCODE_C, SDL_SCANCODE_3},
    {SDL_SCANCODE_V, SDL_SCANCODE_4},
    {SDL_SCANCODE_UP, SDL_SCANCODE_I},
    {SDL_SCANCODE_DOWN, SDL_SCANCODE_K},
    {SDL_SCANCODE_LEFT, SDL_SCANCODE_J},
    {SDL_SCANCODE_RIGHT, SDL_SCANCODE_L},
    {SDL_SCANCODE_Z, SDL_SCANCODE_7},
    {SDL_SCANCODE_X, SDL_SCANCODE_8},
    {SDL_SCANCODE_C, SDL_SCANCODE_9},
    {SDL_SCANCODE_V, SDL_SCANCODE_0}
};

void from_rgb565(uint16_t color, uint8_t *r, uint8_t *g, uint8_t *b) {
    uint8_t r5 = (color >> 11) & 0x1f;
    uint8_t g6 = (color >> 5) & 0x3f;
    uint8_t b5 = color & 0x1f;
    *r = (r5 << 3) | (r5 >> 2);
    *g = (g6 << 2) | (g6 >> 4);
    *b = (b5 << 3) | (b5 >> 2);
}

void load_game(struct EMU *emu, char *filename) {
    FILE* fp = fopen(filename, "rb");
    assert(fp);
    uint16_t code_size, data_size;
    assert(fread(&code_size, sizeof(uint16_t), 1, fp) == 1);
    assert(fread(&data_size, sizeof(uint16_t), 1, fp) == 1);
    assert(fread(emu->cpu.code, sizeof(uint16_t), code_size, fp) == code_size);
    assert(fread(emu->cpu.data, sizeof(uint16_t), data_size, fp) == data_size);
    fclose(fp);
}

void save_frame(struct EMU *emu, char *filename) {
    FILE* fp = fopen(filename, "wb");
    assert(fp);
    fprintf(fp, "<svg xmlns=\"http://www.w3.org/2000/svg\">\n");
    fprintf(fp, "<rect x=\"0\" y=\"0\" width=\"%d\" height=\"%d\" fill=\"#000000\" />\n",
            SCREEN_W * ZOOM, SCREEN_H * ZOOM);
    char hex_rgb[8];
    for (int i = 0; i < RECT_NUM; i++) {
        uint8_t *rgb = &emu->rect_colors[i * 3];
        sprintf(hex_rgb, "#%02x%02x%02x", rgb[0], rgb[1], rgb[2]);
        fprintf(fp, "<rect x=\"%1.f\" y=\"%1.f\" width=\"%1.f\" height=\"%1.f\" fill=\"%s\" />\n",
                emu->rects[i].x, emu->rects[i].y, emu->rects[i].w, emu->rects[i].h, hex_rgb);
    }
    fprintf(fp, "</svg>");
    fclose(fp);
}

void debug_put(int c) {
    putchar(c);
}

SDL_AppResult SDL_AppInit(void **appstate, int argc, char **argv) {
    assert(argc == 2);
    *appstate = malloc(sizeof(struct EMU));
    assert(*appstate);
    struct EMU *emu = *appstate;
    setvbuf(stdout, NULL, _IONBF, 0);
    assert(SDL_Init(SDL_INIT_VIDEO | SDL_INIT_AUDIO));
    assert(SDL_CreateWindowAndRenderer("Brus-16", SCREEN_W * ZOOM, SCREEN_H * ZOOM, 0, &emu->window, &emu->renderer));
    SDL_SetRenderVSync(emu->renderer, 1);
    SDL_AudioSpec spec = {SDL_AUDIO_S16, 1, SAMPLES_PER_FRAME * FPS};
    emu->stream = SDL_OpenAudioDeviceStream(SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK, &spec, NULL, NULL);
    assert(emu->stream);
    emu->last_ticks = SDL_GetTicksNS();
    emu->ticks_acc = SDL_NS_PER_SECOND;
    SDL_ResumeAudioStreamDevice(emu->stream);
    load_game(emu, argv[1]);
    emu->cpu.fp = SYSTEM_MEM;
    return SDL_APP_CONTINUE;
}

SDL_AppResult SDL_AppEvent(void *emu, SDL_Event *event) {
    if (event->type == SDL_EVENT_QUIT) {
        return SDL_APP_SUCCESS;
    }
    if (event->type == SDL_EVENT_KEY_DOWN && event->key.scancode == SDL_SCANCODE_PAUSE) {
        save_frame(emu, "frame.svg");
    }
    return SDL_APP_CONTINUE;
}

void update_rects(struct EMU *emu) {
    int cursor_x = 0;
    int cursor_y = 0;
    int rect_addr = RECT_MEM;
    for (int i = 0; i < RECT_NUM; i++) {
        int is_abs = emu->cpu.data[rect_addr + RECT_ABS];
        int16_t x = sext(emu->cpu.data[rect_addr + RECT_X], 16);
        int16_t y = sext(emu->cpu.data[rect_addr + RECT_Y], 16);
        uint16_t w = emu->cpu.data[rect_addr + RECT_W];
        uint16_t h = emu->cpu.data[rect_addr + RECT_H];
        if (is_abs) {
            cursor_x = x;
            cursor_y = y;
        } else {
            x += cursor_x;
            y += cursor_y;
        }
        emu->rects[i] = (SDL_FRect) {x * ZOOM, y * ZOOM, w * ZOOM, h * ZOOM};
        uint16_t color = emu->cpu.data[rect_addr + RECT_COLOR];
        uint8_t *rgb = &emu->rect_colors[i * 3];
        from_rgb565(color, &rgb[0], &rgb[1], &rgb[2]);
        rect_addr += RECT_SIZE;
    }
}

SDL_AppResult SDL_AppIterate(void *appstate) {
    struct EMU *emu = appstate;
    int16_t samples[SAMPLES_PER_FRAME];
    const bool *keys = SDL_GetKeyboardState(NULL);
    for (int i = 0; i < KEY_NUM; i++) {
        emu->cpu.data[KEY_MEM + i] = keys[scancodes[i][0]] | keys[scancodes[i][1]];
    }
    uint64_t ticks = SDL_GetTicksNS();
    uint64_t delta = ticks - emu->last_ticks;
    emu->last_ticks = ticks;
    emu->ticks_acc += delta * FPS;
    while (emu->ticks_acc >= SDL_NS_PER_SECOND) {
        emu->ticks_acc -= SDL_NS_PER_SECOND;
        for(int cycles = 0; !emu->cpu.wait; cycles++) {
            assert(cycles < CYCLES_PER_FRAME);
            step(&emu->cpu);
        }
        emu->cpu.wait = 0;
        sfx_update(&emu->cpu.data[VOICES_MEM], &emu->sfx);
        for (int i = 0; i < SAMPLES_PER_FRAME; i++) {
            samples[i] = sfx_process(&emu->sfx);
        }
        SDL_PutAudioStreamData(emu->stream, samples, sizeof(samples));
    }
    update_rects(emu);
    SDL_SetRenderDrawColor(emu->renderer, 0, 0, 0, 255);
    SDL_RenderClear(emu->renderer);
    for (int i = 0; i < RECT_NUM; i++) {
        uint8_t *rgb = &emu->rect_colors[i * 3];
        SDL_SetRenderDrawColor(emu->renderer, rgb[0], rgb[1], rgb[2], 255);
        SDL_RenderFillRect(emu->renderer, &emu->rects[i]);
    }
    SDL_RenderPresent(emu->renderer);
    return SDL_APP_CONTINUE;
}

void SDL_AppQuit(void *appstate, SDL_AppResult result) {
    free(appstate);
    (void) result;
}

#ifdef EMSCRIPTEN
#include <emscripten.h>
void EMSCRIPTEN_KEEPALIVE quit(void) {
    SDL_Event event;
    SDL_zero(event);
    event.type = SDL_EVENT_QUIT;
    SDL_PushEvent(&event);
}
#endif
