from brus16_asm import *
from brus16_cfg import *
from brus16_dsl import *
from tools import *

TITLE_LETTERS = [1, 5, 9, 11, 15, 16, 19]
TITLE = [
    1, 0, 0, SCREEN_W, SCREEN_H, to_rgb565(0xffffff),
    # B
    1, 190, -280, 30, 50, to_rgb565(0x1c58a0),
    0, 10, 10, 10, 10, to_rgb565(0xffffff),
    0, 20, 20, 10, 10, to_rgb565(0xffffff),
    0, 10, 30, 10, 10, to_rgb565(0xffffff),
    # R
    1, 230, -280, 30, 50, to_rgb565(0xe42024),
    0, 10, 10, 10, 10, to_rgb565(0xffffff),
    0, 20, 30, 10, 10, to_rgb565(0xffffff),
    0, 10, 40, 10, 10, to_rgb565(0xffffff),
    # U
    1, 270, -280, 30, 50, to_rgb565(0x78bc38),
    0, 10, 0, 10, 40, to_rgb565(0xffffff),
    # S
    1, 320, -280, 20, 40, to_rgb565(0xf8c018),
    0, -10, 10, 20, 40, to_rgb565(0xf8c018),
    0, 0, 10, 20, 10, to_rgb565(0xffffff),
    0, -10, 30, 20, 10, to_rgb565(0xffffff),
    # -
    1, 350, -300, 20, 10, to_rgb565(0x903890),
    # 1
    1, 380, -280, 30, 50, to_rgb565(0x903890),
    0, 0, 10, 10, 30, to_rgb565(0xffffff),
    0, 20, 0, 10, 40, to_rgb565(0xffffff),
    # 6
    1, 420, -280, 30, 50, to_rgb565(0x24b4b8),
    0, 10, 10, 20, 10, to_rgb565(0xffffff),
    0, 10, 30, 10, 10, to_rgb565(0xffffff)
]
LOGO_ADDR = len(TITLE) // RECT_SIZE
LOGO = [
    1, 190, -160, 250, 90, to_rgb565(0xc86828),
    0, 10, -10, 250, 10, to_rgb565(0xf8b060),
    0, 130, 10, 120, 10, to_rgb565(0xa4501c),
    0, 0, 20, 110, 10, to_rgb565(0xa4501c),
    0, 80, 50, 170, 10, to_rgb565(0xa4501c),
    0, 0, 60, 80, 10, to_rgb565(0xa4501c),
    0, 140, 70, 110, 10, to_rgb565(0xa4501c),
    0, 250, 0, 10, 80, to_rgb565(0x984c1c),
    0, 250, 10, 10, 70, to_rgb565(0x743818)
]
LOGO_DATA = TITLE + LOGO

SHIFT = 4
DAMPING = 12
START_LEVEL = -160
END_LEVEL = 160

game = f'''
def main():
    set_fp({KEY_MEM})
    setup()
    while 1:
        draw()
        wait()

def setup():
    copy(logo_data, {RECT_MEM}, {len(LOGO_DATA)})

def draw():
    poke({get_rect_addr(LOGO_ADDR, RECT_Y)}, anim())
    if counter >= 300:
        position = {START_LEVEL}
        velocity = 0
        counter = 0

def anim():
    velocity += 1
    position += velocity
    if counter < {len(TITLE_LETTERS)}:
        addr = {RECT_MEM} + letters[counter] * {RECT_SIZE} + {RECT_Y}
        addr[0] = -addr[0]
    if position >= {END_LEVEL}:
        position = {END_LEVEL}
        velocity = shra(-velocity * {DAMPING}, {SHIFT})
        counter += 1
    return position

def copy(src, dst, size):
    end = src + size
    while src < end:
        dst[0] = src[0]
        src += 1
        dst += 1

logo_data = {LOGO_DATA}
position = {START_LEVEL}
velocity = 0
letters = {TITLE_LETTERS}
counter = 0
'''

_, code, data = assemble(comp(game))
save('logo.bin', code, data)
