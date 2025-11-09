import sys
from collections import namedtuple
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from brus16_dsl import translate
from brus16_asm import assemble, save
from brus16_cfg import *


def asm_to_text(asm):
    lines = []
    for cmd in asm:
        lines.append(' '.join(str(x) for x in cmd))
    return '\n'.join(lines)


def save_game(filename, source):
    asm = translate(source)
    _, code, data = assemble(asm)
    print(f'code: {len(code)}\ndata: {len(data)}')
    save(filename, code, data)
    return asm


def rgb(x):
    return ((x >> 8) & 0xf800) | ((x >> 5) & 0x07e0) | ((x >> 3) & 0x001f)


Rect = namedtuple('Rect', 'addr abs x y w h color')


def make_rects():
    rects = []
    addr = RECT_MEM
    for _ in range(RECT_NUM):
        rects.append(Rect(addr, *range(addr, addr + RECT_SIZE)))
        addr += RECT_SIZE
    return rects


rect = make_rects()
