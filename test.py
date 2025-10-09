import ast
from brus16_dsl import comp
from brus16_asm import assemble, save
from brus16_cfg import *
from tools import *


game = f'''
def setup():
    set_fp({KEY_MEM})
    while 1:
        update()
        wait()


def update():
    addr = {RECT_MEM}
    j = 0
    while j < 8:
        i = 0
        while i < 8:
            addr[{RECT_X}] = i * 80
            addr[{RECT_Y}] = j * 60
            addr[{RECT_W}] = 80
            addr[{RECT_H}] = 60
            addr[{RECT_COLOR}] = rnd()           
            addr += {RECT_SIZE}
            i += 1
        j += 1
    delay(10)


def delay(n):
    i = 0
    while i < n:
        wait()
        i += 1


def rnd():
    rnd_seed ^= rnd_seed << 7
    rnd_seed ^= rnd_seed >> 9
    rnd_seed ^= rnd_seed << 8
    return rnd_seed


rnd_seed = 1
'''

asm = comp(game)
_, code, data = assemble(asm)
save('test.bin', code, data)
