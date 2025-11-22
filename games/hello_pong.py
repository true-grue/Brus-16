from brus16 import *

SPEED = 5
WHITE = rgb(0xffffff)

BALL_SIZE = 20
BALL_START_X = (SCREEN_W // 2) - (BALL_SIZE // 2)
BALL_START_Y = (SCREEN_H // 2) - (BALL_SIZE // 2)

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
LEFT_PADDLE_X = 50
RIGHT_PADDLE_X = SCREEN_W - (LEFT_PADDLE_X + PADDLE_WIDTH)
PADDLE_START_Y = (SCREEN_H // 2) - (PADDLE_HEIGHT // 2)

BALL_RECT = rect[0]
LEFT_PAD_RECT = rect[1]

GAME_RECTS = [1, BALL_START_X, BALL_START_Y, BALL_SIZE, BALL_SIZE, WHITE] + \
             [1, LEFT_PADDLE_X, PADDLE_START_Y, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE] + \
             [1, RIGHT_PADDLE_X, PADDLE_START_Y, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE]

save_game('hello_pong.bin', f'''
def main():
    setup()
    while 1:
        draw()
        wait()

def setup():
    copy(game_rects, {RECT_MEM}, {len(GAME_RECTS)})

def draw():
    move_paddle(0, {KEY_MEM + KEY_UP}, {KEY_MEM + KEY_DOWN})
    move_paddle(1, {KEY_MEM + KEY_UP2}, {KEY_MEM + KEY_DOWN2})
    move_ball()

def move_paddle(pad, key_up, key_down):
    addr_y = {LEFT_PAD_RECT.y} + pad * {RECT_SIZE}
    dy = (peek(key_down) - peek(key_up)) * {SPEED}
    poke(addr_y, limit(peek(addr_y) + dy, 0, {SCREEN_H - PADDLE_HEIGHT}))

def move_ball():
    x = peek({BALL_RECT.x})
    y = peek({BALL_RECT.y})
    x += ball_speed_x
    y += ball_speed_y
    y = bounce_walls(y)
    if check_goal(x):
        return
    x = collide_paddles(x, y)
    poke({BALL_RECT.x}, x)
    poke({BALL_RECT.y}, y)

def bounce_walls(y):
    if (y < 0) | (y > {SCREEN_H - BALL_SIZE}):
        ball_speed_y = -ball_speed_y
    return limit(y, 0, {SCREEN_H - BALL_SIZE})

def check_goal(x):
    if (x < 0) | (x > {SCREEN_W - BALL_SIZE}):
        reset_ball()
        return 1
    return 0

def collide_paddles(x, y):
    hit = -1
    if check_overlap(0, x, y):
        hit = 0
    elif check_overlap(1, x, y):
        hit = 1
    if hit == -1:
        return x
    ball_speed_x = -ball_speed_x
    pad_y = peek({LEFT_PAD_RECT.y} + hit * {RECT_SIZE})
    if y + {BALL_SIZE // 2} > pad_y + {PADDLE_HEIGHT // 2}:
        ball_speed_y = {SPEED}
    else:
        ball_speed_y = -{SPEED}
    if hit == 0:
        return {LEFT_PADDLE_X + PADDLE_WIDTH}
    return {RIGHT_PADDLE_X - BALL_SIZE}

def check_overlap(pad, x, y):
    px = peek({LEFT_PAD_RECT.x} + pad * {RECT_SIZE})
    py = peek({LEFT_PAD_RECT.y} + pad * {RECT_SIZE})
    if x > px + {PADDLE_WIDTH}:
        return 0
    if x + {BALL_SIZE} < px:
        return 0
    if y > py + {PADDLE_HEIGHT}:
        return 0
    if y + {BALL_SIZE} < py:
        return 0
    return 1

def reset_ball():
    poke({BALL_RECT.x}, {BALL_START_X})
    poke({BALL_RECT.y}, {BALL_START_Y})
    ball_speed_y = 0
    ball_speed_x = -ball_speed_x

def limit(val, min_val, max_val):
    if val < min_val:
        return min_val
    if val > max_val:
        return max_val
    return val

def copy(src, dst, size):
    end = src + size
    while src < end:
        dst[0] = src[0]
        src += 1
        dst += 1

ball_speed_x = -{SPEED}
ball_speed_y = 0
game_rects = {GAME_RECTS}
''')
