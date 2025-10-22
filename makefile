CC = clang
EMCC = emcc
CFLAGS = -O2 -Wall -Wextra -Wpedantic
LDFLAGS = -lSDL3
SRC = brus16_sdl.c brus16_cpu.c

GAMES = --preload-file racing.bin \
        --preload-file flippy.bin \
        --preload-file zoom.bin \
        --preload-file logo.bin

ifeq ($(OS),Windows_NT)
	TARGET = brus16.exe
	SDL = SDL_MINGW/x86_64-w64-mingw32
	LDFLAGS += -L"$(SDL)/lib"
else
	TARGET = brus16
	SDL = SDL/include/SDL3
endif

CFLAGS += -I"$(SDL)/include"

sdl:
	$(CC) $(CFLAGS) $(SRC) -o $(TARGET) $(LDFLAGS)

web:
	$(EMCC) $(CFLAGS) $(SRC) $(GAMES) -s USE_SDL=3 -s MODULARIZE=1 -o brus16.html --shell-file template.html

.PHONY: sdl web
