# Author: Vladimir Miklashevich
from brus16 import *


def next_id(id: int, data: list[int]):
    return id + len(data) // RECT_SIZE

COLORS_S = [
    '#b0b0b0', '#ffffff', '#707070','#303030',
    '#808080', '#a0a0a0', '#404040','#202020',
    '#f8b060', '#f86030', '#704828','#702818',
    '#f86030', '#f8b060', '#702818','#704828',
    '#ffc0c0', '#ff4040', '#a02020','#402020',
    '#ffe0c0', '#ffa040', '#a06020','#403020',
    '#ffffc0', '#ffff40', '#a0a020','#404020',
    '#e0ffc0', '#a0ff40', '#60a020','#304020',
    '#c0ffc0', '#40ff40', '#20a020','#204020',
    '#c0ffe0', '#40ffa0', '#20a060','#204030',
    '#c0ffff', '#40ffff', '#20a0a0','#204040',
    '#c0e0ff', '#40a0ff', '#2060a0','#203040',
    '#c0c0ff', '#4040ff', '#2020a0','#202040',
    '#e0c0ff', '#a040ff', '#6020a0','#302040',
    '#ffc0ff', '#ff40ff', '#a020a0','#402040',
    '#ffc0e0', '#ff40a0', '#a02060','#402030'
]
COLORS = [
    rgb(0xb0b0b0), rgb(0xffffff), rgb(0x707070), rgb(0x303030),
    rgb(0x808080), rgb(0xa0a0a0), rgb(0x404040), rgb(0x202020),
    rgb(0xf8b060), rgb(0xf86030), rgb(0x704828), rgb(0x702818),
    rgb(0xf86030), rgb(0xf8b060), rgb(0x702818), rgb(0x704828),
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

FIELD_ID = next_id(0, [])
FIELD = [
    1, 80, 0, 240, 480, rgb(0x303030),
    1, 320, 0, 240, 480, rgb(0x303030)
]
BALL_ID = next_id(FIELD_ID, FIELD)
BALL_SIZE = 20
BALL_POS = [(SCREEN_W - BALL_SIZE) // 2, (SCREEN_H - BALL_SIZE) // 2]
BALL = [
    1, BALL_POS[0], BALL_POS[1], 10, 20, rgb(0xffffff),
    1, BALL_POS[0] + 10, BALL_POS[1], 10, 20, rgb(0xffffff)
]
BOARD_H = 80
BOARD1_ID = next_id(BALL_ID, BALL)
BOARD1 = [
    1, 51, 200, 8, 80, rgb(0xb0b0b0),
    0, -1, 5, 10, 70, rgb(0xffffff)
]
BOARD2_ID = next_id(BOARD1_ID, BOARD1)
BOARD2 = [
    1, 581, 200, 8, 80, rgb(0xb0b0b0),
    0, -1, 5, 10, 70, rgb(0xffffff)
]
BOARD_ID_ALL = [BOARD1_ID, BOARD2_ID]

CURSOR_SIZE = 8
CURSOR_GAP = 6
CURSOR_MAX_OFFSET = 400
CURSOR_ANIM_DUR = 15
CURSOR_ANIM_OFFSET = 2
CURSOR_V = [
    1, 51, 186, 8, 8, rgb(0xffffff),
    0, 0, 100, 8, 8, rgb(0xffffff)
]
CURSOR_H = [
    1, 51, 186, 8, 8, rgb(0xffffff),
    0, 100, 0, 8, 8, rgb(0xffffff)
]
CURSOR1_ID = next_id(BOARD2_ID, BOARD2)
CURSOR2_ID = next_id(CURSOR1_ID, CURSOR_V)
CURSOR_ID_ALL = [CURSOR1_ID, CURSOR2_ID]
CURSOR1_POS_REF = [
    BOARD1_ID, 0,
    FIELD_ID, 0,
    BALL_ID, 0
]
CURSOR2_POS_REF = [
    BOARD2_ID, 0,
    FIELD_ID + 1, 0,
    BALL_ID + 1, 0
]

SCORE_DIGIT_COUNT = 3
SCORE_DIGIT_SIZE = RECT_SIZE * 3
SCORE_DIGITS = [
    1, -20, -40, 16, 32, 0,
    0, 4, 4, 8, 24, 65535,
    0, 0, 0, 0, 0, 0,
    1, -20, -40, 6, 4, 0,
    0, 6, 0, 4, 28, 0,
    0, 0, 28, 16, 4, 0,
    1, -20, -40, 16, 32, 0,
    0, 0, 4, 12, 10, 65535,
    0, 4, 18, 12, 10, 65535,
    1, -20, -40, 16, 32, 0,
    0, 0, 4, 12, 10, 65535,
    0, 0, 18, 12, 10, 65535,
    1, -20, -40, 4, 18, 0,
    0, 4, 14, 12, 4, 0,
    0, 12, 0, 4, 32, 0,
    1, -20, -40, 16, 32, 0,
    0, 4, 4, 12, 10, 65535,
    0, 0, 18, 12, 10, 65535,
    1, -20, -40, 16, 32, 0,
    0, 4, 4, 12, 10, 65535,
    0, 4, 18, 8, 10, 65535,
    1, -20, -40, 4, 12, 0,
    0, 4, 0, 8, 4, 0,
    0, 12, 0, 4, 32, 0,
    1, -20, -40, 16, 32, 0,
    0, 4, 4, 8, 10, 65535,
    0, 4, 18, 8, 10, 65535,
    1, -20, -40, 16, 32, 0,
    0, 4, 4, 8, 10, 65535,
    0, 0, 18, 12, 10, 65535
]
SCORE1_ID = next_id(CURSOR2_ID, CURSOR_V)
SCORE1_ID_ALL = [SCORE1_ID, SCORE1_ID + 1, SCORE1_ID + 4, SCORE1_ID + 7]
SCORE1 = [
    1, 220, 20, 80, 50, 65535,
    1, 230, 29, 16, 32, 0,
    0, 4, 4, 8, 24, 65535,
    0, 0, 0, 0, 0, 0,
    1, 252, 29, 16, 32, 0,
    0, 4, 4, 8, 24, 65535,
    0, 0, 0, 0, 0, 0,
    1, 274, 29, 16, 32, 0,
    0, 4, 4, 8, 24, 65535,
    0, 0, 0, 0, 0, 0
]
SCORE1_BASE = SCORE1[:RECT_SIZE]
SCORE1_POS = [
    SCORE1[RECT_X], SCORE1[RECT_Y],
    SCORE1[RECT_SIZE + RECT_X], SCORE1[RECT_SIZE + RECT_Y],
    SCORE1[4 * RECT_SIZE + RECT_X], SCORE1[4 * RECT_SIZE + RECT_Y],
    SCORE1[7 * RECT_SIZE + RECT_X], SCORE1[7 * RECT_SIZE + RECT_Y]
]
SCORE2_ID = next_id(SCORE1_ID, SCORE1)
SCORE2_ID_ALL = [SCORE2_ID, SCORE2_ID + 1, SCORE2_ID + 4, SCORE2_ID + 7]
SCORE2 = [
    1, 340, 20, 80, 50, 65535,
    1, 350, 29, 16, 32, 0,
    0, 4, 4, 8, 24, 65535,
    0, 0, 0, 0, 0, 0,
    1, 372, 29, 16, 32, 0,
    0, 4, 4, 8, 24, 65535,
    0, 0, 0, 0, 0, 0,
    1, 394, 29, 16, 32, 0,
    0, 4, 4, 8, 24, 65535,
    0, 0, 0, 0, 0, 0
]
SCORE2_BASE = SCORE2[:RECT_SIZE]
SCORE2_POS = [
    SCORE2[RECT_X], SCORE2[RECT_Y],
    SCORE2[RECT_SIZE + RECT_X], SCORE2[RECT_SIZE + RECT_Y],
    SCORE2[4 * RECT_SIZE + RECT_X], SCORE2[4 * RECT_SIZE + RECT_Y],
    SCORE2[7 * RECT_SIZE + RECT_X], SCORE2[7 * RECT_SIZE + RECT_Y]
]
SCORE_ID_ALL = [SCORE1_ID, SCORE2_ID]

SCORE_TIME = 60
RESTART_TIME = [120, 600]
RESET_TIME = 15

COLOR_TARGETS = [
    0, 2,
    2, 1,
    3, 1
]
COLOR1_INDEX = [
    BOARD1_ID, 0, BOARD1_ID + 1, 1,
    FIELD_ID, 3,
    BALL_ID, 1
]
COLOR2_INDEX = [
    BOARD2_ID, 0, BOARD2_ID + 1, 1,
    FIELD_ID + 1, 3,
    BALL_ID + 1, 1
]

RECTANGLES_ALL = FIELD + BALL + BOARD1 + BOARD2 + CURSOR_V * 2 + SCORE1 + SCORE2

main = f'''
def main():
    setup()
    while true:
        draw()
        wait()

def setup():
    copy(rect_all, {RECT_MEM}, {len(RECTANGLES_ALL)})

def draw():
    read_input()
    if playing:
        move_ball()
    animate()
'''
keys = f'''
def read_input():
    if input_active():
        if playing:
            read_input_main()
        else:
            read_input_menu()

def input_active():
    return anim_reset < 0

def read_input_main():
    a_a2 = peek({KEY_MEM + KEY_A}) & peek({KEY_MEM + KEY_A2})
    if pressed2(a_a2, key_a_a2) & (anim_restart < 0):
        playing = false
        reset_ball()
        cache_keys()
        cursor_offsets[0] = 0
        cursor_offsets[1] = 0
        move_cursor(0, cursors[0])
        move_cursor(1, cursors[1])
    else:
        i = 0
        while i < 2:
            addr = rect_addr(player_id_all[i]) + {RECT_Y}
            offset = i * {KEY_NUM // 2}
            y = peek(addr)
            if peek({KEY_MEM + KEY_UP} + offset):
                y -= player_speed
                if y < 0:
                    y = 0
            if peek({KEY_MEM + KEY_DOWN} + offset):
                y += player_speed
                if y > {SCREEN_H - BOARD_H}:
                    y = {SCREEN_H - BOARD_H}
            poke(addr, y)
            i += 1
        key_a_a2 = a_a2

def read_input_menu():
    i = 0
    while i < 2:
        co = cursor_offsets[i]
        cos = co != 0
        if peek({KEY_MEM + KEY_A} + i * {KEY_NUM // 2}):
            co = cursor_hide_offset
        else:
            co = cursor_show_offset
        if (co != cursor_offsets[i]) & (cos | (co == cursor_show_offset)):
            if cos:
                addr = rect_addr(cursor_id_all[i]) + {RECT_Y}
                poke(addr, peek(addr) + co)
            cursor_offsets[i] = co
        i += 1
    if pressed2(peek({KEY_MEM + KEY_A}) & peek({KEY_MEM + KEY_A2}), key_a_a2):
        i = 0
        while i < 2:
            if cursor_offsets[i] == 0:
                cursor_offsets[i] = cursor_hide_offset
                addr = rect_addr(cursor_id_all[i]) + {RECT_Y}
                poke(addr, peek(addr) + cursor_hide_offset)
            i += 1
        playing = true
    else:
        i = 0
        while i < 2:
            offset = i * {KEY_NUM // 2}
            cursor = cursors[i]
            if cursor < cursor_min:
                cursor = cursor_min
            elif cursor > cursor_max:
                cursor = cursor_max
            if pressed({KEY_LEFT} + offset):
                cursor -= 1
                if cursor < cursor_min:
                    cursor = cursor_max
            if pressed({KEY_RIGHT} + offset):
                cursor += 1
                if cursor > cursor_max:
                    cursor = cursor_min
            if cursor != cursors[i]:
                move_cursor(i, cursor)
            else:
                handle_cursor(i, cursor)
            cursors[i] = cursor
            i += 1
    cache_keys()

def cache_keys():
    copy({KEY_MEM}, key_cache, {KEY_NUM})
    key_a_a2 = key_cache[{KEY_A}] & key_cache[{KEY_A2}]

def pressed(key):
    return pressed2(peek({KEY_MEM} + key), key_cache[key])

def pressed2(state, cache):
    return state & (cache == false)
'''
menu = f'''
def move_cursor(player, cursor):
    i = (cursor << 1) + player * {len(CURSOR1_POS_REF)}
    addr_s = rect_addr(cursor_pos_ref[i])
    tx = peek(addr_s + {RECT_X})
    ty = peek(addr_s + {RECT_Y})
    tw = peek(addr_s + {RECT_W})
    th = peek(addr_s + {RECT_H})
    tw2 = tw
    if tw2 > {CURSOR_MAX_OFFSET}:
        tw2 = {CURSOR_MAX_OFFSET}
    th2 = th
    if th2 > {CURSOR_MAX_OFFSET}:
        th2 = {CURSOR_MAX_OFFSET}
    addr_f = {rect[CURSOR1_ID].addr} + player * {len(CURSOR_V)}
    rot = cursor_pos_ref[i + 1]
    if rot == 0:
        y = ty + ((th - th2) >> 1) - {CURSOR_SIZE} - {CURSOR_GAP}
        if cursor_offsets[player] == cursor_hide_offset:
            y += cursor_hide_offset
        poke(addr_f + {RECT_X}, tx + ((tw - {CURSOR_SIZE}) >> 1))
        poke(addr_f + {RECT_Y}, y)
        poke(addr_f + {RECT_SIZE + RECT_Y}, th2 + {CURSOR_SIZE} + ({CURSOR_GAP} << 1))
    elif rot == 1:
        y = ty + ((th - {CURSOR_SIZE}) >> 1)
        if cursor_offsets[player] == cursor_hide_offset:
            y += cursor_hide_offset
        poke(addr_f + {RECT_X}, tx + ((tw - tw2) >> 1) - {CURSOR_SIZE} - {CURSOR_GAP})
        poke(addr_f + {RECT_Y}, y)
        poke(addr_f + {RECT_SIZE + RECT_X}, tw2 + {CURSOR_SIZE} + ({CURSOR_GAP} << 1))
    anim_cursor[player] = 0
    anim_cursor_frame[player] = 0

def handle_cursor(player, cursor):
    f = cursor + player * 3
    c = player_colors[f]
    offset = player * {KEY_NUM // 2}
    if pressed({KEY_UP} + offset):
        c += 1
        if c >= {len(COLORS) // 4}:
            c = 0
    if pressed({KEY_DOWN} + offset):
        c -= 1
        if c < 0:
            c = {len(COLORS) // 4} - 1
    if player_colors[f] != c:
        player_colors[f] = c
        n = (cursor << 1) + player * {len(COLOR_TARGETS)}
        i = 0
        while i < color_targets[n + 1]:
            j = ((color_targets[n] + i) << 1) + player * {len(COLOR1_INDEX)}
            addr = rect_addr(color_index[j]) + {RECT_COLOR}
            poke(addr, colors[(c << 2) + color_index[j + 1]])
            i += 1
'''
physics = f'''
def move_ball():
    x1 = peek({rect[BALL_ID].x}) + ball_dx
    y1 = peek({rect[BALL_ID].y}) + ball_dy
    side = -1
    if x1 <= 0:
        side = 1
    elif x1 >= {SCREEN_W - BALL[RECT_W]}:
        side = 0
    if (side != -1) & (anim_restart == -1):
        starter = side
        if count_score(side, 1):
            anim_restart = {RESTART_TIME[1]}
            anim_reset = {RESET_TIME}
        else:
            anim_score[side] = {SCORE_TIME}
            anim_restart = {RESTART_TIME[0]}
    if y1 < 0:
        y1 = -y1
        ball_dy = -ball_dy
    elif y1 > {SCREEN_H - BALL[RECT_H]}:
        y1 -= (y1 - {SCREEN_H - BALL[RECT_H]}) << 1
        ball_dy = -ball_dy
    poke({rect[BALL_ID].x}, x1)
    poke({rect[BALL_ID].y}, y1)
    poke({rect[BALL_ID + 1].x}, x1 + 10)
    poke({rect[BALL_ID + 1].y}, y1)
    x2 = x1 + {BALL_SIZE}
    y2 = y1 + {BALL_SIZE}
    dy1 = y1 - peek({rect[BOARD1_ID].y})
    dy2 = y1 - peek({rect[BOARD2_ID].y})
    sx = 0
    dy = 0
    if hit_box(x1, y1, x2, y2, {BOARD1_ID}, {BOARD1_ID + 1}):
        sx = 1
        dy = dy1
    elif hit_box(x1, y1, x2, y2, {BOARD1_ID}, {BOARD1_ID}):
        ball_dx = 1
        ball_dy = 5 * sign(dy1 >= 0)
    elif hit_box(x1, y1, x2, y2, {BOARD2_ID}, {BOARD2_ID + 1}):
        sx = -1
        dy = dy2
    elif hit_box(x1, y1, x2, y2, {BOARD2_ID}, {BOARD2_ID}):
        ball_dx = -1
        ball_dy = 5 * sign(dy2 >= 0)
    if sx != 0:
        if dy > 60:
            ball_dx = 2 * sx
            ball_dy = 5
        elif dy > 50:
            ball_dx = 4 * sx
            ball_dy = 4
        elif dy > 40:
            ball_dx = 5 * sx
            ball_dy = 2
        elif dy > 30:
            ball_dx = 5 * sx
            ball_dy = 1
        elif dy < 0:
            ball_dx = 2 * sx
            ball_dy = -5
        elif dy < 10:
            ball_dx = 4 * sx
            ball_dy = -4
        elif dy < 20:
            ball_dx = 5 * sx
            ball_dy = -2
        elif dy < 30:
            ball_dx = 5 * sx
            ball_dy = -1
        else:
            ball_dx = 5 * sx
            ball_dy = 0

def reset_ball():
    poke({rect[BALL_ID].x}, {BALL_POS[0]})
    poke({rect[BALL_ID].y}, {BALL_POS[1]})
    poke({rect[BALL_ID + 1].x}, peek({rect[BALL_ID].x}) + {BALL_SIZE // 2})
    poke({rect[BALL_ID + 1].y}, peek({rect[BALL_ID].y}))
    ball_dx = 5 * sign(starter)
    ball_dy = 0

def hit_box(x1, y1, x2, y2, base, extra):
    addr_b = rect_addr(base)
    bx1 = peek(addr_b + {RECT_X})
    by1 = peek(addr_b + {RECT_Y})
    bx2 = bx1
    by2 = by1
    if extra != base:
        addr_e = rect_addr(extra)
        bx1 += peek(addr_e + {RECT_X})
        by1 += peek(addr_e + {RECT_Y})
        bx2 = bx1 + peek(addr_e + {RECT_W})
        by2 = by1 + peek(addr_e + {RECT_H})
    else:
        bx2 += peek(addr_b + {RECT_W})
        by2 += peek(addr_b + {RECT_H})
    if x2 < bx1:
        return false
    if x1 > bx2:
        return false
    if y2 < by1:
        return false
    if y1 > by2:
        return false
    return true
'''
anim = f'''
def animate():
    i = 0
    while i < 2:
        anim_cursor[i] += 1
        if anim_cursor[i] >= {CURSOR_ANIM_DUR}:
            anim_cursor[i] = 0
            anim_cursor_frame[i] += 1
            if anim_cursor_frame[i] >= 4:
                anim_cursor_frame[i] = 0
            animate_cursor_post_frame(anim_cursor_frame[i], i)
        if anim_score[i] >= 0:
            anim_score[i] -= 1
            animate_score_post(anim_score[i], i)
        i += 1
    if anim_restart >= 0:
        anim_restart -= 1
        if anim_restart < 0:
            store_score(-1)
            reset_ball()
    if anim_reset >= 0:
        if anim_reset == {RESET_TIME}:
            reset_index = 3 - reset_index
            addr = rect_addr(starter) + {RECT_COLOR}
            poke(addr, colors[(player_colors[2 + starter * 3] << 2) + reset_index])
        anim_reset -= 1
        if anim_reset > 0:
            store_score(starter)
        elif anim_restart > 0:
            anim_reset = {RESET_TIME}
        else:
            i = 0
            while i < 6:
                score[i] = 0
                i += 1
            store_score(-1)

def animate_cursor_post_frame(frame, i):
    offset = {CURSOR_ANIM_OFFSET} * sign(frame > 1)
    addr = rect_addr(cursor_id_all[i]) + {RECT_Y}
    poke(addr, peek(addr) + offset)
    poke(addr + {RECT_SIZE}, peek(addr + {RECT_SIZE}) - (offset << 1))

def animate_score_post(anim, i):
    p = 0
    s = 0
    if anim >= {SCORE_TIME // 2}:
        p = -1
        s = 2
    elif anim >= 0:
        p = 1
        s = -2
    addr = rect_addr(score_id_all[i << 2])
    poke(addr + {RECT_X}, peek(addr + {RECT_X}) + p)
    poke(addr + {RECT_Y}, peek(addr + {RECT_Y}) + p)
    poke(addr + {RECT_W}, peek(addr + {RECT_W}) + s)
    poke(addr + {RECT_H}, peek(addr + {RECT_H}) + s)
'''
score = f'''
def count_score(player, delta):
    offset = player * {SCORE_DIGIT_COUNT}
    s1 = score[2 + offset]
    s2 = score[1 + offset]
    s3 = score[offset]
    s1 += delta
    d2 = 0
    while s1 < 0:
        s1 += 10
        d2 -= 1
    while s1 >= 10:
        s1 -= 10
        d2 += 1
    s2 += d2
    d3 = 0
    while s2 < 0:
        s2 += 10
        d3 -= 1
    while s2 >= 10:
        s2 -= 10
        d3 += 1
    s3 += d3
    finisher = -1
    if s3 < 0:
        s1 = 0
        s2 = 0
        s3 = 0
    elif s3 >= 10:
        while s3 >= 10:
            s3 -= 10
        finisher = player
    score[2 + offset] = s1
    score[1 + offset] = s2
    score[offset] = s3
    store_score(finisher)
    return finisher != -1

def store_score(finisher):
    offset = finisher * {SCORE_DIGIT_COUNT}
    i = 0
    while i < 6:
        j = 1 + i + (i > 2)
        k = j << 1
        y = score_pos[k + 1]
        if ((i - offset) & 0xff) < 3:
            y -= {SCREEN_H}
        addr_s = rect_digits + score[i] * {SCORE_DIGIT_SIZE}
        addr_t = rect_addr(score_id_all[j])
        copy(addr_s, addr_t, {SCORE_DIGIT_SIZE})
        poke(addr_t + {RECT_X}, score_pos[k])
        poke(addr_t + {RECT_Y}, y)
        i += 1
'''
base = f'''
def copy(src, dst, size):
    end = src + size
    while src < end:
        poke(dst, peek(src))
        src += 1
        dst += 1

def rect_addr(i):
    return {RECT_MEM} + i * {RECT_SIZE}

def sign(expr):
    return (expr << 1) - 1
'''
fields = f'''
# Generic
false = 0
true = 1

# Common
playing = 0 # false
player_colors = [0, 0, 0, 0, 0, 0]
starter = 0
score = [0, 0, 0, 0, 0, 0]
reset_index = 3

# Keys
key_cache = {[0] * KEY_NUM}
key_a_a2 = 0 # false

# Menu
cursor_min = 0
cursor_max = 2
cursor_show_offset = -{SCREEN_H << 1}
cursor_hide_offset = {SCREEN_H << 1}
cursors = [-1, -1]
cursor_offsets = [-{SCREEN_H << 1}, -{SCREEN_H << 1}]

# Physics
player_speed = 5
ball_dx = -5
ball_dy = 0

# Animations
anim_cursor = [0, 0]
anim_cursor_frame = [0, 0]
anim_score = [-1, -1]
anim_restart = -1
anim_reset = -1

# Arrays
colors = {COLORS}
color_targets = {COLOR_TARGETS * 2}
color_index = {COLOR1_INDEX + COLOR2_INDEX}
cursor_id_all = {CURSOR_ID_ALL}
cursor_pos_ref = {CURSOR1_POS_REF + CURSOR2_POS_REF}
player_id_all = {BOARD_ID_ALL}
score_pos = {SCORE1_POS + SCORE2_POS}
score_id_all = {SCORE1_ID_ALL + SCORE2_ID_ALL}
rect_all = {RECTANGLES_ALL}
rect_digits = {SCORE_DIGITS}
'''

save_game('pong.bin', main + keys + menu + physics + anim + score + base + fields)
