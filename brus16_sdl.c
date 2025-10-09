#define SDL_MAIN_USE_CALLBACKS 1
#include <stdio.h>
#include <assert.h>
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>
#include "brus16_cpu.h"

#define ZOOM 1
#define FPS 60
#define FRAME_DELAY (SDL_NS_PER_SECOND / FPS)

#define SCREEN_W 640
#define SCREEN_H 480
#define KEY_NUM 12
#define RECT_NUM 64
#define RECT_SIZE 6
#define KEY_MEM (DATA_SIZE - (KEY_NUM + RECT_NUM * RECT_SIZE))
#define RECT_MEM (KEY_MEM + KEY_NUM)
#define KEY_UP 0
#define KEY_DOWN 1
#define KEY_LEFT 2
#define KEY_RIGHT 3
#define KEY_A 4
#define KEY_B 5
#define KEY_UP2 6
#define KEY_DOWN2 7
#define KEY_LEFT2 8
#define KEY_RIGHT2 9
#define KEY_A2 10
#define KEY_B2 11
#define RECT_ABS 0
#define RECT_X 1
#define RECT_Y 2
#define RECT_W 3
#define RECT_H 4
#define RECT_COLOR 5

SDL_Scancode scancodes[] = {
    SDL_SCANCODE_UP,
    SDL_SCANCODE_DOWN,
    SDL_SCANCODE_LEFT,
    SDL_SCANCODE_RIGHT,
    SDL_SCANCODE_RCTRL,
    SDL_SCANCODE_RSHIFT,
    SDL_SCANCODE_W,
    SDL_SCANCODE_S,
    SDL_SCANCODE_A,
    SDL_SCANCODE_D,
    SDL_SCANCODE_G,
    SDL_SCANCODE_H

};

void from_rgb565(uint16_t color, uint8_t *r, uint8_t *g, uint8_t *b) {
    uint8_t r5 = (color >> 11) & 0x1f;
    uint8_t g6 = (color >> 5) & 0x3f;
    uint8_t b5 = color & 0x1f;
    *r = (r5 << 3) | (r5 >> 2);
    *g = (g6 << 2) | (g6 >> 4);
    *b = (b5 << 3) | (b5 >> 2);
}

void load(char *filename, struct CPU *cpu) {
    FILE* fp = fopen(filename, "rb");
    assert(fp);
    uint16_t code_size, data_size;
    assert(fread(&code_size, sizeof(uint16_t), 1, fp) == 1);
    assert(fread(&data_size, sizeof(uint16_t), 1, fp) == 1);
    assert(fread(cpu->code, sizeof(uint16_t), code_size, fp) == code_size);
    assert(fread(cpu->data, sizeof(uint16_t), data_size, fp) == data_size);
    fclose(fp);
}

SDL_Window *window;
SDL_Renderer *renderer;
struct CPU cpu;

SDL_AppResult SDL_AppInit(void **appstate, int argc, char **argv) {
    (void) appstate;
    assert(SDL_Init(SDL_INIT_VIDEO));
    assert(SDL_CreateWindowAndRenderer("Brus-16", SCREEN_W * ZOOM, SCREEN_H * ZOOM, 0, &window, &renderer));
    SDL_SetRenderVSync(renderer, 1);
#ifdef __EMSCRIPTEN__
    (void) argc;
    (void) argv;
    load("game.bin", &cpu);
#else
    assert(argc == 2);
    load(argv[1], &cpu);
#endif
    return SDL_APP_CONTINUE;
}

SDL_AppResult SDL_AppEvent(void *appstate, SDL_Event *event) {
    (void) appstate;
    return event->type == SDL_EVENT_QUIT ? SDL_APP_SUCCESS : SDL_APP_CONTINUE;
}

SDL_AppResult SDL_AppIterate(void *appstate) {
    (void) appstate;
    uint64_t frame_start = SDL_GetTicksNS();
    const bool *keystate = SDL_GetKeyboardState(NULL);
    for (int i = 0; i < KEY_NUM; i++) {
        cpu.data[KEY_MEM + i] = keystate[scancodes[i]];
    }
    while (!cpu.wait) {
        step(&cpu);
    }
    cpu.wait = 0;
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderClear(renderer);
    int cursor_x = 0;
    int cursor_y = 0;
    int rect_addr = RECT_MEM;
    for (int i = 0; i < RECT_NUM; i++) {
        int is_abs = cpu.data[rect_addr + RECT_ABS];
        int16_t x = sext(cpu.data[rect_addr + RECT_X], 16);
        int16_t y = sext(cpu.data[rect_addr + RECT_Y], 16);
        uint16_t w = cpu.data[rect_addr + RECT_W];
        uint16_t h = cpu.data[rect_addr + RECT_H];
        uint16_t color = cpu.data[rect_addr + RECT_COLOR];
        if (is_abs) {
            cursor_x = x;
            cursor_y = y;
        } else {
            x += cursor_x;
            y += cursor_y;
        }
        uint8_t r, g, b;
        from_rgb565(color, &r, &g, &b);
        SDL_FRect rect = {x * ZOOM, y * ZOOM, w * ZOOM, h * ZOOM};
        SDL_SetRenderDrawColor(renderer, r, g, b, 255);
        SDL_RenderFillRect(renderer, &rect);
        rect_addr += RECT_SIZE;
    }
    SDL_RenderPresent(renderer);
    uint64_t frame_time = SDL_GetTicksNS() - frame_start;
    if (FRAME_DELAY > frame_time) {
        SDL_DelayPrecise(FRAME_DELAY - frame_time);
    }
    return SDL_APP_CONTINUE;
}

void SDL_AppQuit(void *appstate, SDL_AppResult result) {
    (void) appstate;
    (void) result;
}
