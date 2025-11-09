from tools import *

TITLE_LETTERS = [1, 5, 9, 11, 15, 16, 19]
TITLE = [
    1, 0, 0, SCREEN_W, SCREEN_H, rgb(0xffffff),
    # B
    1, 190, -280, 30, 50, rgb(0x1c58a0),
    0, 10, 10, 10, 10, rgb(0xffffff),
    0, 25, 20, 20, 10, rgb(0xffffff),
    0, 10, 30, 10, 10, rgb(0xffffff),
    # R
    1, 230, -280, 30, 50, rgb(0xe42024),
    0, 10, 10, 10, 10, rgb(0xffffff),
    0, 20, 30, 10, 10, rgb(0xffffff),
    0, 10, 40, 10, 10, rgb(0xffffff),
    # U
    1, 270, -280, 30, 50, rgb(0x78bc38),
    0, 10, 0, 10, 40, rgb(0xffffff),
    # S
    1, 320, -280, 20, 40, rgb(0xf8c018),
    0, -10, 10, 20, 40, rgb(0xf8c018),
    0, 0, 10, 20, 10, rgb(0xffffff),
    0, -10, 30, 20, 10, rgb(0xffffff),
    # -
    1, 350, -300, 20, 10, rgb(0x903890),
    # 1
    1, 380, -280, 30, 50, rgb(0x903890),
    0, 0, 10, 10, 30, rgb(0xffffff),
    0, 20, 0, 10, 40, rgb(0xffffff),
    # 6
    1, 420, -280, 30, 50, rgb(0x24b4b8),
    0, 10, 10, 20, 10, rgb(0xffffff),
    0, 10, 30, 10, 10, rgb(0xffffff)
]
LOGO_RECT = len(TITLE) // RECT_SIZE
LOGO = [
    1, 190, -160, 250, 90, rgb(0xc86828),
    0, 10, -10, 250, 10, rgb(0xf8b060),
    0, 130, 10, 120, 10, rgb(0xa4501c),
    0, 0, 20, 110, 10, rgb(0xa4501c),
    0, 80, 50, 170, 10, rgb(0xa4501c),
    0, 0, 60, 80, 10, rgb(0xa4501c),
    0, 140, 70, 110, 10, rgb(0xa4501c),
    0, 250, 0, 10, 80, rgb(0x984c1c),
    0, 250, 10, 10, 70, rgb(0x743818)
]
LOGO_DATA = TITLE + LOGO

SHIFT = 4
DAMPING = 12
START_LEVEL = -160
END_LEVEL = 160

save_game('logo.bin', f'''
def main():
    setup()
    while 1:
        draw()
        wait()

def setup():
    copy(logo_data, {RECT_MEM}, {len(LOGO_DATA)})

def draw():
    poke({rect[LOGO_RECT].y}, anim())
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
''')
