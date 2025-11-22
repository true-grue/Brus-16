# Author: Vladimir Miklashevich
from brus16 import *


def next_id(id: int, data: list[int]):
    return id + len(data) // RECT_SIZE

COLORS = [
    rgb(0xffc0c0), rgb(0xff4040), rgb(0xa02020), rgb(0x402020),
    rgb(0xffe0c0), rgb(0xffa040), rgb(0xa06020), rgb(0x403020),
    rgb(0xffffc0), rgb(0xffff40), rgb(0xa0a020), rgb(0x404020),
    rgb(0xe0ffc0), rgb(0xa0ff40), rgb(0x60a020), rgb(0x304020),
    rgb(0xc0ffc0), rgb(0x40ff40), rgb(0x20a020), rgb(0x204020),
    rgb(0xc0ffe0), rgb(0x40ffa0), rgb(0x20a060), rgb(0x204030),
    rgb(0xc0ffff), rgb(0x40ffff), rgb(0x20a0a0), rgb(0x204040),
    rgb(0xc0e0ff), rgb(0x40a0ff), rgb(0x2060a0), rgb(0x203040),
    rgb(0xc0c0ff), rgb(0x4040ff), rgb(0x2020a0), rgb(0x202040),
    rgb(0xe0c0ff), rgb(0xa040ff), rgb(0x6020a0), rgb(0x302040),
    rgb(0xffc0ff), rgb(0xff40ff), rgb(0xa020a0), rgb(0x402040),
    rgb(0xffc0e0), rgb(0xff40a0), rgb(0xa02060), rgb(0x402030)
]

SKY = [1, 0, 0, SCREEN_W, SCREEN_H, rgb(0x000000)]

PLAYER_ID = next_id(0, SKY)
PLAYER_POS = [160, 200]
PLAYER_EYE_H = [5, 10]
PLAYER_JUMP = 4
PLAYER_ANIM_DUR = 6
PLAYER_ANIM_BUSY = 2
PLAYER_ANIM = [
    0, -10, 5, 25, 15, rgb(0x4040ff),
    0, -5, 5, 20, 20, rgb(0x4040ff),
    0, 0, 5, 15, 25, rgb(0x4040ff),
    0, -5, 5, 20, 20, rgb(0x4040ff)
] + [
    0, -10, 10, 25, 15, rgb(0x4040ff),
    0, -5, 5, 20, 20, rgb(0x4040ff),
    0, 0, 0, 15, 25, rgb(0x4040ff),
    0, -5, 5, 20, 20, rgb(0x4040ff)
]
PLAYER = [
    1, PLAYER_POS[0] + 5, 505, 20, 20, rgb(0xff40ff),
    1, PLAYER_POS[0], 500, 30, 30, rgb(0x40ff40),
    0, -10, 5, 10, 10, rgb(0x40ffff),
    0, 20, 5, 10, 5, rgb(0xffffff),
    0, 25, 5, 5, 5, rgb(0x000000),
    0, 30, 10, 10, 10, rgb(0xffff40),
    0, -10, 5, 25, 15, rgb(0x4040ff)
]
PLAYER_FLIPPED = [
    1, PLAYER_POS[0] + 5, 505, 20, 20, rgb(0xff40ff),
    1, PLAYER_POS[0], 500, 30, 30, rgb(0x40ff40),
    0, -10, 15, 10, 10, rgb(0x40ffff),
    0, 20, 20, 10, 5, rgb(0xffffff),
    0, 25, 20, 5, 5, rgb(0x000000),
    0, 30, 10, 10, 10, rgb(0xffff40),
    0, -10, 10, 25, 15, rgb(0x4040ff)
]

COLUMNS_ID = next_id(PLAYER_ID, PLAYER)
COLUMNS_INITIAL = 55
COLUMNS_OFFSET = SCREEN_W >> 2
COLUMNS_OFFSET_W = COLUMNS_OFFSET * 5
COLUMNS_PAUSE_Y = SCREEN_H + 5
COLUMNS_BORDERLINE = 60
COLUMNS_END = 30
COLUMNS_GAP = 100
COLUMNS_RANGE = SCREEN_H - COLUMNS_BORDERLINE * 2 - COLUMNS_GAP - COLUMNS_END * 2
COLUMNS_W = 60
COLUMNS_LIMIT = -COLUMNS_W << 1
COLUMNS_BASE = [
    1, COLUMNS_INITIAL, 0, 50, 60, rgb(0xa0ff40),
    0, 0, 220, 50, 260, rgb(0xa0ff40),
    0, -5, 60, 60, 30, rgb(0x60a020),
    0, -5, 190, 60, 30, rgb(0x60a020),
    0, 10, 0, 5, 55, rgb(0xe0ffc0),
    0, 10, 225, 5, 255, rgb(0xe0ffc0)
]
COLUMNS_ADD = [
    RECT_H,
    RECT_SIZE + RECT_Y,
    RECT_SIZE * 2 + RECT_Y,
    RECT_SIZE * 3 + RECT_Y,
    RECT_SIZE * 4 + RECT_H,
    RECT_SIZE * 5 + RECT_Y
]
COLUMNS_SUB = [
    RECT_SIZE + RECT_H,
    RECT_SIZE * 5 + RECT_H
]
COLUMNS_ID_ALL: list[int] = []
COLUMNS: list[int] = []
for i in range(0, 5):
    COLUMNS_ID_ALL.append(next_id(COLUMNS_ID, COLUMNS))
    COLUMNS += COLUMNS_BASE

PROGRESS_BAR_ID = next_id(COLUMNS_ID, COLUMNS)
PROGRESS_BAR_Y = [-50, 40]
PROGRESS_BAR_TIME = [600, 60]
PROGRESS_BAR = [
    1, 160, PROGRESS_BAR_Y[0], 320, 40, rgb(0xffffff),
    0, 10, 10, 0, 20, rgb(0x000000)
]

SCORE_ID = next_id(PROGRESS_BAR_ID, PROGRESS_BAR)
SCORE_POS = [40, 40, 20, 0]
SCORE_BASE = [1, 30, 30, 75, 45, rgb(0x000000)]
SCORE_DIGIT_SIZE = RECT_SIZE * 3
SCORE_DIGITS = [
    1, -20, -30, 15, 25, rgb(0x000000),
    0, 0, 0, 15, 25, rgb(0xffffff),
    0, 5, 5, 5, 15, rgb(0x000000),
    1, -20, -30, 15, 25, rgb(0xffffff),
    0, 0, 5, 5, 15, rgb(0x000000),
    0, 10, 0, 5, 20, rgb(0x000000),
    1, -20, -30, 15, 25, rgb(0xffffff),
    0, 0, 5, 10, 5, rgb(0x000000),
    0, 5, 15, 10, 5, rgb(0x000000),
    1, -20, -30, 15, 25, rgb(0xffffff),
    0, 0, 5, 10, 5, rgb(0x000000),
    0, 0, 15, 10, 5, rgb(0x000000),
    1, -20, -30, 15, 25, rgb(0xffffff),
    0, 5, 0, 5, 10, rgb(0x000000),
    0, 0, 15, 10, 10, rgb(0x000000),
    1, -20, -30, 15, 25, rgb(0xffffff),
    0, 5, 5, 10, 5, rgb(0x000000),
    0, 0, 15, 10, 5, rgb(0x000000),
    1, -20, -30, 15, 25, rgb(0xffffff),
    0, 5, 5, 10, 5, rgb(0x000000),
    0, 5, 15, 5, 5, rgb(0x000000),
    1, -20, -30, 15, 25, rgb(0xffffff),
    0, 5, 5, 5, 5, rgb(0x000000),
    0, 0, 10, 10, 15, rgb(0x000000),
    1, -20, -30, 15, 25, rgb(0xffffff),
    0, 5, 5, 5, 5, rgb(0x000000),
    0, 5, 15, 5, 5, rgb(0x000000),
    1, -20, -30, 15, 25, rgb(0xffffff),
    0, 5, 5, 5, 5, rgb(0x000000),
    0, 0, 15, 10, 5, rgb(0x000000)
]
SCORE_ID_ALL = [SCORE_ID + 1, SCORE_ID + 4, SCORE_ID + 7]
SCORE = SCORE_BASE + SCORE_DIGITS[0:SCORE_DIGIT_SIZE] * 3

START_ID = next_id(SCORE_ID, SCORE)
START_ANIM_DUR = 15
START_COLORS = [rgb(0x40ff40), rgb(0x4040ff)]
START = [
    1, 280, 200, 80, 80, START_COLORS[0],
    0, 20, 10, 20, 60, START_COLORS[1],
    0, 40, 20, 10, 40, START_COLORS[1],
    0, 50, 30, 10, 20, START_COLORS[1]
]

BONUS_ID = next_id(SCORE_ID, SCORE)
BONUS_OFFSET = 95
BONUS_LIMIT = -50 << 1
BONUS_BORDERLINE = 92
BONUS_RANGE = SCREEN_H - BONUS_BORDERLINE * 2 - 40
BONUS_COLORS = [
    0, 1,
    0, 1,
    0, 2,
    0, 1,
    0, 1,
    0, 2
]
BONUS_ANIM_POS = [-10, -10, -5, -15, -10, -10, -15, -5]
BONUS_ANIM_DUR = 15
BONUS_ANIM = [
    1, -95, -95, 40, 40, rgb(0x20a0a0),
    1, -90, -100, 30, 50, rgb(0x20a0a0),
    1, -95, -95, 40, 40, rgb(0x20a0a0),
    1, -100, -90, 50, 30, rgb(0x20a0a0)
]
BONUS_VARS = [
    1, -95, -95, 40, 40, rgb(0xa02020),
    1, -90, -90, 20, 5, rgb(0xff4040),
    0, 0, 5, 5, 5, rgb(0xff4040),
    0, 0, 15, 5, 5, rgb(0xff4040),
    1, -95, -95, 40, 40, rgb(0x20a020),
    1, -90, -90, 20, 5, rgb(0x40ff40),
    0, 10, 5, 5, 5, rgb(0x40ff40),
    0, 0, 15, 15, 5, rgb(0x40ff40),
    1, -95, -95, 40, 40, rgb(0x2020a0),
    1, -90, -90, 20, 20, rgb(0x2020a0),
    0, 5, 0, 10, 20, rgb(0x4040ff),
    0, 0, 5, 20, 10, rgb(0x4040ff),
    1, -95, -95, 40, 40, rgb(0xa0a020),
    1, -90, -90, 5, 20, rgb(0xffff40),
    0, 5, 0, 15, 5, rgb(0xffff40),
    0, 5, 10, 15, 5, rgb(0xffff40),
    1, -95, -95, 40, 40, rgb(0x20a0a0),
    1, -90, -90, 20, 20, rgb(0x40ffff),
    0, 10, 0, 5, 15, rgb(0x20a0a0),
    0, 5, 5, 5, 15, rgb(0x20a0a0),
    1, -95, -95, 40, 40, rgb(0xa020a0),
    1, -90, -90, 20, 20, rgb(0xa020a0),
    0, 0, 0, 20, 20, rgb(0xff40ff),
    0, 5, 5, 10, 10, rgb(0xa020a0)
]
BONUS = BONUS_VARS[(RECT_SIZE * 16):(RECT_SIZE * 20)]

RECTANGLES_ALL = SKY + PLAYER + COLUMNS + PROGRESS_BAR + SCORE

save_game('flippy.bin', f'''
def main():
    load_rect()
    while true:
        draw()
        wait()

def draw():
    read_input()
    if paused == 0:
        move_world(-world_speed)
        move_player()
        count_bonus(1)
        animate_world()

def load_rect():
    copy(rect_all, {RECT_MEM}, {len(RECTANGLES_ALL)})
    copy(rect_start, {rect[START_ID].addr}, {len(START)})
    poke({rect[0].color}, colors[((accent << 1) + 1) << 2])
    shift_column({COLUMNS_ID_ALL[0]}, col1, false)
    shift_column({COLUMNS_ID_ALL[1]}, col2, false)
    shift_column({COLUMNS_ID_ALL[2]}, col3, false)
    shift_column({COLUMNS_ID_ALL[3]}, col4, false)
    shift_column({COLUMNS_ID_ALL[4]}, col5, false)
    store_score()

def read_input():
    up = peek({KEY_MEM + KEY_UP})
    right = peek({KEY_MEM + KEY_RIGHT})
    if up:
        if playing & (key_up == false):
            if (anim_frame_player == -1) | (anim_frame_player >= {PLAYER_ANIM_BUSY}):
                player_motion = -(player_gravity * {PLAYER_JUMP})
                anim_player = 0
                anim_frame_player = 0
    if right:
        if (playing == false) & (key_right == false):
            playing = true
            if bonus_time >= 0:
                count_bonus(bonus_time)
            if paused:
                pause_resume()
            world_speed = 2
            move_world(({(COLUMNS_OFFSET << 2) + 10} << 1) - col_pos)
            shift_column({COLUMNS_ID_ALL[0]}, col1, false)
            shift_column({COLUMNS_ID_ALL[1]}, col2, false)
            shift_column({COLUMNS_ID_ALL[2]}, col3, false)
            shift_column({COLUMNS_ID_ALL[3]}, col4, false)
            shift_column({COLUMNS_ID_ALL[4]}, col5, false)
            col_next = {((COLUMNS_OFFSET << 2) + COLUMNS_W) << 1}
            col_next_id = col_id
            player_pos = {PLAYER_POS[0] << 1}
            shield_offset = 5
            copy(rect_player, {rect[PLAYER_ID].addr}, {len(PLAYER)})
            player_moving = true
            player_motion = 0
            anim_gravity = 0
            poke({rect[PLAYER_ID].x}, {PLAYER_POS[0] + 5})
            poke({rect[PLAYER_ID + 1].x}, {PLAYER_POS[0]})
            poke({rect[PLAYER_ID].y}, {PLAYER_POS[1] + 5})
            poke({rect[PLAYER_ID + 1].y}, {PLAYER_POS[1]})
            y = peek({rect[START_ID].y})
            poke({rect[START_ID].y}, y + {SCREEN_H})
            score1 = 0
            score2 = 0
            score3 = 0
            store_score()
            anim_start = 0
        elif key_right == false:
            pause_resume()
    key_up = up
    key_right = right

def move_world(delta):
    col_pos += delta
    col1 += delta
    col2 += delta
    col3 += delta
    col4 += delta
    col5 += delta
    if col1 < {COLUMNS_LIMIT}:
        col1 += ({COLUMNS_OFFSET_W} << 1)
        shift_column(col_id, col1, true)
        col_pos = col2
        col_id = {COLUMNS_ID_ALL[1]}
    if col2 < {COLUMNS_LIMIT}:
        col2 += ({COLUMNS_OFFSET_W} << 1)
        shift_column(col_id, col2, true)
        col_pos = col3
        col_id = {COLUMNS_ID_ALL[2]}
    if col3 < {COLUMNS_LIMIT}:
        col3 += ({COLUMNS_OFFSET_W} << 1)
        shift_column(col_id, col3, true)
        col_pos = col4
        col_id = {COLUMNS_ID_ALL[3]}
    if col4 < {COLUMNS_LIMIT}:
        col4 += ({COLUMNS_OFFSET_W} << 1)
        shift_column(col_id, col4, true)
        col_pos = col5
        col_id = {COLUMNS_ID_ALL[4]}
    if col5 < {COLUMNS_LIMIT}:
        col5 += ({COLUMNS_OFFSET_W} << 1)
        shift_column(col_id, col5, true)
        col_pos = col1
        col_id = {COLUMNS_ID_ALL[0]}
    poke({rect[COLUMNS_ID_ALL[0]].x}, shra(col1, 1))
    poke({rect[COLUMNS_ID_ALL[1]].x}, shra(col2, 1))
    poke({rect[COLUMNS_ID_ALL[2]].x}, shra(col3, 1))
    poke({rect[COLUMNS_ID_ALL[3]].x}, shra(col4, 1))
    poke({rect[COLUMNS_ID_ALL[4]].x}, shra(col5, 1))
    if player_moving == 0:
        player_pos += delta
        x = shra(player_pos, 1)
        poke({rect[PLAYER_ID].x}, x + shield_offset)
        poke({rect[PLAYER_ID + 1].x}, x)
    elif playing:
        col_next += delta
        if player_pos >= col_next:
            col_next += ({COLUMNS_OFFSET} << 1)
            if col_next_id == {COLUMNS_ID_ALL[0]}:
                col_next_id = {COLUMNS_ID_ALL[1]}
            elif col_next_id == {COLUMNS_ID_ALL[1]}:
                col_next_id = {COLUMNS_ID_ALL[2]}
            elif col_next_id == {COLUMNS_ID_ALL[2]}:
                col_next_id = {COLUMNS_ID_ALL[3]}
            elif col_next_id == {COLUMNS_ID_ALL[3]}:
                col_next_id = {COLUMNS_ID_ALL[4]}
            elif col_next_id == {COLUMNS_ID_ALL[4]}:
                col_next_id = {COLUMNS_ID_ALL[0]}
            count_score(1)
    if playing & (bonus_type >= 0) & (bonus_time < 0):
        bonus_pos += delta
        x = shra(bonus_pos, 1)
        poke({rect[BONUS_ID].x}, x + bonus_anim_pos[anim_frame_bonus << 1])
        poke({rect[BONUS_ID + 1].x}, x)
        if bonus_pos < {BONUS_LIMIT}:
            y = peek({rect[BONUS_ID].y})
            poke({rect[BONUS_ID].y}, y + {SCREEN_H})
            y = peek({rect[BONUS_ID + 1].y})
            poke({rect[BONUS_ID + 1].y}, y + {SCREEN_H})
            bonus_type = -1

def move_player():
    if player_moving:
        x1 = peek({rect[PLAYER_ID + 1].x})
        y1 = peek({rect[PLAYER_ID + 1].y})
        play = playing
        move = player_moving
        if (y1 + player_motion) <= 0:
            play = false
        elif (y1 + player_motion) >= player_ground:
            player_motion = player_ground - y1
            play = false
            player_moving = false
        poke({rect[PLAYER_ID + 1].y}, y1 + player_motion)
        y = peek({rect[PLAYER_ID].y})
        poke({rect[PLAYER_ID].y}, y + player_motion)
        x2 = x1 + peek({rect[PLAYER_ID + 1].w})
        y2 = y1 + peek({rect[PLAYER_ID + 1].h})
        if player_touch:
            if hit_box(x1, y1, x2, y2, col_next_id, col_next_id):
                play = false
                player_moving = false
            elif hit_box(x1, y1, x2, y2, col_next_id, col_next_id + 1):
                play = false
                player_moving = false
            elif hit_box(x1, y1, x2, y2, col_next_id, col_next_id + 2):
                play = false
                player_moving = false
            elif hit_box(x1, y1, x2, y2, col_next_id, col_next_id + 3):
                play = false
                player_moving = false
        if playing & (play == false):
            if player_revive & (score1 + score2 + score3 > 0):
                count_score(-1)
                player_moving = move
            else:
                playing = false
                anim_frame_player = -1
                poke({rect[PLAYER_ID + 4].x}, 20)
                poke({rect[PLAYER_ID + 4].w}, 10)
                copy(rect_start, {rect[START_ID].addr}, {len(START)})
                if bonus_time < 0:
                    bonus_type = -1
        elif hit_box(x1, y1, x2, y2, {BONUS_ID}, {BONUS_ID}):
            y = peek({rect[BONUS_ID].y})
            poke({rect[BONUS_ID].y}, y + {SCREEN_H})
            y = peek({rect[BONUS_ID + 1].y})
            poke({rect[BONUS_ID + 1].y}, y + {SCREEN_H})
            touch_bonus()

def count_bonus(time):
    if bonus_time > 0:
        bonus_time -= time
        color_time -= time
        if bonus_time > 0:
            poke({rect[PROGRESS_BAR_ID + 1].w}, bonus_time >> 1)
            if (bonus_type == 2) & (color_time <= 0):
                color_time = {PROGRESS_BAR_TIME[1]}
                paint_world(-1, -1)
        else:
            bonus_time = -1
            poke({rect[PROGRESS_BAR_ID].y}, {PROGRESS_BAR_Y[0]})
            if bonus_type == 0:
                world_speed = 2
            elif bonus_type == 1:
                world_speed = 2
            elif bonus_type == 2:
                color_time = -1
                paint_world(-1, -1)
            elif bonus_type == 3:
                player_revive = false
                poke({rect[PLAYER_ID + 3].h}, {PLAYER_EYE_H[0]})
                poke({rect[PLAYER_ID + 4].h}, {PLAYER_EYE_H[0]})
            elif bonus_type == 4:
                player_gravity = 1
                x = peek({rect[PLAYER_ID + 1].x})
                y = peek({rect[PLAYER_ID + 1].y})
                shield_x = peek({rect[PLAYER_ID].x})
                shield_y = peek({rect[PLAYER_ID].y})
                eye_x = peek({rect[PLAYER_ID + 4].x})
                eye_w = peek({rect[PLAYER_ID + 4].w})
                copy(rect_player, {rect[PLAYER_ID].addr}, {len(PLAYER)})
                poke({rect[PLAYER_ID + 1].x}, x)
                poke({rect[PLAYER_ID + 1].y}, y)
                poke({rect[PLAYER_ID].x}, shield_x)
                poke({rect[PLAYER_ID].y}, shield_y)
                poke({rect[PLAYER_ID + 4].x}, eye_x)
                poke({rect[PLAYER_ID + 4].w}, eye_w)
            elif bonus_type == 5:
                player_touch = true
                shield_offset = 5
                x = peek({rect[PLAYER_ID].x})
                poke({rect[PLAYER_ID].x}, x + 20)
                y = peek({rect[PLAYER_ID].y})
                poke({rect[PLAYER_ID].y}, y + 20)
                w = peek({rect[PLAYER_ID].w})
                poke({rect[PLAYER_ID].w}, w - 40)
                h = peek({rect[PLAYER_ID].h})
                poke({rect[PLAYER_ID].h}, h - 40)
            bonus_type = -1

def animate_world():
    not_paused = (paused == false)
    if playing & not_paused & (anim_frame_player >= 0):
        anim_player += 1
        if anim_player >= {PLAYER_ANIM_DUR}:
            anim_player = 0
            anim_frame_player += 1
            anim_addr = rect_player_anim
            if anim_frame_player >= {(len(PLAYER_ANIM) >> 1) // RECT_SIZE}:
                anim_frame_player = -1
                anim_addr += ((1 - player_gravity) << 1) * {RECT_SIZE}
            else:
                anim_addr += (((1 - player_gravity) << 1) + anim_frame_player) * {RECT_SIZE}
            copy(anim_addr, {rect[PLAYER_ID + 6].addr}, {RECT_SIZE})
    if not_paused & player_moving:
        anim_gravity += 1
        if anim_gravity >= {PLAYER_ANIM_DUR >> 1}:
            anim_gravity = 0
            player_motion += player_gravity
    if playing == false:
        anim_start += 1
        if anim_start >= {START_ANIM_DUR}:
            anim_start = 0
            color1 = peek({rect[START_ID].color})
            color2 = peek({rect[START_ID + 1].color})
            poke({rect[START_ID].color}, color2)
            poke({rect[START_ID + 1].color}, color1)
            poke({rect[START_ID + 2].color}, color1)
            poke({rect[START_ID + 3].color}, color1)
    elif not_paused & (bonus_type >= 0):
        anim_bonus += 1
        if anim_bonus >= {BONUS_ANIM_DUR}:
            anim_bonus = 0
            anim_frame_bonus += 1
            if anim_frame_bonus >= {len(BONUS_ANIM) // RECT_SIZE}:
                anim_frame_bonus = 0
            anim_addr = rect_bonus_anim + anim_frame_bonus * {RECT_SIZE}
            color = peek({rect[BONUS_ID].color})
            copy(anim_addr, {rect[BONUS_ID].addr}, {RECT_SIZE})
            x = peek({rect[BONUS_ID + 1].x})
            x += bonus_anim_pos[anim_frame_bonus << 1]
            y = peek({rect[BONUS_ID + 1].y})
            y += bonus_anim_pos[(anim_frame_bonus << 1) + 1]
            poke({rect[BONUS_ID].x}, x)
            poke({rect[BONUS_ID].y}, y)
            poke({rect[BONUS_ID].color}, color)

def pause_resume():
    paused ^= true
    y = peek({rect[COLUMNS_ID_ALL[0]].y})
    poke({rect[COLUMNS_ID_ALL[0]].y}, {COLUMNS_PAUSE_Y} - y)
    y = peek({rect[COLUMNS_ID_ALL[1]].y})
    poke({rect[COLUMNS_ID_ALL[1]].y}, {COLUMNS_PAUSE_Y} - y)
    y = peek({rect[COLUMNS_ID_ALL[2]].y})
    poke({rect[COLUMNS_ID_ALL[2]].y}, {COLUMNS_PAUSE_Y} - y)
    y = peek({rect[COLUMNS_ID_ALL[3]].y})
    poke({rect[COLUMNS_ID_ALL[3]].y}, {COLUMNS_PAUSE_Y} - y)
    y = peek({rect[COLUMNS_ID_ALL[4]].y})
    poke({rect[COLUMNS_ID_ALL[4]].y}, {COLUMNS_PAUSE_Y} - y)

def shift_column(id, pos, bonus):
    ra = rect_addr(id)
    copy(rect_column, ra, {len(COLUMNS_BASE)})
    r = rnd_sized(8)
    offset = ((r & 31) + (r >> 5)) * 5
    i = 0
    while i < {len(COLUMNS_ADD)}:
        j = peek(ra + columns_add[i])
        poke(ra + columns_add[i], j + offset)
        i += 1
    i = 0
    while i < {len(COLUMNS_SUB)}:
        j = peek(ra + columns_sub[i])
        poke(ra + columns_sub[i], j - offset)
        i += 1
    poke(ra + {RECT_X}, shra(pos, 1))
    paint_column(id)
    if playing & bonus & (bonus_type < 0) & (rnd_sized(8) < (3 << 4)):
        bonus_type = rnd_sized(3)
        if bonus_type >= 6:
            bonus_type -= 6
        var_addr = rect_bonus_vars + (bonus_type << 2) * {RECT_SIZE}
        copy(var_addr, {rect[BONUS_ID].addr}, {len(BONUS)})
        bonus_pos = pos + ({BONUS_OFFSET} << 1)
        x = shra(bonus_pos, 1)
        y = {BONUS_BORDERLINE} + rnd_sized(6) * 5
        poke({rect[BONUS_ID].x}, x + bonus_anim_pos[0])
        poke({rect[BONUS_ID].y}, y + bonus_anim_pos[1])
        poke({rect[BONUS_ID + 1].x}, x)
        poke({rect[BONUS_ID + 1].y}, y)
        anim_bonus = 0
        anim_frame_bonus = 0

def count_score(delta):
    score1 += delta
    d2 = 0
    while score1 < 0:
        score1 += 10
        d2 -= 1
    while score1 >= 10:
        score1 -= 10
        d2 += 1
    score2 += d2
    d3 = 0
    while score2 < 0:
        score2 += 10
        d3 -= 1
    while score2 >= 10:
        score2 -= 10
        d3 += 1
    score3 += d3
    if score3 < 0:
        score1 = 0
        score2 = 0
        score3 = 0
        return false
    elif score3 >= 10:
        while score3 >= 10:
            score3 -= 10
        paint_world(1, false)
    store_score()
    return true

def store_score():
    addr1 = rect_digits + score1 * {SCORE_DIGIT_SIZE}
    copy(addr1, {rect[SCORE_ID_ALL[2]].addr}, {SCORE_DIGIT_SIZE})
    addr2 = rect_digits + score2 * {SCORE_DIGIT_SIZE}
    copy(addr2, {rect[SCORE_ID_ALL[1]].addr}, {SCORE_DIGIT_SIZE})
    addr3 = rect_digits + score3 * {SCORE_DIGIT_SIZE}
    copy(addr3, {rect[SCORE_ID_ALL[0]].addr}, {SCORE_DIGIT_SIZE})
    poke({rect[SCORE_ID_ALL[0]].x}, {SCORE_POS[0]})
    poke({rect[SCORE_ID_ALL[0]].y}, {SCORE_POS[1]})
    poke({rect[SCORE_ID_ALL[1]].x}, {SCORE_POS[0] + SCORE_POS[2]})
    poke({rect[SCORE_ID_ALL[1]].y}, {SCORE_POS[1] + SCORE_POS[3]})
    poke({rect[SCORE_ID_ALL[2]].x}, {SCORE_POS[0] + (SCORE_POS[2] << 1)})
    poke({rect[SCORE_ID_ALL[2]].y}, {SCORE_POS[1] + (SCORE_POS[3] << 1)})

def touch_bonus():
    bonus_index = bonus_type << 1
    bonus_color1 = peek(rect_addr({BONUS_ID} + bonus_colors[bonus_index]) + {RECT_COLOR})
    bonus_color2 = peek(rect_addr({BONUS_ID} + bonus_colors[bonus_index + 1]) + {RECT_COLOR})
    poke({rect[PROGRESS_BAR_ID].color}, bonus_color1)
    poke({rect[PROGRESS_BAR_ID + 1].color}, bonus_color2)
    bonus_time = {PROGRESS_BAR_TIME[0]}
    poke({rect[PROGRESS_BAR_ID + 1].w}, bonus_time)
    poke({rect[PROGRESS_BAR_ID].y}, {PROGRESS_BAR_Y[1]})
    if bonus_type == 0:
        world_speed = 1
    elif bonus_type == 1:
        world_speed = 4
    elif bonus_type == 2:
        color_time = {PROGRESS_BAR_TIME[1]}
        paint_world(-1, -1)
    elif bonus_type == 3:
        player_revive = true
        poke({rect[PLAYER_ID + 3].h}, {PLAYER_EYE_H[1]})
        poke({rect[PLAYER_ID + 4].h}, {PLAYER_EYE_H[1]})
    elif bonus_type == 4:
        player_gravity = -1
        x = peek({rect[PLAYER_ID + 1].x})
        y = peek({rect[PLAYER_ID + 1].y})
        shield_x = peek({rect[PLAYER_ID].x})
        shield_y = peek({rect[PLAYER_ID].y})
        copy(rect_player_flipped, {rect[PLAYER_ID].addr}, {len(PLAYER_FLIPPED)})
        poke({rect[PLAYER_ID + 1].x}, x)
        poke({rect[PLAYER_ID + 1].y}, y)
        poke({rect[PLAYER_ID].x}, shield_x)
        poke({rect[PLAYER_ID].y}, shield_y)
    elif bonus_type == 5:
        player_touch = false
        shield_offset = -15
        x = peek({rect[PLAYER_ID].x})
        poke({rect[PLAYER_ID].x}, x - 20)
        y = peek({rect[PLAYER_ID].y})
        poke({rect[PLAYER_ID].y}, y - 20)
        w = peek({rect[PLAYER_ID].w})
        poke({rect[PLAYER_ID].w}, w + 40)
        h = peek({rect[PLAYER_ID].h})
        poke({rect[PLAYER_ID].h}, h + 40)

def paint_world(a, d):
    dark = d
    if a < 0:
        a1 = accent
        a2 = accent
        if accent >= 3:
            a1 -= 3
        else:
            a2 += 3
        r = rnd_sized(3)
        a = r & 3
        dark = r >> 2
        if a >= a1:
            a += 1
        if a >= a2:
            a += 1
    accent = a
    poke({rect[0].color}, colors[((accent << 1) + 1 << 2) + dark * 3])
    paint_column({COLUMNS_ID_ALL[0]})
    paint_column({COLUMNS_ID_ALL[1]})
    paint_column({COLUMNS_ID_ALL[2]})
    paint_column({COLUMNS_ID_ALL[3]})
    paint_column({COLUMNS_ID_ALL[4]})

def paint_column(id):
    palette = (accent << 1) + 1 << 2
    poke(rect_addr(id) + {RECT_COLOR}, colors[palette + 1])
    poke(rect_addr(id + 1) + {RECT_COLOR}, colors[palette + 1])
    poke(rect_addr(id + 2) + {RECT_COLOR}, colors[palette + 2])
    poke(rect_addr(id + 3) + {RECT_COLOR}, colors[palette + 2])
    poke(rect_addr(id + 4) + {RECT_COLOR}, colors[palette])
    poke(rect_addr(id + 5) + {RECT_COLOR}, colors[palette])

def hit_box(x1, y1, x2, y2, base, extra):
    ba = rect_addr(base)
    bx1 = peek(ba + {RECT_X})
    by1 = peek(ba + {RECT_Y})
    bx2 = bx1
    by2 = by1
    if extra != base:
        ea = rect_addr(extra)
        bx1 += peek(ea + {RECT_X})
        by1 += peek(ea + {RECT_Y})
        bx2 = bx1 + peek(ea + {RECT_W})
        by2 = by1 + peek(ea + {RECT_H})
    else:
        bx2 += peek(ba + {RECT_W})
        by2 += peek(ba + {RECT_H})
    if x2 < bx1:
        return false
    if x1 > bx2:
        return false
    if y2 < by1:
        return false
    if y1 > by2:
        return false
    return true

def copy(src, dst, size):
    end = src + size
    while src < end:
        dst[0] = src[0]
        src += 1
        dst += 1

def rect_addr(i):
    return {RECT_MEM} + i * {RECT_SIZE}

def rnd_sized(len):
    return rnd() & ((1 << len) - 1)

def rnd():
    rnd_seed ^= rnd_seed << 7
    rnd_seed ^= rnd_seed >> 9
    rnd_seed ^= rnd_seed << 8
    return rnd_seed

# Generic
rnd_seed = 1
false = 0
true = 1

# Common
playing = 0 # false
paused = 0 # false
accent = 1 # true

# Keys
key_up = -1
key_right = -1

# Positions
world_speed = 2
player_pos = {PLAYER_POS[0] << 1}
shield_offset = 5
col_id = {COLUMNS_ID_ALL[0]}
col_pos = {COLUMNS_INITIAL << 1}
col1 = {COLUMNS_INITIAL << 1}
col2 = {(COLUMNS_INITIAL + COLUMNS_OFFSET) << 1}
col3 = {(COLUMNS_INITIAL + COLUMNS_OFFSET * 2) << 1}
col4 = {(COLUMNS_INITIAL + COLUMNS_OFFSET * 3) << 1}
col5 = {(COLUMNS_INITIAL + COLUMNS_OFFSET * 4) << 1}
col_next = {((COLUMNS_OFFSET << 2) + COLUMNS_W) << 1}
col_next_id = {COLUMNS_ID_ALL[0]}
bonus_pos = 0

# Player
player_revive = 0 # false
player_moving = 0 # false
player_motion = 0
player_gravity = 1
player_touch = 1 # true
player_ground = {SCREEN_H - 30}

# Bonuses
bonus_type = -1
bonus_time = -1
color_time = -1

# Score
score1 = 0
score2 = 0
score3 = 0

# Animations
anim_player = 0
anim_frame_player = -1
anim_gravity = 0
anim_start = 0
anim_bonus = -1
anim_frame_bonus = -1

# Arrays
colors = {COLORS}
bonus_colors = {BONUS_COLORS}
bonus_anim_pos = {BONUS_ANIM_POS}
columns_add = {COLUMNS_ADD}
columns_sub = {COLUMNS_SUB}
rect_all = {RECTANGLES_ALL}
rect_player = {PLAYER}
rect_player_flipped = {PLAYER_FLIPPED}
rect_player_anim = {PLAYER_ANIM}
rect_start = {START}
rect_column = {COLUMNS_BASE}
rect_digits = {SCORE_DIGITS}
rect_bonus_vars = {BONUS_VARS}
rect_bonus_anim = {BONUS_ANIM}
''')
