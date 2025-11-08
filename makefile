CC = clang
EMCC = emcc
CFLAGS = -O2 -Wall -Wextra -Wpedantic
LDFLAGS = -lSDL3
SRC = brus16_emu.c brus16_cpu.c

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

APPS = --preload-file apps/racing.bin \
       --preload-file apps/flippy.bin \
       --preload-file apps/zoom.bin \
       --preload-file apps/logo.bin

web:
	$(EMCC) $(CFLAGS) $(SRC) $(APPS) -s USE_SDL=3 -s MODULARIZE=1 -o brus16.html --shell-file template.html

.PHONY: sdl web
