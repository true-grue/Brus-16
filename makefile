CC = gcc
EMCC = emcc
CFLAGS = -O2 -Wall -Wextra -Wpedantic
LDFLAGS = -lSDL3
SRC = src/brus16_emu.c src/brus16_cpu.c src/brus16_sfx.c

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
	pandoc isa.md --standalone --toc --metadata title="Brus-16 ISA" -o docs/isa.html

games:
	python games/logo.py
	python games/racing.py
	python games/flippy.py
	python games/pong.py
	python games/ping.py
	python games/tower.py
	python games/gerion/gerion_make.py
	python games/robot.py
	python games/zoom.py

GAMES_BIN := $(patsubst %,--preload-file %,$(wildcard *.bin))

web:
	$(EMCC) $(CFLAGS) -DZOOM=1 $(SRC) $(GAMES_BIN) -s USE_SDL=3 -s MODULARIZE=1 -o brus16.html --shell-file src/brus16_emu.html

.PHONY: emu gen games web
