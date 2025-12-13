import os
import sys
import math
from collections import namedtuple
from .brus16_dsl import translate
from .brus16_asm import assemble, save
from .brus16_cfg import *


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
    frame = sys._getframe(1)
    path = os.path.dirname(os.path.abspath(frame.f_code.co_filename))
    with open(os.path.join(path, filename), encoding='utf-8') as f:
        code = f'fr"""{f.read()}"""'
    return eval(code, frame.f_globals)


def rgb(x, g=None, b=None):
    if g is not None:
        x = (x << 16) | (g << 8) | b
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


def get_vol(val):
    return min(round(val * 32768), 65535)


def get_decay(sec):
    steps = (sec * SR) / DECAY_SCALE
    k = math.exp(math.log(0.01) / steps)
    return round(k * 32768)


def get_freq(freq):
    step = round((TABLE_SIZE * freq * (1 / SR)) * (1 << TABLE_BITS))
    return min(step, 65535)


def get_ratio(x):
    return min(round(x * (1 << RATIO_BITS)), 65535)
