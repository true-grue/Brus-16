# Author: Artyom Gorchakov & Vladimir Miklashevich
from brus16 import *

rects_gen = iter(range(1, 65))
new_rect = lambda count: [next(rects_gen) for _ in range(count)][0]

SKY_RECT = new_rect(count=1)
SKY_COLOR = rgb(0x1e2758)
SKY = [1, 0, 0, SCREEN_W, SCREEN_H, SKY_COLOR]

STAR_SIZE = 1
STAR = [1, 0, 0, 5, 5, rgb(0xffffff)]
STAR_COORDS = [(50, 100), (250, 50), (400, 60), (520, 90), (310, 120), (80, 220), (180, 350), (240, 270), (420, 430), (550, 370)]
STAR_RECTS = [new_rect(count=STAR_SIZE) for _ in STAR_COORDS]
STAR_SETUP = '\n'.join(
    f'''
    copy(star, {rect[star_rect].addr}, {RECT_SIZE * STAR_SIZE})
    poke({rect[star_rect].x}, {x})
    poke({rect[star_rect].y}, {y})
    '''.rstrip()
    for star_rect, (x, y)
    in zip(STAR_RECTS, STAR_COORDS))

# Font by Vladimir Miklashevich
SCORE_DIGITS = [1, 0, 0, 15, 30, SKY_COLOR, 0, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 5, 18, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 0, 6, 5, 18, SKY_COLOR, 0, 10, 0, 5, 24, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 0, 6, 10, 6, SKY_COLOR, 0, 5, 18, 10, 6, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 0, 6, 10, 6, SKY_COLOR, 0, 0, 18, 10, 6, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 0, 5, 12, SKY_COLOR, 0, 0, 18, 10, 12, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 10, 6, SKY_COLOR, 0, 0, 18, 10, 6, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 10, 6, SKY_COLOR, 0, 5, 18, 5, 6, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 5, 6, SKY_COLOR, 0, 0, 12, 10, 18, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 5, 6, SKY_COLOR, 0, 5, 18, 5, 6, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 5, 6, SKY_COLOR, 0, 0, 18, 10, 6, SKY_COLOR]

LEFT_DIGIT_RECT = new_rect(count=3)
LEFT_DIGIT = SCORE_DIGITS[:RECT_SIZE * 3]
RIGHT_DIGIT_RECT = new_rect(count=3)
RIGHT_DIGIT = SCORE_DIGITS[:RECT_SIZE * 3]

CLOUD_SIZE = 2
CLOUD_OFFS = 20
CLOUD_W = SCREEN_W // 4
CLOUD_H = SCREEN_W // 8
CLOUD = [1, 0, 0, CLOUD_W, CLOUD_H + CLOUD_OFFS, rgb(0x26316f),
         0, 0, 0, CLOUD_W + CLOUD_OFFS, CLOUD_H, rgb(0x26316f)]

CLOUD_A_RECT = new_rect(count=CLOUD_SIZE)
CLOUD_B_RECT = new_rect(count=CLOUD_SIZE)
CLOUD_C_RECT = new_rect(count=CLOUD_SIZE)

HOOK_RECT = new_rect(count=1)
HOOK_H = 150
HOOK_RANGE = SCREEN_W // 5
HOOK_LEFT_BOUNARY = SCREEN_W // 2 - HOOK_RANGE
HOOK_RIGHT_BOUNARY = SCREEN_W // 2 + HOOK_RANGE
HOOK = [1, HOOK_LEFT_BOUNARY, 0, 1, HOOK_H, rgb(0x565f97)]

HOOK_BOX_SIZE = 5
HOOK_BOX_RECT = new_rect(count=HOOK_BOX_SIZE)
HOOK_BOX_W = 70
HOOK_BOX = [1,  0,  0, 70, 70, rgb(0x3f51b5),
            0,  5,  5, 60, 60, rgb(0x002984),
            0,  7,  7, 27, 56, rgb(0x757de8),
            0, 36,  7, 27, 15, rgb(0x757de8),
            0, 36, 24, 27, 39, rgb(0x757de8)]

BUILDING_BOX_SIZE = 9
BUILDING_BOX_W = 70
BUILDING_BOX_RECT = new_rect(count=BUILDING_BOX_SIZE)
BUILDING_BOX_BOTTOM_RECT = new_rect(count=BUILDING_BOX_SIZE)

BUILDING_BOX_CURTAIN_MIN = 3
BUILDING_BOX_CURTAIN_MAX = 25
BUILDING_BOX_CURTAIN_END = 63

BUILDING_BOX_WARM_LIGHT = rgb(0xffc107)
BUILDING_BOX_WARM_CURTAIN = rgb(0xb28704)
BUILDING_BOX_COLD_LIGHT = rgb(0xe3e6f3)
BUILDING_BOX_COLD_CURTAIN = rgb(0xafb7df)

BUILDING_BOX_GREEN_LIGHT = rgb(0x33bdd1)
BUILDING_BOX_GREEN_CURTAIN = rgb(0x0480a6)
BUILDING_BOX_RED_LIGHT = rgb(0xd1333d)
BUILDING_BOX_RED_CURTAIN = rgb(0xa60400)
BUILDING_BOX_YELLOW_LIGHT = rgb(0xbdd133)
BUILDING_BOX_YELLOW_CURTAIN = rgb(0x80a604)
BUILDING_BOX_PINK_LIGHT = rgb(0xd133bd)
BUILDING_BOX_PINK_CURTAIN = rgb(0xa60480)

BUILDING_BOX_BASE = \
  [1,  0,  0, 70, 70, rgb(0x3f51b5),
   0,  5,  5, 60, 60, rgb(0x002984),
   0,  7,  7, 27, 56, BUILDING_BOX_WARM_LIGHT,
   0, 36,  7, 27, 15, BUILDING_BOX_WARM_LIGHT,
   0, 36, 24, 27, 39, BUILDING_BOX_WARM_LIGHT]

BUILDING_BOX = BUILDING_BOX_BASE + \
  [0,  7,  7, 10, 56, BUILDING_BOX_WARM_CURTAIN,
   0,  7,  7, 10, 56, BUILDING_BOX_WARM_CURTAIN,
   0, 53,  7, 10, 15, BUILDING_BOX_WARM_CURTAIN,
   0, 53, 24, 10, 39, BUILDING_BOX_WARM_CURTAIN]

BUILDING_BOX_LAZY_CAT = BUILDING_BOX_BASE + \
  [0, 10, 56, 14,  7, BUILDING_BOX_WARM_CURTAIN,
   0, 19, 50,  8,  6, BUILDING_BOX_WARM_CURTAIN,
   0, 19, 48,  3,  2, BUILDING_BOX_WARM_CURTAIN,
   0, 24, 48,  3,  2, BUILDING_BOX_WARM_CURTAIN]

BUILDING_BOX_SITTING_CAT = BUILDING_BOX_BASE + \
  [0, 15, 49,  8, 14, BUILDING_BOX_WARM_CURTAIN,
   0, 17, 45,  8,  6, BUILDING_BOX_WARM_CURTAIN,
   0, 17, 43,  3,  2, BUILDING_BOX_WARM_CURTAIN,
   0, 22, 43,  3,  2, BUILDING_BOX_WARM_CURTAIN]

BUILDING_BOX_CACTUS = BUILDING_BOX_BASE + \
  [0, 45, 56,  9,  7, BUILDING_BOX_WARM_CURTAIN,
   0, 48, 44,  3, 12, BUILDING_BOX_WARM_CURTAIN,
   0, 49, 48,  4,  3, BUILDING_BOX_WARM_CURTAIN,
   0, 52, 43,  3,  8, BUILDING_BOX_WARM_CURTAIN]

BUILDING_BOX_CLOTHES = BUILDING_BOX_BASE + \
  [0, 10, 51, 12, 12, BUILDING_BOX_WARM_CURTAIN,
   0, 14, 39, 12, 12, BUILDING_BOX_WARM_CURTAIN,
   0, 44, 48, 15, 15, BUILDING_BOX_WARM_CURTAIN,
   0, 44, 48, 15, 15, BUILDING_BOX_WARM_CURTAIN]

save_game('tower.bin', f'''
def main():
    setup()
    while 1:
        update()
        draw()
        wait()

def xorshift16():
    seed ^= seed << 7
    seed ^= seed >> 9
    seed ^= seed << 8
    return seed

def mask(n):
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    return n

def rnd(size):
    m = mask(size)
    n = xorshift16()
    while (n & m) >= size:
        n = xorshift16()
    return n & m

def random(lower, upper):
    size = upper - lower + 1
    return lower + rnd(size)

def copy(src, dst, size):
    end = src + size
    while src < end:
        dst[0] = src[0]
        src += 1
        dst += 1

def abs(value):
    if value > 0:
        return value
    return -value

def set_building_box_curtain_width(box, width):
    box[{RECT_W + 5 * RECT_SIZE}] = width
    box[{RECT_W + 6 * RECT_SIZE}] = width
    box[{RECT_W + 7 * RECT_SIZE}] = width
    box[{RECT_W + 8 * RECT_SIZE}] = width
    box[{RECT_X + 7 * RECT_SIZE}] = {BUILDING_BOX_CURTAIN_END} - width
    box[{RECT_X + 8 * RECT_SIZE}] = {BUILDING_BOX_CURTAIN_END} - width

def set_building_box_colors(box, light, curtain):
    box[{RECT_COLOR + 2 * RECT_SIZE}] = light
    box[{RECT_COLOR + 3 * RECT_SIZE}] = light
    box[{RECT_COLOR + 4 * RECT_SIZE}] = light
    box[{RECT_COLOR + 5 * RECT_SIZE}] = curtain
    box[{RECT_COLOR + 6 * RECT_SIZE}] = curtain
    box[{RECT_COLOR + 7 * RECT_SIZE}] = curtain
    box[{RECT_COLOR + 8 * RECT_SIZE}] = curtain

def set_building_box_shape(box, shape):
    copy(shape, box, {RECT_SIZE * BUILDING_BOX_SIZE})

def set_random_building_box_curtain_width(box):
    width = random({BUILDING_BOX_CURTAIN_MIN}, {BUILDING_BOX_CURTAIN_MAX})
    set_building_box_curtain_width(box, width)

def set_random_building_box_colors(box):
    n = random(0, 1)
    light = {BUILDING_BOX_WARM_LIGHT} * n + {BUILDING_BOX_COLD_LIGHT} * (1 - n)
    curtain = {BUILDING_BOX_WARM_CURTAIN} * n + {BUILDING_BOX_COLD_CURTAIN} * (1 - n)
    set_building_box_colors(box, light, curtain)

def set_random_building_box(box):
    n = random(0, 9)
    if n <= 5:
        set_building_box_shape(box, building_box)
        set_random_building_box_curtain_width(box)
    elif n == 6:
        set_building_box_shape(box, building_box_lazy_cat)
    elif n == 7:
        set_building_box_shape(box, building_box_sitting_cat)
    elif n == 8:
        set_building_box_shape(box, building_box_cactus)
    elif n == 9:
        set_building_box_shape(box, building_box_clothes)
    set_random_building_box_colors(box)

def get_next_building_box_disco_light_color(color):
    if color == {BUILDING_BOX_GREEN_LIGHT}:
        return {BUILDING_BOX_RED_LIGHT}
    if color == {BUILDING_BOX_RED_LIGHT}:
        return {BUILDING_BOX_YELLOW_LIGHT}
    if color == {BUILDING_BOX_YELLOW_LIGHT}:
        return {BUILDING_BOX_PINK_LIGHT}
    return {BUILDING_BOX_GREEN_LIGHT}

def get_next_building_box_disco_curtain_color(color):
    if color == {BUILDING_BOX_GREEN_CURTAIN}:
        return {BUILDING_BOX_RED_CURTAIN}
    if color == {BUILDING_BOX_RED_CURTAIN}:
        return {BUILDING_BOX_YELLOW_CURTAIN}
    if color == {BUILDING_BOX_YELLOW_CURTAIN}:
        return {BUILDING_BOX_PINK_CURTAIN}
    return {BUILDING_BOX_GREEN_CURTAIN}

def get_hook_box_pos_x():
    return hook_pos_x - {HOOK_BOX_W // 2}

def is_correctly_installed():
    return abs(get_hook_box_pos_x() - building_box_pos_x) < {HOOK_BOX_W // 3}

def is_brilliantly_installed():
    return abs(get_hook_box_pos_x() - building_box_pos_x) < 3

def is_installed():
    return hook_box_pos_y >= {SCREEN_H - BUILDING_BOX_W * 3}

def is_destroyed():
    return hook_box_pos_y >= {SCREEN_H}

def update_hook():
    if state == IDLE:
        hook_box_pos_y += hook_velocity_y
        hook_pos_x += hook_velocity_x
        if hook_box_pos_y >= {HOOK_H + HOOK_H // 4}:
            hook_velocity_y = -hook_velocity_y
        elif hook_box_pos_y <= {HOOK_H - HOOK_H // 4}:
            hook_velocity_y = -hook_velocity_y
        if hook_pos_x >= {HOOK_RIGHT_BOUNARY}:
            hook_velocity_x = -hook_velocity_x
        elif hook_pos_x <= {HOOK_LEFT_BOUNARY}:
            hook_velocity_x = -hook_velocity_x

def update_falling_hook_box():
    hook_box_pos_y += falling_speed
    if is_installed():
        if is_correctly_installed():
            state = SCROLLING
        else:
            state = DESTROYING

def update_destroying_hook_box():
    hook_box_pos_y += falling_speed
    if is_destroyed():
        state = IDLE
        score = 0
        building_box_bottom_disco = 0
        building_box_disco = 0
        building_box_pos_x = {SCREEN_W // 2 - BUILDING_BOX_W // 2}
        building_box_pos_y = {SCREEN_H - BUILDING_BOX_W * 2}
        building_box_bottom_pos_x = {SCREEN_W // 2 - BUILDING_BOX_W // 2}
        building_box_bottom_pos_y = {SCREEN_H - BUILDING_BOX_W}
        hook_box_pos_y = {HOOK_H}
        setup_building_box()

def update_hook_box():
    if state == FALLING:
        update_falling_hook_box()
    if state == DESTROYING:
        update_destroying_hook_box()

def update_scrolling_building():
    hook_box_pos_y += scrolling_speed
    building_box_pos_y += scrolling_speed
    building_box_bottom_pos_y += scrolling_speed
    if building_box_bottom_pos_y >= {SCREEN_H}:
        state = IDLE
        building_box_bottom_disco = building_box_disco
        building_box_disco = is_brilliantly_installed()
        building_box_bottom_pos_x = building_box_pos_x
        building_box_bottom_pos_y = building_box_pos_y
        building_box_pos_x = get_hook_box_pos_x()
        building_box_pos_y = {SCREEN_H - BUILDING_BOX_W * 2}
        copy({rect[BUILDING_BOX_RECT].addr}, {rect[BUILDING_BOX_BOTTOM_RECT].addr}, {RECT_SIZE * BUILDING_BOX_SIZE})
        set_random_building_box({rect[BUILDING_BOX_RECT].addr})
        hook_box_pos_y = {HOOK_H}
        score += building_box_disco

def update_building():
    if state == SCROLLING:
        update_scrolling_building()

def update_keyboard():
    if state == IDLE:
        keyboard_time += 1
        if keyboard_time <= keyboard_delta:
            return
        if peek({KEY_MEM + KEY_A}):
            state = FALLING
            keyboard_time = 0

def update_disco_colors():
    if building_box_disco | building_box_bottom_disco:
        building_box_disco_time += 1
        if building_box_disco_time <= building_box_disco_delta:
            return
        building_box_disco_light_color = get_next_building_box_disco_light_color(building_box_disco_light_color)
        building_box_disco_curtain_color = get_next_building_box_disco_curtain_color(building_box_disco_curtain_color)
        building_box_disco_time = 0

def update_building_box_disco():
    if building_box_disco:
        set_building_box_colors({rect[BUILDING_BOX_RECT].addr}, building_box_disco_light_color, building_box_disco_curtain_color)

def update_building_box_bottom_disco():
    if building_box_bottom_disco:
        set_building_box_colors({rect[BUILDING_BOX_BOTTOM_RECT].addr}, building_box_disco_light_color, building_box_disco_curtain_color)

def update_disco():
    update_disco_colors()
    update_building_box_disco()
    update_building_box_bottom_disco()

def update():
    update_keyboard()
    update_hook()
    update_hook_box()
    update_building()
    update_disco()

def draw_score():
    tens = 0
    ones = score
    while ones >= 10:
        ones -= 10
        tens += 1
    copy(score_digits + tens * {RECT_SIZE * 3}, {rect[LEFT_DIGIT_RECT].addr}, {RECT_SIZE * 3})
    copy(score_digits + ones * {RECT_SIZE * 3}, {rect[RIGHT_DIGIT_RECT].addr}, {RECT_SIZE * 3})
    poke({rect[LEFT_DIGIT_RECT].x}, {SCREEN_W // 2 - LEFT_DIGIT[3] * 2 // 2})
    poke({rect[LEFT_DIGIT_RECT].y}, {LEFT_DIGIT[4]})
    poke({rect[RIGHT_DIGIT_RECT].x}, {SCREEN_W // 2 + RIGHT_DIGIT[3] // 2})
    poke({rect[RIGHT_DIGIT_RECT].y}, {RIGHT_DIGIT[4]})

def draw_hook():
    poke({rect[HOOK_RECT].x}, hook_pos_x)
    poke({rect[HOOK_RECT].h}, hook_box_pos_y)

def draw_hook_box():
    poke({rect[HOOK_BOX_RECT].x}, get_hook_box_pos_x())
    poke({rect[HOOK_BOX_RECT].y}, hook_box_pos_y)

def draw_building():
    poke({rect[BUILDING_BOX_RECT].x}, building_box_pos_x)
    poke({rect[BUILDING_BOX_RECT].y}, building_box_pos_y)
    poke({rect[BUILDING_BOX_BOTTOM_RECT].x}, building_box_bottom_pos_x)
    poke({rect[BUILDING_BOX_BOTTOM_RECT].y}, building_box_bottom_pos_y)

def draw_cloud(cloud, velocity):
    cloud[{RECT_X}] += velocity
    if cloud[{RECT_X}] >= {SCREEN_W}:
        setup_cloud(cloud)

def draw_clouds():
    draw_cloud({rect[CLOUD_A_RECT].addr}, clouds_velocity)
    draw_cloud({rect[CLOUD_B_RECT].addr}, clouds_velocity * 2)
    draw_cloud({rect[CLOUD_C_RECT].addr}, clouds_velocity * 3)

def draw():
    draw_building()
    draw_hook()
    draw_hook_box()
    draw_score()
    draw_clouds()

def setup_building_box():
    copy(building_box, {rect[BUILDING_BOX_RECT].addr}, {RECT_SIZE * BUILDING_BOX_SIZE})
    copy(building_box, {rect[BUILDING_BOX_BOTTOM_RECT].addr}, {RECT_SIZE * BUILDING_BOX_SIZE})

def setup_cloud(cloud):
    copy(clouds, cloud, {RECT_SIZE * CLOUD_SIZE})
    cloud[{RECT_SIZE + RECT_X}] = random({-CLOUD_OFFS}, {CLOUD_OFFS})
    cloud[{RECT_SIZE + RECT_Y}] = random({-CLOUD_OFFS}, {CLOUD_OFFS})
    cloud[{RECT_SIZE + RECT_W}] = random({CLOUD_W // 2}, {CLOUD_W})
    cloud[{RECT_SIZE + RECT_H}] = random({CLOUD_H // 4}, {CLOUD_H // 2})
    cloud[{RECT_X}] = -(cloud[{RECT_W}] + {CLOUD_OFFS})
    cloud[{RECT_Y}] = random({CLOUD_H}, {SCREEN_H - CLOUD_H})
    cloud[{RECT_W}] = random({CLOUD_W // 2}, {CLOUD_W})
    cloud[{RECT_H}] = random({CLOUD_H // 4}, {CLOUD_H // 2})

def setup_clouds():
    setup_cloud({rect[CLOUD_A_RECT].addr})
    setup_cloud({rect[CLOUD_B_RECT].addr})
    setup_cloud({rect[CLOUD_C_RECT].addr})

def setup():
    copy(hook, {rect[HOOK_RECT].addr}, {RECT_SIZE})
    copy(hook_box, {rect[HOOK_BOX_RECT].addr}, {RECT_SIZE * HOOK_BOX_SIZE})
    copy(sky, {rect[SKY_RECT].addr}, {RECT_SIZE})
    setup_building_box()
    setup_clouds()
    {STAR_SETUP}

IDLE = 0
FALLING = 1
SCROLLING = 2
DESTROYING = 3
state = 0

sky = {SKY}
star = {STAR}
clouds = {CLOUD}
clouds_velocity = 1

building_box = {BUILDING_BOX}
building_box_lazy_cat = {BUILDING_BOX_LAZY_CAT}
building_box_sitting_cat = {BUILDING_BOX_SITTING_CAT}
building_box_cactus = {BUILDING_BOX_CACTUS}
building_box_clothes = {BUILDING_BOX_CLOTHES}

building_box_pos_x = {SCREEN_W // 2 - BUILDING_BOX_W // 2}
building_box_pos_y = {SCREEN_H - BUILDING_BOX_W * 2}
building_box_bottom_pos_x = {SCREEN_W // 2 - BUILDING_BOX_W // 2}
building_box_bottom_pos_y = {SCREEN_H - BUILDING_BOX_W}

building_box_disco_light_color = {BUILDING_BOX_GREEN_LIGHT}
building_box_disco_curtain_color = {BUILDING_BOX_GREEN_CURTAIN}
building_box_disco = 0
building_box_bottom_disco = 0
building_box_disco_time = 0
building_box_disco_delta = 30

hook_box = {HOOK_BOX}
hook_box_pos_y = {HOOK_H}
hook = {HOOK}
hook_pos_x = {HOOK_LEFT_BOUNARY}
hook_velocity_x = 4
hook_velocity_y = 1

falling_speed = 4
scrolling_speed = 2
score_digits = {SCORE_DIGITS}
score = 0
seed = 1

keyboard_time = 30
keyboard_delta = 30
''')
