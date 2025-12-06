CC = gcc
EMCC = emcc
CFLAGS = -O2 -Wall -Wextra -Wpedantic
LDFLAGS = -lSDL3
SRC = src/brus16_cpu.c src/brus16_emu.c

ifeq ($(OS),Windows_NT)
	TARGET = brus16.exe
	SDL = SDL/x86_64-w64-mingw32
	LDFLAGS += -L"$(SDL)/lib"
else
	TARGET = brus16
	SDL = SDL/include/SDL3
endif

CFLAGS += -I"$(SDL)/include"

emu:
	$(CC) $(CFLAGS) -DDEBUG $(SRC) -o $(TARGET) $(LDFLAGS)

gen:
	python tools/gen_cfg.py src
	python tools/gen_isa.py .
	pandoc isa.md --template docs/template.html --metadata title="Brus-16 ISA" -o docs/isa.html

GAMES = --preload-file logo.bin \
		--preload-file racing.bin \
		--preload-file flippy.bin \
		--preload-file pong.bin \
		--preload-file ping.bin \
		--preload-file tower.bin \
		--preload-file alterego.bin \
		--preload-file gerion.bin \
		--preload-file robot.bin \
		--preload-file zoom.bin

web:
	$(EMCC) $(CFLAGS) -DZOOM=1 $(SRC) $(GAMES) -s USE_SDL=3 -s MODULARIZE=1 -o brus16.html --shell-file src/template.html

.PHONY: sdl web
