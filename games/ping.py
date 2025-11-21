# Author: Peter Sovietov
from brus16 import *

def to_center(table, width, height):
    a, _, _, w, h, color = table
    x, y = (width - w) // 2, (height - h) // 2
    return [a, x, y, w, h, color]

BG_COLOR = rgb(0x202010)
BG_HIGH_COLOR = rgb(0x404020)
BG_RECT = 0
BG = [1, 0, 0, SCREEN_W, SCREEN_H, BG_COLOR]

SCALE = 1.7
TABLE_W, TABLE_H = round(274 * SCALE), round(152.5 * SCALE)
TABLE1 = to_center([1, 0, 0, TABLE_W, TABLE_H, rgb(0xe0e0e0)],
                   SCREEN_W, SCREEN_H)
BORDER = 3
TABLE2 = [0, BORDER, BORDER, TABLE_W - BORDER * 2,
          TABLE_H - BORDER * 2, rgb(0x008033)]

HLINE = to_center([0, 0, 0, TABLE_W, BORDER, rgb(0xe0e0e0)],
                  TABLE_W, TABLE_H)

NET = to_center([1, 0, 0, BORDER * 2, TABLE_H + BORDER * 8, rgb(0x6f7c91)],
                SCREEN_W, SCREEN_H)
NET_SHADOW1 = [1, NET[1] + BORDER * 2, NET[2] + BORDER * 5,
               BORDER * 4, TABLE_H - BORDER, rgb(0x393f49)]
NET_SHADOW2 = [0, 0, HLINE[2] - BORDER, BORDER * 4, BORDER, rgb(0x535d6c)]

BALL_W = 7
BALL_GAP = 1
BALL_SHADOW_RECT = 7
BALL_SHADOW = [1, 0, 0, BALL_W, BALL_W, rgb(0x000000)]
BALL1_RECT = 8
BALL1 = [1, 0, 0, BALL_W - BALL_GAP * 2, BALL_W, rgb(0xffff00)]
BALL2 = [0, -BALL_GAP, BALL_GAP, BALL_W, BALL_W - BALL_GAP * 2, rgb(0xffff00)]

RACKET_W, RACKET_H = 4, round(17 * SCALE)
HANDLE_W, HANDLE_H = 6, round(10 * SCALE)
LEFT_RACKET_RECT = 10
LEFT_RACKET1 = [1, 90, 100, RACKET_W, RACKET_H, rgb(0x2a2aff)]
LEFT_RACKET2 = [0, -1, RACKET_H, HANDLE_W, HANDLE_H, rgb(0xb97b18)]

RIGHT_RACKET_RECT = 12
RIGHT_RACKET1 = [1, 500, 200, RACKET_W, RACKET_H, rgb(0xff0000)]
RIGHT_RACKET2 = [0, -1, -HANDLE_H, HANDLE_W, HANDLE_H, rgb(0xb97b18)]

LEFT_RACKET_X = TABLE1[1] - TABLE1[1] // 2
LEFT_RACKET_Y = SCREEN_H // 2 - RACKET_H // 2
RIGHT_RACKET_X = TABLE1[1] + TABLE1[1] // 2 + TABLE_W - RACKET_W
RIGHT_RACKET_Y = SCREEN_H // 2 - RACKET_H // 2

# Font by Vladimir Miklashevich
SCORE_DIGITS = [1, 0, 0, 15, 30, BG_COLOR, 0, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 5, 18, BG_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 0, 6, 5, 18, BG_COLOR, 0, 10, 0, 5, 24, BG_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 0, 6, 10, 6, BG_COLOR, 0, 5, 18, 10, 6, BG_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 0, 6, 10, 6, BG_COLOR, 0, 0, 18, 10, 6, BG_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 0, 5, 12, BG_COLOR, 0, 0, 18, 10, 12, BG_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 10, 6, BG_COLOR, 0, 0, 18, 10, 6, BG_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 10, 6, BG_COLOR, 0, 5, 18, 5, 6, BG_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 5, 6, BG_COLOR, 0, 0, 12, 10, 18, BG_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 5, 6, BG_COLOR, 0, 5, 18, 5, 6, BG_COLOR, 1, 0, 0, 15, 30, rgb(0xffffff), 0, 5, 6, 5, 6, BG_COLOR, 0, 0, 18, 10, 6, BG_COLOR]

LEFT_DIGIT_RECT = 14
LEFT_DIGIT = SCORE_DIGITS[:RECT_SIZE * 3]
RIGHT_DIGIT_RECT = 17
RIGHT_DIGIT = SCORE_DIGITS[:RECT_SIZE * 3]

PLAY_RECTS = BG + TABLE1 + TABLE2 + HLINE + NET + NET_SHADOW1 + NET_SHADOW2 + \
             BALL_SHADOW + BALL1 + BALL2 + LEFT_RACKET1 + LEFT_RACKET2 + \
             RIGHT_RACKET1 + RIGHT_RACKET2 + LEFT_DIGIT + RIGHT_DIGIT

TABLE_BBOX = TABLE1[1:5]
NET_BBOX = NET[1:5]
BALL_BBOX = [0, 0, BALL_W, BALL_W]
RACKET_BBOX = [0, 0, RACKET_W, RACKET_H]
PREV_BALL_BBOX = [0, 0, BALL_W, BALL_W]
PREV_RACKET_BBOX = [0, 0, RACKET_W, RACKET_H]

BITS = 5
GRAVITY = 10
TABLE_FRICTION = 25
TABLE_DAMPING = 30
NET_DAMPING = 5
NET_HEIGHT = 25 << BITS
MAX_VX = 300
RACKET_STEP = 16
AI_STEP = 2
MAX_ANGLE = 6
BALL_VZ = 90
BALL_Z = 90 << BITS
MIN_POWER = 150
MAX_POWER = 300
FLAT_ZONE = 3
DELAY = 60

SERVE = 0
PLAY = 1
LOSE = 2

save_game('ping.bin', f'''
def main():
    setup()
    while 1:
        draw()
        wait()

def setup():
    copy(play_rects, {rect[0].addr}, {len(PLAY_RECTS)})
    draw_score()
    reset_state()

def draw():
    if game_state == {SERVE}:
        serve()
    elif game_state == {PLAY}:
        play()
    elif game_state == {LOSE}:
        lose()
    game_state = change_state(game_state)

def serve():
    y_center = {RACKET_H // 2 - BALL_W // 2}
    if who_serve == 0:
        ball_x = (left_racket_x + {RACKET_W + BALL_GAP}) << {BITS}
        ball_y = (left_racket_y + y_center) << {BITS}
    else:
        ball_x = (right_racket_x - {BALL_W - BALL_GAP}) << {BITS}
        ball_y = (right_racket_y + y_center) << {BITS}
    draw_ball()
    draw_rackets()

def play():
    get_prev_coords()
    control_rackets()
    if peek({KEY_MEM + KEY_A}):
        left_power = {MAX_POWER}
    else:
        left_power = {MIN_POWER}
    ball_hit = move_ball()
    left_hit = check_left_racket()
    right_hit = check_right_racket()
    net_hit = check_net()
    draw_ball()
    draw_rackets()

def lose():
    get_prev_coords()
    ball_hit = move_ball()
    net_hit = check_net()
    draw_ball()
    draw_rackets()

def change_state(game_state):
    if game_state == {SERVE}:
        return change_serve_state()
    if game_state == {PLAY}:
        return change_play_state()
    if game_state == {LOSE}:
        return change_lose_state()
    return game_state

def change_serve_state():
    if peek({KEY_MEM + KEY_A}) & (who_serve == 0):
        left_power = {MAX_POWER}
        strike(0)
        return {PLAY}
    elif who_serve == 1:
        right_power = {MAX_POWER}
        strike(1)
        return {PLAY}
    return {SERVE}

def change_play_state():
    poke({rect[BG_RECT].color}, {BG_COLOR})
    other_side = (ball_x > {(SCREEN_W // 2) << BITS}) != who_serve
    if net_hit:
        return {LOSE}
    if ball_hit:
        if is_on_table() & other_side & (table_hit_count == 0):
            table_hit_count = 1
            poke({rect[BG_RECT].color}, {BG_HIGH_COLOR})
            return {PLAY}
        if table_hit_count:
            who_serve = 1 - who_serve
        return {LOSE}
    if left_hit:
        who_serve = 0
        if table_hit_count == 1:
            table_hit_count = 0
            return {PLAY}
        return {LOSE}
    if right_hit:
        who_serve = 1
        if table_hit_count == 1:
            table_hit_count = 0
            return {PLAY}
        return {LOSE}
    return {PLAY}

def change_lose_state():
    if timer_on == 0:
        timer_on = 1
        timer = {DELAY}
        update_score()
        return {LOSE}
    timer -= 1
    if (timer == 0) | (is_on_screen() == 0):
        reset_state()
        return {SERVE}
    return {LOSE}

def update_score():
    if who_serve == 1:
        left_score += 1
    else:
        right_score += 1
    if (left_score > 9) | (right_score > 9):
        left_score = 0
        right_score = 0
    copy(score_digits + left_score * {RECT_SIZE * 3}, {rect[LEFT_DIGIT_RECT].addr}, {RECT_SIZE * 3})
    copy(score_digits + right_score * {RECT_SIZE * 3}, {rect[RIGHT_DIGIT_RECT].addr}, {RECT_SIZE * 3})
    draw_score()

def reset_state():
    timer_on = 0
    table_hit_count = 0
    left_racket_x = {LEFT_RACKET_X}
    left_racket_y = {LEFT_RACKET_Y}
    right_racket_x = {RIGHT_RACKET_X}
    right_racket_y = {RIGHT_RACKET_Y}
    ball_z = {BALL_Z}
    ball_vx = 0
    ball_vy = 0
    ball_vz = 0

def is_on_table():
    return hit(ball_bbox, table_bbox)

def is_on_screen():
    return hit(ball_bbox, screen_bbox)

def get_prev_coords():
    prev_left_racket_x = left_racket_x
    prev_left_racket_y = left_racket_y
    prev_right_racket_x = right_racket_x
    prev_right_racket_y = right_racket_y
    update_ball_bbox(prev_ball_bbox)

def control_left_racket():
    if peek({KEY_MEM + KEY_UP}):
        left_racket_vy = min(left_racket_vy, 0) - 1
    elif peek({KEY_MEM + KEY_DOWN}):
        left_racket_vy = max(left_racket_vy, 0) + 1
    else:
        left_racket_vy = 0
    if peek({KEY_MEM + KEY_LEFT}):
        left_racket_vx = min(left_racket_vx, 0) - 1
    elif peek({KEY_MEM + KEY_RIGHT}):
        left_racket_vx = max(left_racket_vx, 0) + 1
    else:
        left_racket_vx = 0
    left_racket_vx = limit(left_racket_vx, {-RACKET_STEP}, {RACKET_STEP})
    left_racket_vy = limit(left_racket_vy, {-RACKET_STEP}, {RACKET_STEP})
    left_racket_x += shra(left_racket_vx, 1)
    left_racket_y += shra(left_racket_vy, 1)

def control_right_racket():
    target_y = right_racket_y
    if ball_vx > 0:
        dist = (right_racket_x << {BITS}) - ball_x
        if dist > 0:
            frames = shra(dist, 8)
            pred_y = ball_y + (ball_vy * frames)
            target_y = shra(pred_y, {BITS}) - {RACKET_H // 2}
    target_x = right_racket_x    
    if (ball_vx > 0) & table_hit_count & (ball_z > {NET_HEIGHT}):
        ball_px = shra(ball_x, {BITS})
        offset = {RACKET_W + BALL_W + 4}
        target_x = ball_px + offset
    diff_x = target_x - right_racket_x
    right_racket_x += limit(diff_x, {-AI_STEP}, {AI_STEP})
    diff_y = target_y - right_racket_y
    right_racket_y += limit(diff_y, {-AI_STEP}, {AI_STEP})
    if right_racket_x < {TABLE1[1] + TABLE_W - 150}:
        right_power = {MIN_POWER}
    else:
        right_power = {MAX_POWER}

def limit_rackets():
    left_racket_x = limit(left_racket_x, 1, {NET[1] - HANDLE_W - BALL_W})
    left_racket_y = limit(left_racket_y, 0, {SCREEN_H - RACKET_H - HANDLE_H})
    right_racket_x = limit(right_racket_x, {NET[1] + HANDLE_W + BALL_W + 1}, {SCREEN_W - HANDLE_W + 1})
    right_racket_y = limit(right_racket_y, {HANDLE_H}, {SCREEN_H - RACKET_H})

def control_rackets():
    control_left_racket()
    control_right_racket()
    limit_rackets()

def check_net():
    update_ball_bbox(ball_bbox)
    if tunnel_hit(prev_ball_bbox, ball_bbox, net_bbox, net_bbox) & (ball_z < {NET_HEIGHT}):
        ball_vx = -shra(ball_vx * {NET_DAMPING}, {BITS})
        ball_vy = shra(ball_vy * {NET_DAMPING}, {BITS})
        if ball_vx < 0:
            ball_x = (net_bbox[0] - {BALL_W} - 1) << {BITS}
        else:
            ball_x = (net_bbox[0] + net_bbox[2] + 1) << {BITS}
        return 1
    return 0

def strike(who):
    ball_vz = {BALL_VZ}
    ball_z = {BALL_Z}
    if who == 0:
        ball_x = (left_racket_x + {RACKET_W + BALL_W + 1}) << {BITS}
        ball_vx = min({MAX_VX}, left_power)
    else:
        ball_x = (right_racket_x - {BALL_W} - 1) << {BITS}
        ball_vx = max({-MAX_VX}, -right_power)

def check_left_racket():
    if ball_vx > 0:
        return 0
    update_ball_bbox(ball_bbox)
    prev_racket_bbox[0] = prev_left_racket_x
    prev_racket_bbox[1] = prev_left_racket_y
    racket_bbox[0] = left_racket_x
    racket_bbox[1] = left_racket_y    
    if tunnel_hit(prev_ball_bbox, ball_bbox, prev_racket_bbox, racket_bbox):
        strike(0)
        ball_center_y = ball_bbox[1] + {BALL_W // 2}
        racket_center_y = left_racket_y + {RACKET_H // 2}
        diff = ball_center_y - racket_center_y
        diff -= limit(diff, {-FLAT_ZONE}, {FLAT_ZONE})           
        y_power = min(left_power, {MAX_ANGLE})
        ball_vy = diff * {MAX_ANGLE}
        return 1
    return 0

def check_right_racket():
    if ball_vx < 0:
        return 0
    update_ball_bbox(ball_bbox)
    prev_racket_bbox[0] = prev_right_racket_x
    prev_racket_bbox[1] = prev_right_racket_y
    racket_bbox[0] = right_racket_x
    racket_bbox[1] = right_racket_y
    if tunnel_hit(prev_ball_bbox, ball_bbox, prev_racket_bbox, racket_bbox):
        strike(1)
        ball_center_y = ball_bbox[1] + {BALL_W // 2}
        racket_center_y = right_racket_y + {RACKET_H // 2}
        diff = ball_center_y - racket_center_y
        diff -= limit(diff, {-FLAT_ZONE}, {FLAT_ZONE})           
        y_power = min(right_power, {MAX_ANGLE})
        ball_vy = diff * {MAX_ANGLE}
        return 1
    return 0

def move_ball():
    ball_x += ball_vx
    ball_y += ball_vy
    ball_vz -= {GRAVITY}
    ball_z += ball_vz
    if ball_z < 0:
        old_vx = ball_vx
        old_vy = ball_vy
        ball_vx = shra(ball_vx * {TABLE_FRICTION}, {BITS})
        ball_vy = shra(ball_vy * {TABLE_FRICTION}, {BITS})
        if ball_vx == old_vx:
            ball_vx = 0
        if ball_vy == old_vy:
            ball_vy = 0
        ball_z = 0
        ball_vz = -shra(ball_vz * {TABLE_DAMPING}, {BITS})
        return 1
    return 0

def update_ball_bbox(bbox):
    bbox[0] = shra(ball_x, {BITS})
    bbox[1] = shra(ball_y, {BITS})

def draw_ball():
    x = shra(ball_x, {BITS})
    y = shra(ball_y, {BITS})
    z = shra(ball_z, {BITS + 1})
    poke({rect[BALL1_RECT].x}, x)
    poke({rect[BALL1_RECT].y}, y)
    poke({rect[BALL_SHADOW_RECT].x}, x + z)
    poke({rect[BALL_SHADOW_RECT].y}, y + z + 1)

def draw_rackets():
    poke({rect[LEFT_RACKET_RECT].x}, left_racket_x)
    poke({rect[LEFT_RACKET_RECT].y}, left_racket_y)
    poke({rect[RIGHT_RACKET_RECT].x}, right_racket_x)
    poke({rect[RIGHT_RACKET_RECT].y}, right_racket_y)

def draw_score():
    poke({rect[LEFT_DIGIT_RECT].x}, {SCREEN_W // 2 - LEFT_DIGIT[3] * 3})
    poke({rect[LEFT_DIGIT_RECT].y}, {LEFT_DIGIT[4]})
    poke({rect[RIGHT_DIGIT_RECT].x}, {SCREEN_W // 2 + RIGHT_DIGIT[3] * 2})
    poke({rect[RIGHT_DIGIT_RECT].y}, {RIGHT_DIGIT[4]})

def copy(src, dst, size):
    end = src + size
    while src < end:
        dst[0] = src[0]
        src += 1
        dst += 1

def set_swept_bbox(prev_bbox, current_bbox, new_bbox):
    px = prev_bbox[0]
    py = prev_bbox[1]
    pw = prev_bbox[2]
    ph = prev_bbox[3]
    cx = current_bbox[0]
    cy = current_bbox[1]
    cw = current_bbox[2]
    ch = current_bbox[3]    
    x = min(px, cx)
    y = min(py, cy)    
    new_bbox[0] = x
    new_bbox[1] = y
    new_bbox[2] = max(px + pw, cx + cw) - x
    new_bbox[3] = max(py + ph, cy + ch) - y
    
def tunnel_hit(prev_bbox, bbox, prev_wall_bbox, wall_bbox):
    set_swept_bbox(prev_bbox, bbox, swept_bbox1)
    set_swept_bbox(prev_wall_bbox, wall_bbox, swept_bbox2)
    return hit(swept_bbox1, swept_bbox2)
 
def hit(bbox1, bbox2):
    bbox1_x1 = bbox1[0]
    bbox1_y1 = bbox1[1]
    bbox2_x1 = bbox2[0]
    bbox2_y1 = bbox2[1]
    if bbox1_x1 + bbox1[2] < bbox2_x1:
        return 0
    if bbox1_x1 > bbox2_x1 + bbox2[2]:
        return 0
    if bbox1_y1 + bbox1[3] < bbox2_y1:
        return 0
    if bbox1_y1 > bbox2_y1 + bbox2[3]:
        return 0
    return 1

def limit(val, min_val, max_val):
    if val < min_val:
        return min_val
    if val > max_val:
        return max_val
    return val

def max(a, b):
    if a > b:
        return a
    return b

def min(a, b):
    if a < b:
        return a
    return b

play_rects = {PLAY_RECTS}
score_digits = {SCORE_DIGITS}
left_racket_vx = 0
left_racket_vy = 0
right_racket_vx = 0
right_racket_vy = 0
ball_x = 0
ball_y = 0
ball_z = 0
ball_vx = 0
ball_vy = 0
ball_vz = 0
table_bbox = {TABLE_BBOX}
net_bbox = {NET_BBOX}
ball_bbox = {BALL_BBOX}
racket_bbox = {RACKET_BBOX}
screen_bbox = {[0, 0, SCREEN_W, SCREEN_H]}
prev_ball_bbox = {PREV_BALL_BBOX}
prev_racket_bbox = {PREV_RACKET_BBOX}
swept_bbox1 = {[0] * 4}
swept_bbox2 = {[0] * 4}
left_racket_x = 0
left_racket_y = 0
right_racket_x = 0
right_racket_y = 0
prev_left_racket_x = 0
prev_left_racket_y = 0
prev_right_racket_x = 0
prev_right_racket_y = 0
left_power = 0
right_power = 0
ball_hit = 0
left_hit = 0
right_hit = 0
net_hit = 0
who_serve = 0
table_hit_count = 0
game_state = {SERVE}
timer_on = 0
timer = 0
left_score = 0
right_score = 0
''')
