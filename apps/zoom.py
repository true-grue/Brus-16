from brus16_dsl import comp
from brus16_asm import assemble, save
from brus16_cfg import *
from tools import *

game = f'''
def main():
    set_fp({KEY_MEM})
    while 1:
        draw()
        wait()

def draw():
    addr = {RECT_MEM}
    j = 0
    while j < 8:
        i = 0
        while i < 8:
            addr[{RECT_X}] = w * (i - 4) + 320
            addr[{RECT_Y}] = h * (j - 4) + 240
            addr[{RECT_W}] = w
            addr[{RECT_H}] = h
            if w & 15 == 0:
                addr[{RECT_COLOR}] = rnd()
            addr += {RECT_SIZE}
            i += 1
        j += 1
    w = (w & 255) + d
    h = (h & 255) + d
    if w & 255 == 0:
        d = -d

def rnd():
    rnd_seed ^= rnd_seed << 7
    rnd_seed ^= rnd_seed >> 9
    rnd_seed ^= rnd_seed << 8
    return rnd_seed

rnd_seed = 1
w = 0
h = 0
d = 1
'''

_, code, data = assemble(comp(game))
save('zoom.bin', code, data)
