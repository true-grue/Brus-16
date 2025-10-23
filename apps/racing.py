from brus16_dsl import comp
from brus16_asm import assemble, save
from brus16_cfg import *
from tools import *

GRASS_DATA = [1, 0, 0, SCREEN_W, SCREEN_H, to_rgb565(0x3a661c)]

ROAD0_W = 225
ROAD1_W = 180
ROAD2_W = 150

ROAD0_DATA = [1, (SCREEN_W - ROAD0_W) // 2, 0, ROAD0_W, SCREEN_H, to_rgb565(0x338000)]
ROAD1_DATA = [1, (SCREEN_W - ROAD1_W) // 2, 0, ROAD1_W, SCREEN_H, to_rgb565(0x808080)]
ROAD2_DATA = [1, (SCREEN_W - ROAD2_W) // 2, 0, ROAD2_W, SCREEN_H, to_rgb565(0x999999)]

LINE_RECT = 4
LINE_PARTS = 4
LINE_W = 4
LINE_H = 42
LINE_GAP = (SCREEN_H - LINE_PARTS * LINE_H) // (LINE_PARTS - 1)
LINE_DATA = []
for i in range(LINE_PARTS):
    LINE_DATA += [1, (SCREEN_W - LINE_W) // 2, i * (LINE_H + LINE_GAP),
                  LINE_W, LINE_H, to_rgb565(0xe6e6e6)]

CROSSING_RECT = LINE_RECT + LINE_PARTS
CROSSING_PARTS = 5
CROSSING_W = LINE_W * 2
CROSSING_H = LINE_H
CROSSING_GAP = CROSSING_W * 3
CROSSING = [
    1, 252, 218, CROSSING_W, CROSSING_H, to_rgb565(0xffcc00),
    0, CROSSING_W + CROSSING_GAP, 0, CROSSING_W, CROSSING_H, to_rgb565(0xe6e6e6),
    0, (CROSSING_W + CROSSING_GAP) * 2, 0, CROSSING_W, CROSSING_H, to_rgb565(0xffcc00),
    0, (CROSSING_W + CROSSING_GAP) * 3, 0, CROSSING_W, CROSSING_H, to_rgb565(0xe6e6e6),
    0, (CROSSING_W + CROSSING_GAP) * 4, 0, CROSSING_W, CROSSING_H, to_rgb565(0xffcc00),
]

HOUSE0_RECT = CROSSING_RECT + CROSSING_PARTS
HOUSE_H = 100
HOUSE0_DATA = [
    1, 60, 140, 80, HOUSE_H * 2, to_rgb565(0x552200),
    0, -3, -3, 80, HOUSE_H * 2, to_rgb565(0xaa4400),
    0, 35, -3, 4, HOUSE_H * 2, to_rgb565(0xd45500),
    0, 39, -3, 38, HOUSE_H * 2, to_rgb565(0x803300)
]
HOUSE_PARTS = len(HOUSE0_DATA) // 6
HOUSE1_RECT = HOUSE0_RECT + HOUSE_PARTS
HOUSE1_DATA = HOUSE0_DATA.copy()
HOUSE1_DATA[1] = 500
HOUSE_SIZES = [HOUSE_H, HOUSE_H * 2, HOUSE_H * 3, HOUSE_H * 4]

CAR_RECT = HOUSE1_RECT + HOUSE_PARTS
CAR_BBOX = [2, -8, 20, 56]
CAR_DATA = [
    1, (SCREEN_W - 24) // 2 + 40, 350, 24, 9, to_rgb565(0),
    0, 0, 32, 24, 9, to_rgb565(0),
    0, 2, -8, 20, 56, to_rgb565(0xff2a2a),
    0, 2, -8, 20, 20, to_rgb565(0xff5555),
    0, 2, 7, 20, 6, to_rgb565(0xffaaaa),
    0, 2, 32, 20, 6, to_rgb565(0xffaaaa)
]
CAR_PARTS = len(CAR_DATA) // 6

SMALL_CAR_RECT = CAR_RECT + CAR_PARTS
SMALL_CAR_X = (SCREEN_W - 24) // 2 + 40
SMALL_CAR_BBOX = [0, -8, 24, 54]
SMALL_CAR_DATA = [
    1, SMALL_CAR_X, 100, 24, 9, to_rgb565(0),
    0, 0, 32, 24, 9, to_rgb565(0),
    0, 2, -8, 20, 54, to_rgb565(0x0088aa),
    0, 2, 32, 20, 14, to_rgb565(0x006680),
    0, 2, 7, 20, 30, to_rgb565(0x00aad4),
    0, 4, 14, 16, 18, to_rgb565(0x006680)
]
SMALL_CAR_PARTS = len(SMALL_CAR_DATA) // 6
SMALL_CAR_X_POS = [SMALL_CAR_X, SMALL_CAR_X + 20, SMALL_CAR_X - 10, SMALL_CAR_X - 20]
SMALL_CAR_SPEED = [-5, -5, -7, -10, -12]

BIG_CAR_RECT = SMALL_CAR_RECT + SMALL_CAR_PARTS
BIG_CAR_X = 260
BIG_CAR_BBOX = [0, 0, 40, 172]
BIG_CAR_DATA = [
    1, BIG_CAR_X, 200, 40, 128, to_rgb565(0x006680),
    0, 10, 128, 20, 4, to_rgb565(0),
    0, 0, 155, 40, 9, to_rgb565(0),
    0, 2, 132, 36, 40, to_rgb565(0x0088aa),
    0, 2, 144, 36, 20, to_rgb565(0x006680),
    0, 2, 157, 36, 10, to_rgb565(0x00aad4),
    0, 5, 157, 30, 4, to_rgb565(0x006680),
    0, 2, 166, 36, 6, to_rgb565(0x0088aa),
]
BIG_CAR_PARTS = len(BIG_CAR_DATA) // 6
BIG_CAR_X_POS = [BIG_CAR_X, BIG_CAR_X - 15, BIG_CAR_X + 10, BIG_CAR_X + 20]
BIG_CAR_SPEED = [2, 2, 2, 3, 4]

BG_DATA = GRASS_DATA + ROAD0_DATA + ROAD1_DATA + ROAD2_DATA + \
    LINE_DATA + CROSSING + HOUSE0_DATA + HOUSE1_DATA + CAR_DATA + \
    SMALL_CAR_DATA + BIG_CAR_DATA

MAX_SPEED = 2000
ACCEL = 10
BRAKE = 20
SLIDE = 30

game = f'''
def main():
    set_fp({KEY_MEM})
    setup()
    while 1:
        draw()
        wait()

def setup():
    copy(bg_data, {RECT_MEM}, {len(BG_DATA)})

def draw():
    detect_collisions()
    control_my_car()
    slide_my_car()
    move_background()
    move_npc_cars()

def control_my_car():
    if peek({KEY_MEM + KEY_UP}):
        speed_y += {ACCEL}
    if peek({KEY_MEM + KEY_DOWN}):
        speed_y -= {BRAKE}
        speed_x = 0
    if peek({KEY_MEM + KEY_LEFT}):
        if speed_y >= 100:
            speed_x = {-SLIDE}
    if peek({KEY_MEM + KEY_RIGHT}):
        if speed_y >= 100:
            speed_x = {SLIDE}
    speed_y = min({MAX_SPEED}, max(0, speed_y - 3))

def slide_my_car():
    dx = 1 + (({MAX_SPEED} - speed_y) >> 9)
    if speed_x > 0:
        speed_x = max(0, speed_x - dx)
    elif speed_x < 0:
        speed_x = min(0, speed_x + dx)
    car_x = peek({get_rect_addr(CAR_RECT, RECT_X)})
    poke({get_rect_addr(CAR_RECT, RECT_X)}, car_x + shra(speed_x + 4, 3))

def move_npc_cars():
    move_npc_car(
        {get_rect_addr(SMALL_CAR_RECT)},
        -500,
        {SCREEN_H + 500},
        -80,
        small_car_x_pos,
        small_car_speed,
        1000)
    move_npc_car(
        {get_rect_addr(BIG_CAR_RECT)},
        -500,
        {SCREEN_H},
        -200,
        big_car_x_pos,
        big_car_speed,
        500)

def move_npc_car(car, y_min, y_max, y_start, x_pos, speed, prob):
    if (car[2] >= y_max) | (car[2] <= y_min):
        if ltu(rnd(), prob):
            car[1] = x_pos[rnd() & 3]
            car[2] = y_start
            speed[0] = speed[1 + (rnd() & 3)]
    else:
        car[2] += speed[0] + (speed_y >> 7)

def detect_collisions():
    car = {get_rect_addr(CAR_RECT)}
    car_x1 = car[1] + {CAR_BBOX[0]}
    car_y1 = car[2] + {CAR_BBOX[1]}
    car_x2 = car_x1 + {CAR_BBOX[2]}
    car_y2 = car_y1 + {CAR_BBOX[3]}
    if (car_x1 < {ROAD1_DATA[1]}) | (car_x2 > {ROAD1_DATA[1] + ROAD1_W}):
        game_over()
    small_car = {get_rect_addr(SMALL_CAR_RECT)}
    small_car_x1 = small_car[1] + {SMALL_CAR_BBOX[0]}
    small_car_y1 = small_car[2] + {SMALL_CAR_BBOX[1]}
    small_car_x2 = small_car_x1 + {SMALL_CAR_BBOX[2]}
    small_car_y2 = small_car_y1 + {SMALL_CAR_BBOX[3]}
    if hit(car_x1, car_y1, car_x2, car_y2,
           small_car_x1, small_car_y1, small_car_x2, small_car_y2):
        game_over()
    big_car = {get_rect_addr(BIG_CAR_RECT)}
    big_car_x1 = big_car[1] + {BIG_CAR_BBOX[0]}
    big_car_y1 = big_car[2] + {BIG_CAR_BBOX[1]}
    big_car_x2 = big_car_x1 + {BIG_CAR_BBOX[2]}
    big_car_y2 = big_car_y1 + {BIG_CAR_BBOX[3]}
    if hit(car_x1, car_y1, car_x2, car_y2,
           big_car_x1, big_car_y1, big_car_x2, big_car_y2):
        game_over()

def game_over():
    car = {get_rect_addr(CAR_RECT)}
    x = car[{RECT_Y}]
    j = 0
    while j < 5:
        i = 0
        car[{RECT_Y}] = x
        while i < 15:
            wait()
            i += 1
        i = 0
        car[{RECT_Y}] = -1000
        while i < 30:
            wait()
            i += 1
        j += 1
    while 1:
        wait()

def move_background():
    bg_speed = speed_y >> 7
    move_lines(bg_speed)
    move_crossing(bg_speed)
    move_house({get_rect_addr(HOUSE0_RECT)}, bg_speed)
    move_house({get_rect_addr(HOUSE1_RECT)}, bg_speed)

def move_crossing(speed):
    crossing = {get_rect_addr(CROSSING_RECT)}
    line = {get_rect_addr(LINE_RECT)}
    if (crossing[{RECT_Y}] >= {SCREEN_H}) & ltu(rnd(), 1000):
        if line[{RECT_Y}] < 0:
            crossing[{RECT_Y}] = line[{RECT_Y}] - {CROSSING_H + 31}
    crossing[2] += speed

def set_house_size(house, size):
    i = 0
    while i < {HOUSE_PARTS}:
        house[{RECT_H}] = size
        house += {RECT_SIZE}
        i += 1

def move_house(house, speed):
    house[{RECT_Y}] += speed
    if house[{RECT_Y}] >= {SCREEN_H}:
        if ltu(rnd(), 1000):
            set_house_size(house, house_sizes[rnd() & 3])
            house[{RECT_Y}] = -house[{RECT_H}] - 10

def move_lines(speed):
    i = 0
    while i < {LINE_PARTS}:
        move_line(i * {RECT_SIZE} + 2)
        i += 1
    line_y += speed

def move_line(rect_y):
    if line_y >= {SCREEN_H}:
        line_y -= {SCREEN_H + LINE_GAP}
    poke({get_rect_addr(LINE_RECT)} + rect_y, line_y)
    line_y += {LINE_H + LINE_GAP}

def hit(x1, y1, x2, y2, other_x1, other_y1, other_x2, other_y2):
    if x2 < other_x1:
        return 0
    if x1 > other_x2:
        return 0
    if y2 < other_y1:
        return 0
    if y1 > other_y2:
        return 0
    return 1

def max(a, b):
    if a > b:
        return a
    return b

def min(a, b):
    if a < b:
        return a
    return b

def copy(src, dst, size):
    end = src + size
    while src != end:
        dst[0] = src[0]
        src += 1
        dst += 1

def rnd():
    rnd_seed ^= rnd_seed << 7
    rnd_seed ^= rnd_seed >> 9
    rnd_seed ^= rnd_seed << 8
    return rnd_seed

bg_data = {BG_DATA}
house_sizes = {HOUSE_SIZES}
rnd_seed = 1
line_y = 0
speed_x = 0
speed_y = 0
small_car_x_pos = {SMALL_CAR_X_POS}
small_car_speed = {SMALL_CAR_SPEED}
big_car_x_pos = {BIG_CAR_X_POS}
big_car_speed = {BIG_CAR_SPEED}
'''

_, code, data = assemble(comp(game))
save('racing.bin', code, data)
