import sys
from pathlib import Path
from collections import namedtuple
sys.path.append(str(Path(__file__).resolve().parent.parent))
from tools.brus16_dsl import translate
from tools.brus16_asm import assemble, save
from tools.brus16_cfg import *


def asm_to_text(asm):
    lines = []
    pos = 0
    for cmd in asm:
        text = ' '.join(str(x) for x in cmd)
        match cmd:
            case ('LABEL' | 'DATA', *_):
                lines.append(text)
            case _:
                lines.append(f'{pos}: {text}')
                pos += 1
    return '\n'.join(lines)


def save_game(filename, source):
    asm = translate(source)
    _, code, data = assemble(asm)
    print(f'code: {len(code)}\ndata: {len(data)}')
    save(filename, code, data)
    return asm


def load_code(filename):
    with open(filename) as f:
        code = f'f"""{f.read()}"""'
    return eval(code, sys._getframe(1).f_globals)


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
