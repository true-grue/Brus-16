def start():
    main()

#def debug_val(x):
#   d = (x >> 12) & 15
#   poke(-1, d + 48 + (d > 9) * 7)
#   d = (x >> 8) & 15
#   poke(-1, d + 48 + (d > 9) * 7)
#   d = (x >> 4) & 15
#   poke(-1, d + 48 + (d > 9) * 7)
#   d = x & 15
#   poke(-1, d + 48 + (d > 9) * 7)
#   poke(-1, 10)

FG = 0
BG = 0
FILL = 0
DIV = 0
OBJS = {OBJS}
TITLE = {TITLE}
ASTEROID = {ASTEROID}
STARS= {STARS}
SHAKE_MODE = 0
ENDING_MODE = 0
HERO_DEAD = 0
HERO_LDIRS = {HERO_LASER_DIR}
DIRS = {DIRS}
HERO_C = {HERO_C}
FRAMES = 0
RADAR_MAP = {RADAR_MAP}
SPAWN_FRAME = 0
PADS_NR = 0
PADS_MAX = 0
SPAWNS_NR = 0
SPAWN_ID = 0
TELEPORT_FRAME = 0
POWER_DRAW = 0
LEVELS = {LEVELS}
LEVELS_DIR = {LEVELS_DIR}
LEVEL_NR = 0
HEROR = {HERO}
HEROL = {HEROL}
HEROU = {HEROU}
HEROD = {HEROD}
ALIEN = {ALIEN}
ALIENS = {ALIENS}
ALIENS_NR = 0
OBS = {OBS}
OBS_NR = 0

SPAWNS = {SPAWNS}
LEVEL = 0
NEXT_LEVEL = 0
HERO_DIR = 0

PX = 0
PY = 0

EXIT_CX = 0
EXIT_CY = 0

LASER_X = -1
LASER_Y = 0
LASER_X2 = 0
LASER_Y2 = 0

def rgb(r, g, b):
    return ((r>>3) << 11) | ((g>>2) << 5) | (b>>3)

def abs(a):
    if a < 0:
        return -a
    return a

def max(a, b):
    if a > b:
        return a
    return b

def min(a, b):
    if a < b:
        return a
    return b

def memcpy(dst, src, size):
    end = src + size
    while src < end:
        poke(dst, src[0])
        src += 1
        dst += 1

def bzero(dst, size):
    end = dst + size
    while dst < end:
        dst[0] = 0
        dst += 1

def bit(a, v):
    return (a&v) != 0

def not_bit(a, v):
    return (a&v) == 0

def bit_sethi(a, mask, v):
    a &= ~mask
    a |= v<<8
    return a

def bit_gethi(a, mask):
    return (a & mask)>>8

def to_bool(a):
    return a != 0

seed = 7

def rnd():
    seed = random(seed)
    return seed

def random(s):
    s ^= s << 7
    s ^= s >> 9
    s ^= s << 8
    return s

def otype(m, t):
    if (m&{OB_MASK}) == t:
        return 1
    return 0

def ob(cx, cy, t):
    return otype(oget(cx, cy), t)

def obxy(x, y, t):
    return ob(x2c(x), y2c(y), t)

def oget(cx, cy):
    return OBJS[cy*{W}+cx]

def ogetxy(x, y):
    return oget(x2c(x), y2c(y))

def oset(cx, cy, v):
    ov = oget(cx, cy)
    OBJS[cy*{W}+cx] = v
    return ov

def oclr(cx, cy):
    return oset(cx, cy, 0)

def oclrxy(x, y):
    return oset(x2c(x), y2c(y), 0)

def mset(m, cx, cy, v):
    mask = 1<<cx
    r = (m[cy]&mask) != 0
    if v:
        m[cy] |= mask
    else:
        m[cy] &= ~mask
    return r

def msetxy(m, cx, cy, v):
    return mset(m, cx>>{TWS}, cy>>{THS}, v)

def inside(cx, cy):
    if (cx < 0) | (cx >= {W}):
        return 0
    if (cy < 0) | (cy >= {H}):
        return 0
    return 1

def insidexy(x, y):
    return inside(x>>{TWS}, y>>{THS})

def mget(m, cx, cy):
    return (m[cy]&(1<<cx)) != 0

def x2c(x):
    return x >> {TWS}

def y2c(y):
    return y >> {THS}

def x2tl(x, w):
    return x - (w>>1)

def y2tl(y, h):
    return y - (h>>1)

def c2int(cx, cy):
    return (cy<<4)|cx

def int2cx(v):
    return v&0xf

def int2cy(v):
    return (v>>4)&0xf

def c2x(c):
    return c*{TW}+({TW}>>1)

def c2y(c):
    return c*{TH}+({TH}>>1)

def oblock(x, y):
    if inside(x, y) == 0:
        return 1
    return bit(oget(x, y),{OB_OBSTACLE})

def oblockxy(x, y):
    return oblock(x2c(x), y2c(y))

def lookup_obs(cx, cy, t):
    if ob(cx, cy, t):
        o = oget(cx, cy)
        return OBS + ((o&0xff)*{OBS_SIZE})
    return 0

def lookup_door(cx, cy):
    return lookup_obs(cx, cy, {OB_DOOR})

def lookup_reactor(cx, cy):
    return lookup_obs(cx, cy,  {OB_REACTOR})

def obs_add(cx, cy, it):
    OBS[OBS_NR*{OBS_SIZE}] = c2int(cx, cy)
    OBS[OBS_NR*{OBS_SIZE}+1] = it
    oset(cx, cy, (it&0xff00)|OBS_NR)
    OBS_NR += 1

def loadlev():
    bzero(OBJS, {W*H})

    current_zoom = {1 << ZOOM_BITS}
    SHAKE_MODE = 0
    ENDING_MODE = 0
    EXPLODE_MODE = 0
    NEXT_LEVEL = LEVEL
    SCROLL_MODE = 480
    RADAR_MODE = 0
    HERO_DEAD = 0
    HERO_DIR = 3

    y = 0
    while y < {H}:
        x = 0
        while x < {W}:
            if mget(LEVEL, x, y):
                oset(x, y, {OB_WALL})
            x += 1
        y += 1

    cb = LEVEL + {H}

    t = cb[0]

    # hero
    PX = c2x(int2cx(t))
    PY = c2y(int2cy(t))

    # exit
    EXIT_CX = (t>>8)&0xf
    EXIT_CY = (t>>12)&0xf

    ALIENS_NR = 0
    bzero(ALIENS, {ALIENS_SIZE})

    OBS_NR = 0
    bzero(OBS, {OBS_MAX*OBS_SIZE})
    # colors
    cb += 1
    FG = cb[0]
    BG = cb[1]
    FILL = cb[2]
    DIV = cb[3]
    # items
    cb += 4
    cb_start = cb
    bzero(SPAWNS, {SPAWNS_MAX})
    PADS_NR = 0
    SPAWNS_NR = 0
    SPAWN_ID = 0
    SPAWN_FRAME = FRAMES

    TELEPORT_FRAME = FRAMES

    while 1:
        if cb[0] == 0:
            break
        cx = int2cx(cb[0])
        cy = int2cy(cb[0])
        it = cb[0]&{OB_MASK}
        if it == {OB_PAD}:
            oset(cx, cy, it)
            PADS_NR += 1
        elif (it == {OB_SPAWN}):
            fl = 0
            if bit(cb[0], {OB_BOSS}):
                fl = {SPAWN_BOSS}
            SPAWNS[SPAWNS_NR] = c2int(cx, cy) | fl
            oset(cx, cy, {OB_SPAWN})
            SPAWNS_NR += 1
        elif it == {OB_ALIEN}:
            new_alien(c2x(cx), c2y(cy))
            if bit(cb[0], {OB_BOSS}):
                ALIENS[(ALIENS_NR-1)*{ALIEN_SIZE}+2] |= {ALIEN_BOSS}
        elif it == {OB_REACTOR}:
            obs_add(cx, cy, cb[0])
            PADS_NR += 1
        elif it == {OB_TRAP}:
            oset(cx, cy, (cb[0]&0xff00)|(cb-cb_start+1))
            while cb[0]&0xff00:
                cb += 1
        else:
            obs_add(cx, cy, cb[0])
        cb += 1

    PADS_MAX = PADS_NR

def draw_rect(ptr, x, y, w, h, col):
    if (ptr >= {RECT_MEM+RECT_SIZE*RECT_NUM}):
        return ptr
    ptr[0] = 1
    set_rect(ptr, x, y, w, h)
    ptr[5] = col
    return ptr + {RECT_SIZE}

# ha-ha :)
def draw_circle(ptr, cx, cy, r, col):
    if (ptr >= {RECT_MEM+RECT_SIZE*RECT_NUM}):
        return ptr
    ptr[0] = 1
    set_rect(ptr, cx - r, cy - r, 2*r, 2*r)
    ptr[5] = col
    return ptr + {RECT_SIZE}

def inside_view(x, y):
    return hit1(x2c(PX) - {VIEW_R}, y2c(PY) - {VIEW_R}, {VIEW_SIZE}, {VIEW_SIZE}, x2c(x), y2c(y))

def draw_laser(ptr):
    if LASER_X < 0:
        return ptr

    ex = LASER_X2
    ey = LASER_Y2

    if LASER_X2 != LASER_X:
        ex &= ~{TWM}
        ex += {TW//2}
        ey += 1

    if LASER_Y2 != LASER_Y:
        ey &= ~{THM}
        ey += {TH//2}
        ex += 1

    if inside_view(ex, ey) == 0:
        ptr = draw_mrect(ptr, x2c(ex), y2c(ey), 0, 0)

    x = LASER_X
    y = LASER_Y

    if (ex < x) | (ey < y):
        {mswap("x", "ex")}
        {mswap("y", "ey")}

    color = rate_color({LASERCOL_RATE}, {LASERCOL1}, {LASERCOL2})

    return draw_rect(ptr, x, y, abs(ex - x), abs(ey - y), color)

def upd_obs():
    i = 0
    while i < OBS_NR:
        obs = OBS+i*{OBS_SIZE}
        if bit(obs[0], {OBS_DEAD}):
            e = bit_gethi(obs[0], {OBS_MASK}) + 1
            m = 4
            if otype(obs[1], {OB_REACTOR}):
                m = 0x1f
            if e > m:
                if oclr(int2cx(obs[0]), int2cy(obs[0])):
                    EXPLODE_MODE += 1
                    if otype(obs[1], {OB_REACTOR}):
                        PADS_NR -= 1
                        if PADS_NR == 0:
                            ENDING_MODE = 1
                            return
            else:
                obs[0] = bit_sethi(obs[0], {OBS_MASK}, e)
        elif otype(obs[1], {OB_REACTOR}):
            e = max(0, bit_gethi(obs[0], {OBS_MASK}) - rate_trigger(2))
#            debug_val(e)
            SHAKE_MODE += (e > 0xf)
            obs[0] = bit_sethi(obs[0], {OBS_MASK}, e)
        i += 1

def obs_laser(obs, hit, health):
    e = bit_gethi(obs[0], {OBS_MASK}) + hit
    obs[0] |= {OBS_HIT}
    if (e >= health) & not_bit(obs[0], {OBS_DEAD}):
        obs[0] = bit_sethi(obs[0], {OBS_MASK}, 0)
        obs[0] |= {OBS_DEAD}
    elif not_bit(obs[0], {OBS_DEAD}):
        obs[0] = bit_sethi(obs[0], {OBS_MASK}, e)

def alien_hit_laser(a):
    e = bit_gethi(a[2], {ALIEN_MASK})
    a[2] |= {ALIEN_HIT}
    if (e > 0) & not_bit(a[2], {ALIEN_DEAD}):
        if bit(a[2],{ALIEN_BOSS}):
            e -= rate_trigger(3)
        else:
            e -= 1
        a[2] = bit_sethi(a[2], {ALIEN_MASK}, e)
    elif not_bit(a[2], {ALIEN_DEAD}):
        a[2] = {ALIEN_DEAD | (ALIEN_HEALTH<<8)}

def upd_laser():
    a = ALIENS
    ae = ALIENS + {ALIENS_SIZE}
    while a < ae:
        a[2] &= {~ALIEN_HIT}
        a += {ALIEN_SIZE}

    i = 0
    while i < OBS_NR:
        obs = OBS + i*{OBS_SIZE}
        obs[0] &= ~{OBS_HIT}

        if otype(obs[1], {OB_DOOR}):
            if ((LASER_X == -1) | (bit(obs[1], {OB_BOSS}))) & not_bit(obs[0], {OBS_DEAD}):
                obs[0] = bit_sethi(obs[0], {OBS_MASK}, 0)
        i += 1

    if (HERO_DEAD > 0) | (abs(FRAMES-TELEPORT_FRAME) < 30):
        LASER_X = -1
        return

    if (INP_STATE[{KEY_A}] == 0) | (INP_C == 1):
        if (INP_X == 0) & (INP_Y == 0):
            POWER_DRAW = max(0, POWER_DRAW - {POWER_CHARGE})
        else:
            POWER_DRAW = max(0, POWER_DRAW - {POWER_CHARGE_MOVE})
        LASER_X = -1
        return 0
    POWER_DRAW = min(POWER_DRAW + {LASER_COST}, {POWER_DRAW_MAX})
    if POWER_DRAW >= {POWER_DRAW_MAX}:
        LASER_X = -1
        return 0

    x = PX + HERO_LDIRS[HERO_DIR*2]
    y = PY + HERO_LDIRS[HERO_DIR*2+1]
    dx = DIRS[HERO_DIR*2]*({TW//2})
    dy = DIRS[HERO_DIR*2+1]*({TH//2})

    ex = x
    ey = y

    a = 0

    while oblockxy(ex, ey) == 0:
        ex += dx
        ey += dy
        a = scan_alien(ex, ey, 0)
        if a != 0:
            alien_hit_laser(a)
            break

    if lookup_door(x2c(ex), y2c(ey)) != 0:
        door = lookup_door(x2c(ex), y2c(ey))
        obs_laser(door, 2, {DOOR_HEALTH})

    elif lookup_reactor(x2c(ex), y2c(ey)) != 0:
        r = lookup_reactor(x2c(ex), y2c(ey))
        obs_laser(r, 1, {R_HEALTH})

    ex = max(-1, ex)
    ey = max(-1, ey)
    ex = min(ex, {W*TW})
    ey = min(ey, {H*TH})

    LASER_X = x
    LASER_Y = y
    LASER_X2 = ex
    LASER_Y2 = ey

LEGS = [1, 3, 5, 7, 5, 3, 2, 1]

def light_ray(x, y, tx, ty, r):
    dx = 0
    dy = 0

    if tx - x > 0:
        dx = 1
    elif tx - x < 0:
        dx = -1

    if ty - y > 0:
        dy = 1
    elif ty - y < 0:
        dy = -1

    if (x != tx) & (y != ty) & (abs(tx-x) != abs(ty-y)):
        return 0;

    while (abs(tx - x) <= r) & (abs(ty - y) <= r):
        if oblock(x, y):
            return 0
        x += dx
        y += dy
        if (x == tx) & (y == ty):
            return 1
    return 0

def alien_light_cell(a):
    if inside_view(a[0], a[1]) == 0:
        return 0

    px = PX >> {TWS}
    py = PY >> {THS}
    tx = a[0] >> {TWS}
    ty = a[1] >> {THS}

    if (px == tx) | (py == ty) | (abs(tx-px) == abs(ty-py)):
        return light_ray(px, py, tx, ty, {VIEW_R})

    dx = 0; dy = 0

    if abs(tx-px) > abs(ty-py): #h
        if tx > px:
            dx = 1
        else:
            dx = -1
    else: #v
        if ty > py:
            dy = 1
        else:
            dy = -1

    i = 0
    while i < 2:
        i += 1
        if light_ray(px, py, px + dx*i, py + dy*i, 1) == 0:
            return 0
        px += dx; py += dy
        if oblock(px, py):
            return 0
        if light_ray(px, py, tx, ty, {VIEW_R}-i):
            return 1
    return 0

def alien_visible(a):
    return bit(a[2], {ALIEN_HIT}) | alien_light_cell(a)

def draw_alien(ptr, a):
    x = a[0]
    y = a[1]

    if (alien_visible(a) == 0) | (ptr >= {RECT_MEM+RECT_SIZE*RECT_NUM}):
        return ptr

    memcpy(ptr, ALIEN, {len(ALIEN)})

    ptr[1] = x2tl(x, ALIEN[3])
    ptr[2] = y2tl(y, ALIEN[4])

    i = 0
    while i < {len(ALIEN)//RECT_SIZE}:
        col = ALIEN_COLS[i]
        if bit(a[2], {ALIEN_BOSS}):
            col = rate_color(3, {rgb(106,50,159)}, {rgb(82,32,129)})
        f = i*{RECT_SIZE}
        if bit(a[2],{ALIEN_HIT}):
            col = 0xffff
        if bit(a[2], {ALIEN_DEAD}):
            e = (0xf - (a[2]>>8)&0xf)
            ptr[f+3] = max(0, ptr[f+3]+e)
            ptr[f+4] = max(0, ptr[f+3]+e)
            ptr[f+1] -= e
            ptr[f+2] -= e
            col = 0xff00
        i += 1
        ptr[f+5] = col

    if a[2]&{ALIEN_DEAD}:
        return ptr + {len(ALIEN)}

    n = (FRAMES>>2)&0x7
    ptr += {RECT_SIZE}
    if a[2]&{ALIEN_SIGHT}:
        ptr[1] = 8
        ptr[3] = 7
    else:
        ptr[3] = LEGS[n]
        ptr[1] = 1 + (LEGS[n]*2)

    if bit(a[2], {ALIEN_BOSS}) & not_bit(a[2],{ALIEN_HIT}):
        ptr[5] = { rgb(15, 255, 80) }
    ptr += {RECT_SIZE}
    ptr[4] = LEGS[n]
    ptr += {RECT_SIZE}
    ptr[4] = LEGS[(n+2)&0x7]
    ptr += {RECT_SIZE}
    ptr[4] = LEGS[(n+5)&0x7]
    return ptr + {RECT_SIZE}

def draw_hero(ptr, cx, cy):
    if HERO_DIR == 0:
        memcpy(ptr, HEROR, {len(HERO)})
    elif HERO_DIR == 2:
        memcpy(ptr, HEROL, {len(HERO)})
    elif HERO_DIR == 1:
        memcpy(ptr, HEROU, {len(HERO)})
    else:
        memcpy(ptr, HEROD, {len(HERO)})

    if (INP_X != 0) | (INP_Y != 0):
        lo = (FRAMES >> 2)&0x3
        ptr[4*{RECT_SIZE}+4] += 1 - lo
        ptr[5*{RECT_SIZE}+4] += -1 + lo

    ptr[1] = cx - HERO_C[0]
    ptr[2] = cy - HERO_C[1]

    if abs(FRAMES-TELEPORT_FRAME) < 48:
        i = 0
        while i < {len(HERO)}:
            poke(ptr + i + 5, rate_color(3, 0xffff, ptr[i+5]))
            i += {RECT_SIZE}

    if HERO_DEAD > 0:
        h = 16
        d = min(HERO_DEAD, h)
        wl = h - d
        ptr[2] += d
        ptr[4] = max(wl, 2)
        if ptr[4] == 2:
            ptr[5] = {rgb(200, 0, 0)}
            ptr[3] = min(ptr[3]+(HERO_DEAD-h), 12)
        i = {RECT_SIZE}
        while i < {len(HERO)}:
            ptr[i+2] = min(ptr[i+2], wl)
            sy = min(ptr[i+2]+ptr[i+4], wl)
            ptr[i+4] = sy - ptr[i+2]
            i += {RECT_SIZE}
    return ptr + {len(HERO)}

def rate(r):
    return (FRAMES >> r)&1

def rate_shift(r, s):
    return ((FRAMES+s) >> r)&1

def rate_trigger(r):
    return (((FRAMES-1) >> r)&1) != ((FRAMES >> r)&1)

def rate_color(r, c1, c2):
    if rate(r):
        return c1
    return c2

rect_clip = [0, 0, 0, 0, 0, 0]

def item_rect(dst, x, y, w, h, clip):
    if hit2(x, y, w, h, clip[1], clip[2], clip[3], clip[4]) == 0:
        return 0

    nx = max(clip[1], x)
    ny = max(clip[2], y)
    dst[3] = max(1, min(clip[1] + clip[3], x + w) - nx)
    dst[4] = max(1, min(clip[2] + clip[4], y + h) - ny)
    dst[1] = nx
    dst[2] = ny

    return 1

#def mrect_sprite(dst, ptr, l, x, y, xoff, yoff):
#    mrect_clip(rect_clip, xoff, yoff)
#    eptr = ptr + l
#    while ptr < eptr:
#        if item_rect(dst, ptr[1], ptr[2], ptr[3], ptr[4], rect_clip) == 1:
#            dst[5] = ptr[5]
#            dst[0] = 1
#            dst[1] += x<<{TW}
#            dst[2] += y<<{TH}
#            dst += {RECT_SIZE}
#        ptr += {RECT_SIZE}

def mrect_clip(ptr, xoff, yoff):
    xmod = xoff >> 8
    ymod = yoff >> 8
    xoff = xoff & {TWM}
    yoff = yoff & {THM}

    ptr[1] = 0
    ptr[2] = 0

    if xmod == 1:
        ptr[1] = xoff
        ptr[3] = {TW} - xoff
    elif xmod == 2:
        ptr[3] = xoff
    else:
        ptr[3] = {TW}

    if ymod == 1:
        ptr[2] = yoff
        ptr[4] = {TH} - yoff
    elif ymod == 2:
        ptr[4] = yoff
    else:
        ptr[4] = {TH}


def atexit(cx, cy):
    return (cx == EXIT_CX) & (cy == EXIT_CY)

def atexitxy(x, y):
    return atexit(x2c(x), y2c(y))

def laser_hor(cx, cy):
    return bit(oget(cx, cy), {OB_H})

def draw_mrect(ptr, cx, cy, xoff, yoff):
    x = 0
    y = 0
    w = {TW}
    h = {TH}

#    if inside(cx, cy) == 0:
#        return ptr
    obj = 0
    ot = 0

    if inside(cx, cy):
        obj = oget(cx, cy)
        ot = obj&{OB_MASK}
    if inside(cx, cy) == 0:
        ptr[5] = FG
    elif ot == {OB_WALL}:
        ptr[5] = FG
    elif atexit(cx, cy):
        if exit_activated():
            ptr[5] = rate_color({EXITCOL_RATE}, {EXITCOL3}, {EXITCOL4})
        else:
            ptr[5] = rate_color({EXITCOL_RATE}, {EXITCOL1}, {EXITCOL2})
        x += 2; y += 2; w -= 4; h -= 4
    elif ot == {OB_PAD}:
        ptr[5] = rate_color({PADCOL_RATE}, {PADCOL1}, {PADCOL2})
        w = {TW//4}; h = {TH//4}
        amp = 8
        offs = 4
        mask = 15
        x = {TH//4} + amp - abs(amp - (FRAMES & mask))
        y = {TH//4} + amp - abs(amp - ((FRAMES + offs) & mask))
    elif ot == {OB_SPAWN}:
        ptr[5] = rate_color({SPAWNCOL_RATE}, {SPAWNCOL1}, {SPAWNCOL2})
        x = 2; y = 2; w = {TW-4}; h = {TH-4}
    elif (ot == {OB_TRAP}) & not_bit(obj, {OB_SECRET}):
        traps = LEVEL + (obj&0xff) + {LEVEL_HEADER}
        x = 12; y = 12; w = 8; h = 8
        if oget(int2cx(traps[0]), int2cy(traps[0])):
            ptr[5] = rate_color({BTN_RATE}, {BTNCOL1}, {BTNCOL2})
        else:
            ptr[5] = {BTNCOL2}
    elif ot == {OB_LASER}:
        if check_laser_active(cx, cy):
            if laser_hor(cx, cy):
                x = 0; y  = 15 ^ (FRAMES&1); w = {TW}; h = 1
            else:
                x = 15 ^ (FRAMES&1); y = 0; w = 1; h = {TH}
            ptr[5] = rate_color(1, {rgb(255, 0, 0)}, {rgb(0, 255, 0)})
        else:
            return ptr
    elif ot == {OB_DOOR}:
        door = lookup_door(cx, cy)
        if bit(door[0], {OBS_DEAD}):
            ptr[5] = 0xff00
        elif bit(door[0], {OBS_HIT}):
            ptr[5] = 0xffff
        elif bit(door[1], {OB_SECRET}):
            ptr[5] = FG
        elif bit(door[1], {OB_BOSS}):
            ptr[5] = { DOORCOL_BOSS }
        else:
            ptr[5] = { DOORCOL }
        if not_bit(door[1], {OB_SECRET}):
            if bit(obj, {OB_H}):
                x = 1; y = {TH//2-8}; w = {TW-2}; h = 16
            else:
                x = {TW//2-8}; y = 1; w = 16; h = {TH-2}

        if bit(door[0], {OBS_DEAD}):
            x += 7 - (rnd() & 0xf)
            y += 7 - (rnd() & 0xf)
            w += 7 - (rnd() & 0xf)
            h += 7 - (rnd() & 0xf)
        elif bit(door[0], {OBS_HIT}):
            x ^= rnd()&1
            y ^= rnd()&1
            w ^= rnd()&1
            h ^= rnd()&1
    elif ot == {OB_REACTOR}:
        r = lookup_reactor(cx, cy)

        w = 16
        h = 16
        x = abs(0xf-((FRAMES+8)&0x1f))
        y = abs(0xf-(FRAMES&0x1f))

        if bit(r[0], {OBS_HIT}):
            ptr[5] = 0xffff
            w = 16 #(FRAMES&{TWM//2-1})*2
            h = 16 # (FRAMES&{TWM//2-1})*2
            x += 7 - (rnd() & 0xf)
            y += 7 - (rnd() & 0xf)
        else:
            ptr[5] = rate_color({SPAWNCOL_RATE}, {SPAWNCOL1}, {SPAWNCOL2})

        if bit(r[0], {OBS_DEAD}):
            x += 0xf - (rnd() & 0x1f)
            y += 0xf - (rnd() & 0x1f)
            w += 0xf - (rnd() & 0x1f)
            h += 0xf - (rnd() & 0x1f)
    else:
        return ptr

    if EXPLODE_MODE > 0:
        ptr[5] = 0xffff

    mrect_clip(rect_clip, xoff, yoff)

    if item_rect(ptr, x, y, w, h, rect_clip) == 0:
        return ptr

    ptr[0] = 1
    ptr[1] += cx*{TW}
    ptr[2] += cy*{TH}

    return ptr + {RECT_SIZE}

def vwall_scan(sx, sy, ey):
    r = 0
    while sy <= ey:
        if inside(sx, sy) == 1:
            if ob(sx, sy, {OB_WALL}) == 0:
                break
        sy += 1
        r += 1
    return r

def hwall_scan(sx, sy, ex):
    r = 0
    while sx <= ex:
        if inside(sx, sy) == 1:
            if ob(sx, sy, {OB_WALL}) == 0:
                break
        sx += 1
        r += 1
    return r

def draw_hwall(ptr, sx, sy, ex, xoff, yoff):
    while sx <= ex:
        l = hwall_scan(sx, sy, ex)
        optr = ptr
        ptr = draw_mrect(ptr, sx, sy, xoff, yoff)
        if l > 0:
            sx += l
            optr[3] = l*{TW}
        else:
            sx += 1
    return ptr

def draw_vwall(ptr, sx, sy, ey, xoff, yoff):
    while sy <= ey:
        l = vwall_scan(sx, sy, ey)
        optr = ptr
        ptr = draw_mrect(ptr, sx, sy, xoff, yoff)
        if l > 0:
            sy += l
            optr[4] = l*{TH}
        else:
            sy += 1
    return ptr

def draw_map(ptr, x, y):
    xoff = x & {TWM}
    yoff = y & {THM}
    x >>= {TWS}
    y >>= {THS}

    r = {VIEW_R} - 1
    ptr = draw_hwall(ptr, x - r, y - {VIEW_R}, x + r, 0, yoff|0x100)
    ptr = draw_hwall(ptr, x - r, y + {VIEW_R}, x + r, 0, yoff|0x200)

    ptr = draw_vwall(ptr, x - {VIEW_R}, y - r, y + r, xoff|0x100, 0)
    ptr = draw_vwall(ptr, x + {VIEW_R}, y - r, y + r, xoff|0x200, 0)

    ptr = draw_mrect(ptr, x-{VIEW_R}, y-{VIEW_R}, xoff|0x100, yoff|0x100)
    ptr = draw_mrect(ptr, x-{VIEW_R}, y+{VIEW_R}, xoff|0x100, yoff|0x200)
    ptr = draw_mrect(ptr, x+{VIEW_R}, y-{VIEW_R}, xoff|0x200, yoff|0x100)
    ptr = draw_mrect(ptr, x+{VIEW_R}, y+{VIEW_R}, xoff|0x200, yoff|0x200)
    sy = y - r
    while sy <= y + r:
        ptr = draw_hwall(ptr, x - r, sy, x + r, 0, 0)
        sy += 1
    return ptr

INP_STATE = {KEY_STATE}

INP_Y = 0
INP_X = 0
INP_A = 0
INP_B = 0
INP_C = 0

def kbd_clear():
    INP_A = 0
    INP_B = 0
    INP_C = 0

def kbd_proc():
    i = 0
    while i < {KEY_NUM}:
        c = peek({KEY_MEM} + i)
        if c != INP_STATE[i]:
            if i == {KEY_UP}:
                INP_Y = -1*c
            elif i == {KEY_DOWN}:
                INP_Y = 1*c
            elif i == {KEY_LEFT}:
                INP_X = -1*c
            elif i == {KEY_RIGHT}:
                INP_X = 1*c
            elif i == {KEY_A}:
                INP_A = c
            elif i == {KEY_B}:
                INP_B = c
            elif i == {KEY_C}:
                INP_C = c
            INP_STATE[i] = c
        i += 1

    if INP_X == 0:
        if INP_STATE[{KEY_LEFT}]:
            INP_X = -1
        elif INP_STATE[{KEY_RIGHT}]:
            INP_X = 1

    if INP_Y == 0:
        if INP_STATE[{KEY_UP}]:
            INP_Y = -1
        elif INP_STATE[{KEY_DOWN}]:
            INP_Y = 1

def map_coll(x, y, rx, ry):
    return (oblockxy(x+rx, y-ry) | oblockxy(x+rx, y+ry) | oblockxy(x-rx, y-ry) |
        oblockxy(x-rx, y+ry))

def draw_radar(ptr, pos):
    y = 0
    b = 255 - (FRAMES&(0xffff>>(16-{RADAR_RATE})))*5
    pos >>= {THS}
    cx = PX>>{TWS}
    cy = PY>>{THS}
    while y < {H}:
        x = 0
        while x < {W}:
            if (pos > y):
                far = ((abs(cx-x)>{VIEW_R})|(abs(cy-y)>{VIEW_R}))
                if mget(RADAR_MAP, x, y):
                    ptr = draw_circle(ptr, c2x(x), c2y(y), 4, rgb(b,0,0))
                elif ob(x, y, {OB_PAD}) & far:
                    ptr = draw_circle(ptr, c2x(x), c2y(y), 4, rgb(b,b,0))
                elif atexit(x, y) & far:
                    ptr = draw_circle(ptr, c2x(x), c2y(y), 4, rgb(0,b,b))
            x += 1
        y += 1
    return ptr

def draw_aliens(ptr):
    a = ALIENS
    ae = ALIENS + {ALIENS_SIZE}
    while a < ae:
        if a[2] != 0:
            ptr = draw_alien(ptr, a)
        a += {ALIEN_SIZE}
    return ptr

def get_alien_dir():
    return rnd()&0x3

def spawn_alien():
    if SPAWNS_NR == 0:
        return
    if ltu(abs(FRAMES-SPAWN_FRAME), {SPAWN_DELAY}):
        return
    spawn = SPAWNS[SPAWN_ID]
    sx = c2x(int2cx(spawn))
    sy = c2y(int2cy(spawn))
    if scan_alien(sx, sy, 0) != 0:
        return
    SPAWN_ID += 1
    if SPAWN_ID >= SPAWNS_NR:
        SPAWN_ID = 0
    if new_alien(sx, sy):
        if bit(spawn, {SPAWN_BOSS}):
            ALIENS[(ALIENS_NR-1)*{ALIEN_SIZE}+2] |= {ALIEN_BOSS}


def new_alien(sx, sy):
    a = ALIENS
    ae = ALIENS + {ALIENS_SIZE}
    while a < ae:
        if a[2] == 0:
            a[0] = sx
            a[1] = sy
            a[2] = {ALIEN_HEALTH<<8} | get_alien_dir()
            ALIENS_NR += 1
            SPAWN_FRAME = FRAMES
            return 1
        a += {ALIEN_SIZE}
    return 0

def hit1(x, y, w, h, tx, ty):
    return (tx >= x) & (tx < x + w) & \
        (ty >= y) & (ty < y + h)

def hit2(x1, y1, w1, h1, x2, y2, w2, h2):
    return (x1 < (x2+w2)) & ((x1 + w1)>x2) & \
        (y1 < (y2+h2)) & ((y1+h1)>y2)

def alien_coll(a):
    x1 = PX - HERO_C[0]
    y1 = PY - HERO_C[1]
    w1 = HERO_C[0]*2
    h1 = HERO_C[1]*2

    w2 = ALIEN[3]
    h2 = ALIEN[4]
    x2 = x2tl(a[0], w2)
    y2 = y2tl(a[1], h2)

    return hit2(x1, y1, w1, h1, x2, y2, w2, h2)

def scan_alien(x, y, aa):
    if insidexy(x, y) == 0:
        return 0
    a = ALIENS
    ae = ALIENS + {ALIENS_SIZE}
    w = ALIEN[3]
    h = ALIEN[4]
    while a < ae:
        if (a[2]!=0) & (aa != a) & hit1(x2tl(a[0], w), y2tl(a[1], h), w, h, x, y):
            return a
        a += {ALIEN_SIZE}
    return 0

def alien_can_move(a, dir):
    xc = x2c(a[0]) + DIRS[dir*2]
    yc = y2c(a[1]) + DIRS[dir*2+1]

    if oblock(xc, yc):
        return 0

    aa = scan_alien(c2x(xc), c2y(yc), a)
    if aa:
        return 0
    return 1

def alien_sight(x, y, tx, ty):
    if (x2c(x) != x2c(tx)) & (y2c(y) != y2c(ty)):
        return 0;
    return light_ray(x2c(x), y2c(y), x2c(tx), y2c(ty), {W})

try_dirsl = [0, -1, 2, 1]
try_dirsr = [0, 1, -2, -1]

def upd_alien(a):
    if bit(a[2], {ALIEN_DEAD}):
        e = bit_gethi(a[2], {ALIEN_MASK}) - 4
        a[2] = bit_sethi(a[2], {ALIEN_MASK}, e)
        if e <= 0:
            a[2] = 0
            ALIENS_NR -= 1
            EXPLODE_MODE += 1
            SPAWN_FRAME = FRAMES
        return

    dir = a[2]&0x3

    x = a[0]
    y = a[1]

    aligned_x = ((x - {TW//2}) & {TWM}) == 0
    aligned_y = ((y - {TH//2}) & {THM}) == 0
    aligned = aligned_x & aligned_y

    ttl = (a[2]&0xf0)>>4

    if (ttl > 0) & aligned:
        ttl = ttl - 1

    if (HERO_DEAD == 0) & alien_sight(x, y, PX, PY):
        a[2] |= {ALIEN_SIGHT}
    else:
        a[2] &= ~{ALIEN_SIGHT}

    if aligned & bit(a[2], {ALIEN_SIGHT}):
        if (x>>{TWS}) == (PX>>{TWS}):
            if PY > y:
                dir = 3
            else:
                dir = 1
        else:
            if PX > x:
                dir = 0
            else:
                dir = 2
        ttl = 7

    t = 0

    if rnd()&1:
        try_dirs = try_dirsl
    else:
        try_dirs = try_dirsr

    while (aligned) & (t < 4) & (alien_can_move(a, dir) == 0):
        dir += try_dirs[t]
        dir &= 0x3
        t += 1

    dl = (dir + 1)&0x3
    dr = (dir + 3)&0x3
    if (rnd() & 1):
        {mswap("dl", "dr")}
    escape = bit(a[2], {ALIEN_HIT})
    if max(abs(a[0]-PX), abs(a[1]-PY)) < 2*{TW}:
        escape = 0
    if (((ttl == 0)|escape)) & aligned & (t == 0):
        if (alien_can_move(a, dl) == 1):
            dir = dl
            ttl = 4
        elif (alien_can_move(a, dr) == 1):
            dir = dr
            ttl = 4

    if check_laser_trap(x, y, ALIEN[3]>>1, ALIEN[4]>>1):
        alien_hit_laser(a)

    if (t != 4):
        aa = scan_alien(x, y, a)
        nx = x + DIRS[dir*2]
        ny = y + DIRS[dir*2+1]
        if ((aa == 0) | (aa > a)):
            if (check_laser_active(x2c(nx), x2c(ny)) == 0) | bit(a[2], {ALIEN_HIT}):
                x = nx
                y = ny

    a[2] &= ~0xf3
    a[2] |= dir | (ttl << 4)
    a[0] = x
    a[1] = y

    if (HERO_DEAD == 0) & (alien_coll(a)==1):
        HERO_DEAD = 1
        kbd_clear()

    if insidexy(x, y):
        if (RADAR_MODE == 480) & (alien_visible(a) == 0):
            msetxy(RADAR_MAP, x, y, 1)
    return

def upd_aliens():
    if RADAR_MODE == 480:
        bzero(RADAR_MAP, {H})

    if ALIENS_NR < SPAWNS_NR:
        spawn_alien()

    a = ALIENS
    ae = ALIENS + {ALIENS_SIZE}

    if ALIENS_NR > 0:
        a = ALIENS
        while a < ae:
            if a[2] != 0:
                upd_alien(a)
            a += {ALIEN_SIZE}
        return

def check_laser_active(xc, yc):
    o = oget(xc, yc)
    if otype(o, {OB_LASER}) == 0:
        return 0
    if bit(o, {OB_SECRET}):
        return 1
    hor = (laser_hor(xc, yc)==1)
    if hor:
        d = yc&1
    else:
        d = xc&1
    return rate_shift({LASERS_RATE}, d*{LASERS_SHIFT})

def check_laser_trap(x, y, w, h):
    xc = x2c(x)
    yc = y2c(y)
    if check_laser_active(xc, yc):
       hor = laser_hor(xc, yc)
       if (hor==0) & (abs((x&{TWM})-{TW//2}) < w):
           return 1
       elif (hor==1) & (abs((y&{THM})-{TH//2}) < h):
           return 1
    return 0

def upd_hero():
    if HERO_DEAD > 0:
        HERO_DEAD = min(HERO_DEAD + 1, 0x1000)

        if INP_A & (HERO_DEAD>100):
            kbd_clear()
            SCROLL_MODE = - 480
        return

    if RADAR_MODE > 0:
        POWER_DRAW = min(POWER_DRAW + {RADAR_COST}, {POWER_DRAW_MAX})
        if POWER_DRAW >= {POWER_DRAW_MAX}:
            RADAR_MODE = 0
        else:
            RADAR_MODE -= 8

    if INP_C & (INP_A | INP_B):
        if INP_B:
            LEVEL_NR -= 1
        else:
            LEVEL_NR += 1
        kbd_clear()

        if (LEVEL_NR >= {LEVELS_NR}) | (LEVEL_NR < 0):
            setup()
            loadlev()
            return
        NEXT_LEVEL = LEVELS + LEVELS_DIR[LEVEL_NR]
        SCROLL_MODE = -480
        return

    if INP_B & (RADAR_MODE == 0):
        INP_B = 0
        RADAR_MODE = 480

    ox = PX
    oy = PY
    if map_coll(PX+INP_X, PY, 4, 10) == 0:
        PX = PX + INP_X
    if map_coll(PX, PY+INP_Y, 4, 10) == 0:
        PY = PY + INP_Y
    if (INP_X > 0) & ((HERO_DIR == 2) | (INP_Y == 0)):
        HERO_DIR = 0
    elif (INP_X < 0) & ((HERO_DIR == 0) | (INP_Y == 0)):
        HERO_DIR = 2
    elif (INP_Y > 0) & ((HERO_DIR == 1) | (INP_X == 0)):
        HERO_DIR = 3
    elif (INP_Y < 0) & ((HERO_DIR == 3) | (INP_X == 0)):
        HERO_DIR = 1

    if insidexy(PX, PY) == 0:
        return

    if check_laser_trap(PX, PY, 6, 9):
           HERO_DEAD = 1
           return
    o = ogetxy(PX, PY)
    if otype(o, {OB_PAD}):
        oclrxy(PX, PY)
        PADS_NR -= 1
        POWER_DRAW = 0
        EXPLODE_MODE += 1
    elif exit_activated() & atexitxy(PX, PY):
        LEVEL_NR += 1
        NEXT_LEVEL = LEVELS + LEVELS_DIR[LEVEL_NR]
        SCROLL_MODE = -480
        return
    elif otype(o, {OB_TRAP}):
        traps = LEVEL + (o&0xff) + {LEVEL_HEADER}
        while traps[0]&0xff00:
            oclr(int2cx(traps[0]), int2cy(traps[0]))
            traps += 1

    if (o == {OB_SPAWN}) & (obxy(ox, oy, {OB_SPAWN}) != 1) & (SPAWNS_NR > 1):
        i = 0
        cx = x2c(PX)
        cy = y2c(PY)
        while i < SPAWNS_NR:
            spawn = SPAWNS[i]
            i += 1
            if c2int(cx, cy) == (spawn&0xff):
                if i == SPAWNS_NR:
                    i = 0
                spawn = SPAWNS[i]
                PX = c2x(int2cx(spawn))
                PY = c2y(int2cy(spawn))
                TELEPORT_FRAME = FRAMES
                return

EXPLODE_MODE = 0
TITLE_MODE = 0

def update():
    kbd_proc()
    EXPLODE_MODE = 0
    SHAKE_MODE = 0
    if SCROLL_MODE > 0:
        SCROLL_MODE -= 16
        return
    elif SCROLL_MODE < 0:
        SCROLL_MODE += 16
        if SCROLL_MODE >= 0:
            TITLE_MODE = 0
            SCROLL_MODE = 480
            LEVEL = NEXT_LEVEL
            loadlev()
        return
    elif TITLE_MODE > 0:
        TITLE_MODE = min(TITLE_MODE+1, 512)
        if INP_A:
            kbd_clear()
            SCROLL_MODE = -480
        return
    elif ENDING_MODE > 0:
        ENDING_MODE = min(ENDING_MODE+1, 10000)
        return

    upd_laser()
    upd_obs()
    upd_aliens()
    upd_hero()

ALIEN_COLS = [0,0,0,0,0]
SCROLL_MODE = 0

def setup():
    TITLE_MODE = 1
    LEVEL_NR = 0
    LEVEL = LEVELS + LEVELS_DIR[LEVEL_NR]
    NEXT_LEVEL = LEVEL
    i = 0
    while i < {len(ALIEN)}:
        ALIEN_COLS[i] = ALIEN[i*{RECT_SIZE}+5]
        i += 1

def screen_off(ox, oy):
    ptr = {RECT_MEM} #+ {RECT_SIZE} # skip bg
    if ptr[0] & (SCROLL_MODE ==0):
#        ptr[2] += oy
        ptr += {RECT_SIZE}
    eptr = {RECT_MEM} + {RECT_NUM}*{RECT_SIZE}
    while ptr < eptr:
        if ptr[0]:
            ptr[1] += ox
            ptr[2] += oy
        ptr += {RECT_SIZE}

def exit_activated():
    return (PADS_NR == 0) & (PADS_MAX > 0)

def draw_status(ptr):
    if SCROLL_MODE != 0:
        return ptr

    l = {POWER_DRAW_MAX} - POWER_DRAW

    ptr = draw_rect(ptr, {640-STATUS_W}, 0,
        {STATUS_W}, l, rgb(min(128+(l>>2), 255), 32, 0))
    if exit_activated():
        l = 480
    else:
        l = (PADS_MAX - PADS_NR) * DIV
    if l >= 480:
        col = rate_color(2, {rgb(0, 32, 255)}, {rgb(0, 212, 255)})
    else:
        col = rgb(0, 32, min(128+(l>>2), 255))
    ptr = draw_rect(ptr, 0, 0, {STATUS_W}, l, col)
    return ptr

RADAR_MODE = 0

current_zoom = {1 << ZOOM_BITS}

def zoom(start, end, factor):
    while start < end:
        start[{RECT_X}] = shra(start[{RECT_X}] * factor, {ZOOM_BITS})
        start[{RECT_Y}] = shra(start[{RECT_Y}] * factor, {ZOOM_BITS})
        start[{RECT_W}] = (start[{RECT_W}] * factor) >> {ZOOM_BITS}
        start[{RECT_H}] = (start[{RECT_H}] * factor) >> {ZOOM_BITS}
        start[{RECT_W}] += (factor > 1<<{ZOOM_BITS})
        start[{RECT_H}] += (factor > 1<<{ZOOM_BITS})

        start += {RECT_SIZE}

def zoomx(start, end, factor, bits):
    while start < end:
        start[{RECT_W}] = (start[{RECT_W}] * factor) >> bits
        start += {RECT_SIZE}

def set_rect(ptr, x, y, w, h):
    ptr[1] = x
    ptr[2] = y
    ptr[3] = w
    ptr[4] = h

def draw_stars(ptr):
    memcpy(ptr, STARS, {len(STARS)})
    i = 0
    while i < {len(STARS)}:
        v = abs(16 - (((FRAMES+i)&0x1f)))
        x = ptr[i+1]
        y = ptr[i+2]
        set_rect(ptr+i, x, y-(v>>1), 1, v)

        i += {RECT_SIZE}
        ptr[i] = 1
        set_rect(ptr+i, x-(v>>1), y, v, 1)
        i += {RECT_SIZE}

    return ptr + {len(STARS)}

def draw_ending(ptr):
    frame1 = 200
    if ENDING_MODE > frame1:
        draw_rect(ptr, 0, 0, 640, 480, 0xffff)
        if ENDING_MODE > frame1+64:
            v = 240 - min(ENDING_MODE - (frame1+64), 119)*2
            ptr[2] = 240-v
            ptr[4] = v*2
            if ENDING_MODE > frame1+64+120:
                c = max(0, 255 - (ENDING_MODE-(frame1+64+120)))
                ptr[5] = rgb(c, c, c)
                v = 320 - min(ENDING_MODE - (frame1+64+120), 159)*2
                ptr[1] = 320 - v
                ptr[3] = v*2
            if (ENDING_MODE > frame1+64+120+160+128):
                setup()
                loadlev()
        return ptr + {RECT_SIZE}
    ptr = draw_stars(ptr)
    memcpy(ptr, ASTEROID, {len(ASTEROID)})
    ptr[1] += 306
    ptr[2] += 183
    eptr = ptr + {len(ASTEROID)}
    a = (min(ENDING_MODE, 128)>>2)
    chance = (rnd()&0x1f) <= a
    if ENDING_MODE > frame1+32:
        pass
    elif ENDING_MODE > 64:
        ptr[1] ^= rnd()&1
        ptr[2] ^= rnd()&1
    while ptr < eptr:
        if ENDING_MODE > frame1:
          v = min(ENDING_MODE - 128, 31)*8
          ptr[5] = rgb(v, v, v)
        elif chance:
          ptr[5] = 0xffff
        ptr += {RECT_SIZE}
    ptr = eptr
    return ptr

def draw_title(ptr):
    ptr = draw_stars(ptr)
    memcpy(ptr, TITLE, {len(TITLE)})
    ptr[1] += 147
    ptr[2] += 79
    zoomx(ptr, ptr + {len(TITLE)}, min((TITLE_MODE), 128), 7)
    ptr += {len(TITLE)}
    memcpy(ptr, ASTEROID, {len(ASTEROID)})
    ptr[1] += 306
    ptr[2] += 283
    ptr += {len(ASTEROID)}
    return ptr

def zoom_mode():
    target_z = {2 << ZOOM_BITS}
    if ((RADAR_MODE != 0) | INP_STATE[{KEY_B}]) | (HERO_DEAD > 0) | (SCROLL_MODE > 0):
        target_z = {1 << ZOOM_BITS}
    if current_zoom < target_z:
        current_zoom += 1
    if current_zoom > target_z:
        current_zoom -= 1
    if SCROLL_MODE == 0:
        zoom({rect[1].addr}, {RECT_MEM + (RECT_NUM - (1)) * RECT_SIZE}, current_zoom)
    else:
        zoom({rect[0].addr}, {RECT_MEM + (RECT_NUM - (0)) * RECT_SIZE}, current_zoom)
    ox = 240 - shra(PX * current_zoom, {ZOOM_BITS})
    oy = 240 - shra(PY * current_zoom, {ZOOM_BITS})
    screen_off(ox, oy)

def draw():
    ptr = {RECT_MEM}
    bzero(ptr, {RECT_SIZE}*{RECT_NUM})
    if TITLE_MODE:
        ptr = draw_title(ptr)
        if SCROLL_MODE < 0:
            screen_off(0, -SCROLL_MODE-480)
        return
    elif ENDING_MODE:
        ptr = draw_ending(ptr)
        return

    if SCROLL_MODE == 0:
        ptr = draw_rect(ptr, 0, 0, 640, 480, FILL)

    ptr = draw_rect(ptr, PX-{TW}*{VIEW_R}, PY-{TH}*{VIEW_R}, {VIEW_SIZE-1}*32, {VIEW_SIZE-1}*32, BG)

    ptr = draw_map(ptr, PX, PY)
    ptr = draw_hero(ptr, PX, PY)
    ptr = draw_laser(ptr)
    ptr = draw_aliens(ptr)

    if (RADAR_MODE > 0):
        ptr = draw_radar(ptr, 480 - RADAR_MODE)

    {ZOOM_MODE_ENABLED}
    dx = 0
    dy = 0
    if SHAKE_MODE > 0:
        dx = 0x1 - (rnd()&0x3)
        dy = 0x1 - (rnd()&0x3)
    if SCROLL_MODE < 0:
        screen_off(((640-{W*TW})>>1)+dx, -SCROLL_MODE-480+dy)
    else:
        screen_off(((640-{W*TW})>>1)+dx, SCROLL_MODE+dy)

    if (RADAR_MODE > 0):
        ptr = draw_rect(ptr, 0, 480 - RADAR_MODE, 640, 1, rate_color(3, rgb(255,0,0), rgb(128, 128, 128)))

    ptr = draw_status(ptr)

def main():
    setup()
    loadlev()
    while 1:
        update()
        draw()
        wait()
        FRAMES += 1
