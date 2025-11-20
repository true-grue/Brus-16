# Author: Vladimir Miklashevich
from brus16 import *

TITLE_LETTERS = [1, 4, 7, 10, 12, 13, 16, 19]
TITLE_COLORS = [rgb(0x000000), rgb(0xf86030), rgb(0xf8b060), rgb(0xf8b060), rgb(0xf8b060),
                rgb(0xf8b060), rgb(0xf86030), rgb(0xf8b060)]
TITLE = [
    1, 0, 0, SCREEN_W, SCREEN_H, rgb(0xffffff),
    1, 165, 270, 40, 80, rgb(0x000000),
    0, 10, 10, 30, 25, rgb(0xffffff),
    0, 10, 45, 20, 25, rgb(0xffffff),
    1, 210, 270, 10, 80, rgb(0x000000),
    0, 10, 0, 30, 45, rgb(0x000000),
    0, 10, 10, 20, 25, rgb(0xffffff),
    1, 255, 270, 40, 80, rgb(0x000000),
    0, 10, 0, 20, 35, rgb(0xffffff),
    0, 0, 45, 30, 25, rgb(0xffffff),
    1, 300, 270, 40, 80, rgb(0x000000),
    0, 10, 10, 30, 60, rgb(0xffffff),
    1, 350, 305, 30, 10, rgb(0x000000),
    1, 390, 270, 15, 10, rgb(0x000000),
    0, 15, 0, 10, 70, rgb(0x000000),
    0, 0, 70, 40, 10, rgb(0x000000),
    1, 435, 270, 40, 80, rgb(0x000000),
    0, 10, 10, 30, 25, rgb(0xffffff),
    0, 10, 45, 20, 25, rgb(0xffffff)
]
TITLE_BG = [i for i in range(len(TITLE) // RECT_SIZE)
            if TITLE[i * RECT_SIZE + RECT_COLOR] == rgb(0xffffff)]
c = 1
for i in range(RECT_SIZE, len(TITLE), RECT_SIZE):
    if i // RECT_SIZE >= TITLE_LETTERS[c]:
        c += 1
    if TITLE[i + RECT_ABS] != 0:
        TITLE[i + RECT_Y] *= -1
    if TITLE[i + RECT_COLOR] == TITLE_COLORS[0]:
        TITLE[i + RECT_COLOR] = TITLE_COLORS[c]
TITLE_LETTERS.pop()
LOGO_RECT = len(TITLE) // RECT_SIZE
LOGO = [
    1, 165, -160, 280, 90, rgb(0xc86828),
    0, 130, 10, 150, 10, rgb(0xa4501c),
    0, 0, 20, 110, 10, rgb(0xa4501c),
    0, 60, 50, 220, 10, rgb(0xa4501c),
    0, 0, 60, 80, 10, rgb(0xa4501c),
    0, 170, 70, 110, 10, rgb(0xa4501c),
    0, 280, -10, 20, 80, rgb(0x984c1c),
    0, 280, 10, 10, 70, rgb(0x743818),
    0, 280, 10, 10, 70, rgb(0x743818),
    0, 300, -20, 10, 80, rgb(0x743818),
    0, 20, -20, 270, 20, rgb(0xf8b060),
    0, 30, -30, 280, 10, rgb(0xf8b060),
    0, 10, -10, 130, 10, rgb(0xcc7838),
    0, 210, -20, 90, 10, rgb(0xcc7838),
    0, 30, -30, 190, 10, rgb(0xcc7838)
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
    if counter >= 300:
        position = {START_LEVEL}
        velocity = 0
        counter = -1
        day_time = (day_time + 1) & 3
        if day_time == 0:
            cycle({rgb(0xffffff)})
        elif day_time >= 2:
            cycle({rgb(0x202020)})
    poke({rect[LOGO_RECT].y}, anim())

def anim():
    velocity += 1
    position += velocity
    if (counter >= 0) & (counter < {len(TITLE_LETTERS)}):
        addr = {RECT_MEM} + letters[counter] * {RECT_SIZE} + {RECT_Y}
        addr[0] = -addr[0]
    if position >= {END_LEVEL}:
        position = {END_LEVEL}
        velocity = shra(-velocity * {DAMPING}, {SHIFT})
        counter += 1
    return position

def cycle(color):
    i = 0
    while i < {len(TITLE_BG)}:
        poke({RECT_MEM} + background[i] * {RECT_SIZE} + {RECT_COLOR}, color)
        i += 1

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
background = {TITLE_BG}
counter = -1
day_time = 0
''')
