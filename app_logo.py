from brus16_dsl import comp
from brus16_asm import assemble, save
from brus16_cfg import *
from tools import *

TITLE = [
    1, 0, 0, SCREEN_W, SCREEN_H, to_rgb565(0xffffff),
    # B
    0, 190, 280, 30, 50, to_rgb565(0x1c58a0),
    0, 200, 290, 10, 10, to_rgb565(0xffffff),
    0, 210, 300, 10, 10, to_rgb565(0xffffff),
    0, 200, 310, 10, 10, to_rgb565(0xffffff),
    # R
    0, 230, 280, 30, 50, to_rgb565(0xe42024),
    0, 240, 290, 10, 10, to_rgb565(0xffffff),
    0, 250, 310, 10, 10, to_rgb565(0xffffff),
    0, 240, 320, 10, 10, to_rgb565(0xffffff),
    # U
    0, 270, 280, 30, 50, to_rgb565(0x78bc38),
    0, 280, 280, 10, 40, to_rgb565(0xffffff),
    # S
    0, 320, 280, 20, 40, to_rgb565(0xf8c018),
    0, 310, 290, 20, 40, to_rgb565(0xf8c018),
    0, 320, 290, 20, 10, to_rgb565(0xffffff),
    0, 310, 310, 20, 10, to_rgb565(0xffffff),
    # -
    0, 350, 300, 20, 10, to_rgb565(0x903890),
    # 1
    0, 380, 280, 30, 50, to_rgb565(0x903890),
    0, 380, 290, 10, 30, to_rgb565(0xffffff),
    0, 400, 280, 10, 40, to_rgb565(0xffffff),
    # 6
    0, 420, 280, 30, 50, to_rgb565(0x24b4b8),
    0, 430, 290, 20, 10, to_rgb565(0xffffff),
    0, 430, 310, 10, 10, to_rgb565(0xffffff)
]

SHIFT = 4
DAMPING = 10
START_LEVEL = -160
END_LEVEL = 160

LOGO_ADDR = len(TITLE) // RECT_SIZE
LOGO = [
    1, 190, START_LEVEL, 250, 90, to_rgb565(0xc86828),
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
    t += 1
    if t > 255:
        position = {START_LEVEL}
        velocity = 0
        t = 0
    poke({get_rect_addr(LOGO_ADDR, RECT_Y)}, anim())

def anim():
    velocity += 1
    position += velocity
    if position >= {END_LEVEL}:
        position = {END_LEVEL}
        velocity = shra(-velocity * {DAMPING}, {SHIFT})
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
t = 0
'''

_, code, data = assemble(comp(game))
save('logo.bin', code, data)
