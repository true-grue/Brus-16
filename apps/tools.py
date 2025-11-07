import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from brus16_dsl import translate
from brus16_asm import assemble, save
from brus16_cfg import *


def save_game(filename, source):
    asm = translate(source)
    _, code, data = assemble(asm)
    print(f'code: {len(code)}\ndata: {len(data)}')
    save(filename, code, data)
    return asm


def rgb(x):
    return ((x >> 8) & 0xf800) | ((x >> 5) & 0x07e0) | ((x >> 3) & 0x001f)


def get_rect_addr(rect, offs=0):
    return RECT_MEM + rect * RECT_SIZE + offs


def asm_to_text(asm):
    lines = []
    for cmd in asm:
        lines.append(' '.join(str(x) for x in cmd))
    return '\n'.join(lines)
