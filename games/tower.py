# Author: Artyom Gorchakov & Vladimir Miklashevich
from brus16 import *

rects_gen = iter(range(1, 65))
new_rect = lambda count: [next(rects_gen) for _ in range(count)][0]

SKY_RECT = new_rect(1)
SKY_COLOR = rgb(0x1e2758)
SKY = [1, 0, 0, SCREEN_W, SCREEN_H, SKY_COLOR]

STAR_SIZE = 2
STAR_COLOR = rgb(0xffffff)
STAR = [1, 0,  0, 7, 3, STAR_COLOR,
        0, 2, -2, 3, 7, STAR_COLOR]

STARS = [(50, 100), (250, 50), (400, 60), (310, 120), (80, 220), (180, 350), (240, 270), (490, 230), (550, 370)]
STAR_RECTS = [new_rect(STAR_SIZE) for _ in STARS]
STAR_SETUP = '\n'.join(
    f'''
    copy(star, {rect[star_rect].addr}, {RECT_SIZE * STAR_SIZE})
    poke({rect[star_rect].x}, {x})
    poke({rect[star_rect].y}, {y})
    '''.rstrip()
    for star_rect, (x, y)
    in zip(STAR_RECTS, STARS))

# Font by Vladimir Miklashevich
SCORE_DIGITS = [1, 0, 0, 15, 30, SKY_COLOR, 0, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 5, 18, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 0, 6, 5, 18, SKY_COLOR, 0, 10, 0, 5, 24, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 0, 6, 10, 6, SKY_COLOR, 0, 5, 18, 10, 6, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 0, 6, 10, 6, SKY_COLOR, 0, 0, 18, 10, 6, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 0, 5, 12, SKY_COLOR, 0, 0, 18, 10, 12, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 10, 6, SKY_COLOR, 0, 0, 18, 10, 6, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 10, 6, SKY_COLOR, 0, 5, 18, 5, 6, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 5, 6, SKY_COLOR, 0, 0, 12, 10, 18, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 5, 6, SKY_COLOR, 0, 5, 18, 5, 6, SKY_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 5, 6, SKY_COLOR, 0, 0, 18, 10, 6, SKY_COLOR]

LEFT_DIGIT_RECT = new_rect(3)
MIDDLE_DIGIT_RECT = new_rect(3)
RIGHT_DIGIT_RECT = new_rect(3)

ZERO = SCORE_DIGITS[:RECT_SIZE * 3]
LEFT_DIGIT = MIDDLE_DIGIT = RIGHT_DIGIT = ZERO
LEFT_DIGIT_X = LEFT_DIGIT_Y = 30

CLOUD_SIZE = 2
CLOUD_OFFS = 20
CLOUD_W = SCREEN_W // 4
CLOUD_H = SCREEN_W // 8
CLOUD = [1, 0, 0, CLOUD_W, CLOUD_H + CLOUD_OFFS, rgb(0x26316f),
         0, 0, 0, CLOUD_W + CLOUD_OFFS, CLOUD_H, rgb(0x26316f)]

CLOUD_A_RECT = new_rect(CLOUD_SIZE)
CLOUD_B_RECT = new_rect(CLOUD_SIZE)
CLOUD_C_RECT = new_rect(CLOUD_SIZE)

WARM_LIGHT = rgb(0xffc107)
WARM_CURTAIN = rgb(0xb28704)
COLD_LIGHT = rgb(0xe3e6f3)
COLD_CURTAIN = rgb(0xafb7df)
GREEN_LIGHT = rgb(0x33bdd1)
GREEN_CURTAIN = rgb(0x0480a6)
RED_LIGHT = rgb(0xd1333d)
RED_CURTAIN = rgb(0xa60400)
YELLOW_LIGHT = rgb(0xbdd133)
YELLOW_CURTAIN = rgb(0x80a604)
PINK_LIGHT = rgb(0xd133bd)
PINK_CURTAIN = rgb(0xa60480)

MOON_SIZE = 3
MOON_RECT = new_rect(MOON_SIZE)
MOON = [1, SCREEN_W - 60, LEFT_DIGIT_Y - 5, 20, 40, WARM_LIGHT,
        0, -5, 5, 20, 30, WARM_LIGHT,
        0, 15, 5, 20, 30, SKY_COLOR]

HOOK_RECT = new_rect(1)
HOOK_H = 150
HOOK_RANGE = SCREEN_W // 5
HOOK_LEFT_BOUNARY = SCREEN_W // 2 - HOOK_RANGE
HOOK_RIGHT_BOUNARY = SCREEN_W // 2 + HOOK_RANGE
HOOK = [1, HOOK_LEFT_BOUNARY, 0, 1, HOOK_H, rgb(0x565f97)]

HOOK_BOX_SIZE = 5
HOOK_BOX_RECT = new_rect(HOOK_BOX_SIZE)
HOOK_BOX_W = 70
HOOK_BOX = [1,  0,  0, 70, 70, rgb(0x3f51b5),
            0,  5,  5, 60, 60, rgb(0x002984),
            0,  7,  7, 27, 56, rgb(0x757de8),
            0, 36,  7, 27, 15, rgb(0x757de8),
            0, 36, 24, 27, 39, rgb(0x757de8)]

HOOK_MAGNET_RECT = new_rect(1)
HOOK_MAGNET_W = HOOK_BOX_W // 2
HOOK_MAGNET_H = 10
HOOK_MAGNET = [1, HOOK_LEFT_BOUNARY - HOOK_MAGNET_W // 2, 0,
                  HOOK_MAGNET_W, HOOK_MAGNET_H, rgb(0x3f51b5)]

BOX_SIZE = 9
BOX_W = 70
BOX_RECT = new_rect(BOX_SIZE)
BOX_BOTTOM_RECT = new_rect(BOX_SIZE)

BOX_CURTAIN_MIN = 3
BOX_CURTAIN_MAX = 25
BOX_CURTAIN_END = 63

BOX_BASE = \
  [1,  0,  0, 70, 70, rgb(0x3f51b5),
   0,  5,  5, 60, 60, rgb(0x002984),
   0,  7,  7, 27, 56, WARM_LIGHT,
   0, 36,  7, 27, 15, WARM_LIGHT,
   0, 36, 24, 27, 39, WARM_LIGHT]

BOX = BOX_BASE + \
  [0,  7,  7, 10, 56, WARM_CURTAIN,
   0,  7,  7, 10, 56, WARM_CURTAIN,
   0, 53,  7, 10, 15, WARM_CURTAIN,
   0, 53, 24, 10, 39, WARM_CURTAIN]

BOX_LAZY_CAT = BOX_BASE + \
  [0, 10, 56, 14,  7, WARM_CURTAIN,
   0, 19, 50,  8,  6, WARM_CURTAIN,
   0, 19, 48,  3,  2, WARM_CURTAIN,
   0, 24, 48,  3,  2, WARM_CURTAIN]

BOX_SITTING_CAT = BOX_BASE + \
  [0, 15, 49,  8, 14, WARM_CURTAIN,
   0, 17, 45,  8,  6, WARM_CURTAIN,
   0, 17, 43,  3,  2, WARM_CURTAIN,
   0, 22, 43,  3,  2, WARM_CURTAIN]

BOX_CACTUS = BOX_BASE + \
  [0, 45, 56,  9,  7, WARM_CURTAIN,
   0, 48, 44,  3, 12, WARM_CURTAIN,
   0, 49, 48,  4,  3, WARM_CURTAIN,
   0, 52, 43,  3,  8, WARM_CURTAIN]

BOX_CLOTHES = BOX_BASE + \
  [0, 10, 51, 12, 12, WARM_CURTAIN,
   0, 14, 39, 12, 12, WARM_CURTAIN,
   0, 44, 48, 15, 15, WARM_CURTAIN,
   0, 44, 48, 15, 15, WARM_CURTAIN]

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

def set_box_curtain_width(rect, width):
    rect[{RECT_W + 5 * RECT_SIZE}] = width
    rect[{RECT_W + 6 * RECT_SIZE}] = width
    rect[{RECT_W + 7 * RECT_SIZE}] = width
    rect[{RECT_W + 8 * RECT_SIZE}] = width
    rect[{RECT_X + 7 * RECT_SIZE}] = {BOX_CURTAIN_END} - width
    rect[{RECT_X + 8 * RECT_SIZE}] = {BOX_CURTAIN_END} - width

def set_box_colors(rect, light, curtain):
    rect[{RECT_COLOR + 2 * RECT_SIZE}] = light
    rect[{RECT_COLOR + 3 * RECT_SIZE}] = light
    rect[{RECT_COLOR + 4 * RECT_SIZE}] = light
    rect[{RECT_COLOR + 5 * RECT_SIZE}] = curtain
    rect[{RECT_COLOR + 6 * RECT_SIZE}] = curtain
    rect[{RECT_COLOR + 7 * RECT_SIZE}] = curtain
    rect[{RECT_COLOR + 8 * RECT_SIZE}] = curtain

def set_box_shape(rect, shape):
    copy(shape, rect, {RECT_SIZE * BOX_SIZE})

def set_random_box_curtain_width(rect):
    set_box_curtain_width(rect, random({BOX_CURTAIN_MIN}, {BOX_CURTAIN_MAX}))

def set_random_box_colors(rect):
    n = random(0, 1)
    light = {WARM_LIGHT} * n + {COLD_LIGHT} * (1 - n)
    curtain = {WARM_CURTAIN} * n + {COLD_CURTAIN} * (1 - n)
    set_box_colors(rect, light, curtain)

def set_random_box(rect):
    n = random(0, 9)
    if n <= 5:
        set_box_shape(rect, box)
        set_random_box_curtain_width(rect)
    if n == 6: set_box_shape(rect, box_lazy_cat)
    if n == 7: set_box_shape(rect, box_sitting_cat)
    if n == 8: set_box_shape(rect, box_cactus)
    if n == 9: set_box_shape(rect, box_clothes)
    set_random_box_colors(rect)

def get_next_disco_light(color):
    if color == {GREEN_LIGHT}:
        return {RED_LIGHT}
    if color == {RED_LIGHT}:
        return {YELLOW_LIGHT}
    if color == {YELLOW_LIGHT}:
        return {PINK_LIGHT}
    return {GREEN_LIGHT}

def get_next_disco_curtain(color):
    if color == {GREEN_CURTAIN}:
        return {RED_CURTAIN}
    if color == {RED_CURTAIN}:
        return {YELLOW_CURTAIN}
    if color == {YELLOW_CURTAIN}:
        return {PINK_CURTAIN}
    return {GREEN_CURTAIN}

def get_hook_box_pos_x():
    return hook_pos_x - {HOOK_BOX_W // 2}

def is_correctly_installed():
    return abs(get_hook_box_pos_x() - box_pos_x) < {HOOK_BOX_W // 4}

def is_brilliantly_installed():
    return abs(get_hook_box_pos_x() - box_pos_x) < 3

def is_installed():
    return hook_box_pos_y >= {SCREEN_H - BOX_W * 3}

def is_destroyed():
    return hook_box_pos_y >= {SCREEN_H}

def bound_velocity(velocity, pos, lb, rb):
    if (pos >= rb) | (pos <= lb):
        return -velocity
    return velocity

def update_idle_hook():
    hook_box_pos_y += hook_box_vy
    hook_pos_x += hook_box_vx
    hook_h = hook_box_pos_y
    hook_box_vy = bound_velocity(hook_box_vy, hook_box_pos_y, {HOOK_H - HOOK_H // 4}, {HOOK_H + HOOK_H // 4})
    hook_box_vx = bound_velocity(hook_box_vx, hook_pos_x, {HOOK_LEFT_BOUNARY}, {HOOK_RIGHT_BOUNARY})

def update_falling_hook():
    hook_h -= spawning_speed * 2
    if hook_h <= 0:
        hook_h = 0

def update_hook():
    if state == IDLE:
        update_idle_hook()
    elif state == FALLING:
        update_falling_hook()

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
        state = SPAWNING
        score = 0
        box_bottom_disco = 0
        box_disco = 0
        box_pos_x = {SCREEN_W // 2 - BOX_W // 2}
        box_pos_y = {SCREEN_H - BOX_W * 2}
        box_bottom_pos_x = {SCREEN_W // 2 - BOX_W // 2}
        box_bottom_pos_y = {SCREEN_H - BOX_W}
        hook_box_pos_y = {HOOK_H}
        setup_box()
        hook_box_pos_y = {-HOOK_BOX_W}
        hook_pos_y = 1

def update_spawning_hook_box():
    hook_box_pos_y += spawning_speed
    if hook_box_pos_y >= {HOOK_H}:
        hook_box_pos_y = {HOOK_H}
        state = IDLE
    if hook_box_pos_y >= 0:
        hook_h = hook_box_pos_y
    hook_pos_x += hook_box_vx
    hook_box_vx = bound_velocity(hook_box_vx, hook_pos_x, {HOOK_LEFT_BOUNARY}, {HOOK_RIGHT_BOUNARY})
      
def update_hook_box():
    if state == FALLING:
        update_falling_hook_box()
    elif state == DESTROYING:
        update_destroying_hook_box()
    elif state == SPAWNING:
        update_spawning_hook_box()

def update_scrolling_building():
    hook_box_pos_y += scrolling_speed
    box_pos_y += scrolling_speed
    box_bottom_pos_y += scrolling_speed
    if box_bottom_pos_y >= {SCREEN_H}:
        state = SPAWNING
        box_bottom_disco = box_disco
        box_disco = is_brilliantly_installed()
        box_bottom_pos_x = box_pos_x
        box_bottom_pos_y = box_pos_y
        box_pos_x = get_hook_box_pos_x()
        box_pos_y = {SCREEN_H - BOX_W * 2}
        copy({rect[BOX_RECT].addr}, {rect[BOX_BOTTOM_RECT].addr}, {RECT_SIZE * BOX_SIZE})
        set_random_box({rect[BOX_RECT].addr})
        hook_box_pos_y = {-HOOK_BOX_W}
        hook_pos_y = 1
        score += 1

def update_building():
    if state == SCROLLING:
        update_scrolling_building()

def update_keyboard():
    if (state == IDLE) | (state == SPAWNING):
        keyboard_time += 1
        if keyboard_time <= keyboard_delta:
            return
        if peek({KEY_MEM + KEY_A}):
            state = FALLING
            keyboard_time = 0

def update_disco():
    if box_disco | box_bottom_disco:
        disco_time += 1
        if disco_time <= disco_delta:
            return
        disco_light = get_next_disco_light(disco_light)
        disco_curtain = get_next_disco_curtain(disco_curtain)
        disco_time = 0

def update_score():
    hundreds = 0
    tens = 0
    ones = score
    while ones >= 10:
        ones -= 10
        tens += 1
    while tens >= 10:
        tens -= 10
        hundreds += 1

def update():
    update_keyboard()
    update_hook()
    update_hook_box()
    update_building()
    update_disco()
    update_score()

def draw_score():
    copy(score_digits + hundreds * {RECT_SIZE * 3}, {rect[LEFT_DIGIT_RECT].addr}, {RECT_SIZE * 3})
    copy(score_digits + tens * {RECT_SIZE * 3}, {rect[MIDDLE_DIGIT_RECT].addr}, {RECT_SIZE * 3})
    copy(score_digits + ones * {RECT_SIZE * 3}, {rect[RIGHT_DIGIT_RECT].addr}, {RECT_SIZE * 3})
    poke({rect[LEFT_DIGIT_RECT].x}, {LEFT_DIGIT_X})
    poke({rect[LEFT_DIGIT_RECT].y}, {LEFT_DIGIT_Y})
    poke({rect[MIDDLE_DIGIT_RECT].x}, {LEFT_DIGIT_X + RIGHT_DIGIT[3] + RIGHT_DIGIT[3] // 2})
    poke({rect[MIDDLE_DIGIT_RECT].y}, {LEFT_DIGIT_Y})
    poke({rect[RIGHT_DIGIT_RECT].x}, {LEFT_DIGIT_X + 3 * RIGHT_DIGIT[3]})
    poke({rect[RIGHT_DIGIT_RECT].y}, {LEFT_DIGIT_Y})

def draw_hook():
    poke({rect[HOOK_RECT].x}, hook_pos_x)
    poke({rect[HOOK_RECT].h}, hook_h)
    poke({rect[HOOK_MAGNET_RECT].x}, hook_pos_x - {HOOK_MAGNET_W // 2})
    poke({rect[HOOK_MAGNET_RECT].y}, hook_h - {HOOK_MAGNET_H})

def draw_hook_box():
    poke({rect[HOOK_BOX_RECT].x}, get_hook_box_pos_x())
    poke({rect[HOOK_BOX_RECT].y}, hook_box_pos_y)

def draw_building():
    poke({rect[BOX_RECT].x}, box_pos_x)
    poke({rect[BOX_RECT].y}, box_pos_y)
    poke({rect[BOX_BOTTOM_RECT].x}, box_bottom_pos_x)
    poke({rect[BOX_BOTTOM_RECT].y}, box_bottom_pos_y)

def draw_cloud(cloud, time, velocity):
    if time <= cloud_time_delta:
        return time + velocity
    cloud[{RECT_X}] += 1
    if cloud[{RECT_X}] >= {SCREEN_W}:
        setup_cloud(cloud)
    return 0

def draw_clouds():
    cloud_a_time = draw_cloud({rect[CLOUD_A_RECT].addr}, cloud_a_time, 1)
    cloud_b_time = draw_cloud({rect[CLOUD_B_RECT].addr}, cloud_b_time, 2)
    cloud_c_time = draw_cloud({rect[CLOUD_C_RECT].addr}, cloud_c_time, 3)

def draw_disco():
    if box_disco:
        set_box_colors({rect[BOX_RECT].addr}, disco_light, disco_curtain)
    if box_bottom_disco:
        set_box_colors({rect[BOX_BOTTOM_RECT].addr}, disco_light, disco_curtain)

def draw_moon():
    disco = box_disco & box_bottom_disco
    color = disco_light * disco + {WARM_LIGHT} * (1 - disco)
    poke({rect[MOON_RECT].color}, color)
    poke({rect[MOON_RECT + 1].color}, color)

def draw():
    draw_building()
    draw_hook()
    draw_hook_box()
    draw_score()
    draw_clouds()
    draw_disco()
    draw_moon()

def setup_box():
    copy(box, {rect[BOX_RECT].addr}, {RECT_SIZE * BOX_SIZE})
    copy(box, {rect[BOX_BOTTOM_RECT].addr}, {RECT_SIZE * BOX_SIZE})

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
    poke({rect[CLOUD_A_RECT].x}, 100)
    poke({rect[CLOUD_B_RECT].x}, 300)
    poke({rect[CLOUD_C_RECT].x}, 200)

def setup_moon():
    copy(moon, {rect[MOON_RECT].addr}, {RECT_SIZE * MOON_SIZE})

def setup():
    copy(hook, {rect[HOOK_RECT].addr}, {RECT_SIZE})
    copy(hook_box, {rect[HOOK_BOX_RECT].addr}, {RECT_SIZE * HOOK_BOX_SIZE})
    copy(hook_magnet, {rect[HOOK_MAGNET_RECT].addr}, {RECT_SIZE})
    copy(sky, {rect[SKY_RECT].addr}, {RECT_SIZE})
    setup_box()
    setup_clouds()
    setup_moon()
    {STAR_SETUP}

IDLE = 0
FALLING = 1
SCROLLING = 2
DESTROYING = 3
SPAWNING = 4
state = 0

sky = {SKY}
star = {STAR}
moon = {MOON}
clouds = {CLOUD}
clouds_velocity = 1
cloud_a_time = 0
cloud_b_time = 0
cloud_c_time = 0
cloud_time_delta = 3

box = {BOX}
box_lazy_cat = {BOX_LAZY_CAT}
box_sitting_cat = {BOX_SITTING_CAT}
box_cactus = {BOX_CACTUS}
box_clothes = {BOX_CLOTHES}

box_pos_x = {SCREEN_W // 2 - BOX_W // 2}
box_pos_y = {SCREEN_H - BOX_W * 2}
box_bottom_pos_x = {SCREEN_W // 2 - BOX_W // 2}
box_bottom_pos_y = {SCREEN_H - BOX_W}

box_disco = 0
box_bottom_disco = 0
disco_light = {GREEN_LIGHT}
disco_curtain = {GREEN_CURTAIN}
disco_time = 0
disco_delta = 30

hook = {HOOK}
hook_box = {HOOK_BOX}
hook_magnet = {HOOK_MAGNET}
hook_box_pos_y = {HOOK_H}
hook_h = {HOOK_H}
hook_pos_x = {HOOK_LEFT_BOUNARY}
hook_box_vx = 4
hook_box_vy = 1

falling_speed = 4
scrolling_speed = 2
spawning_speed = 6

score_digits = {SCORE_DIGITS}
score = 0
hundreds = 0
tens = 0
ones = 0
seed = 1

keyboard_time = 30
keyboard_delta = 30
''')
