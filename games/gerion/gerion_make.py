#!/usr/bin/env python3
from brus16 import *
ZOOM_MODE_ENABLED = "zoom_mode()"

def mswap(a, b):
    return f'''{a} ^= {b}; {b} ^= {a}; {a} ^= {b}'''

def mbool(a):
    return a != 0

ZOOM_BITS = 4
STATUS_W = 10
VIEW_SIZE = 7
VIEW_R = (VIEW_SIZE//2)
#MRECT = [0]*(VIEW_SIZE*VIEW_SIZE)

KEY_STATE = [-1]*KEY_NUM
SPAWN_DELAY = 100
# r, u, l, d
DIRS = [1, 0, 0, -1, -1, 0, 0, 1]

# fire points: r, u, l, d
HERO_LASER_DIR = [10, -3, 4, -10, -10, -4, -4, 6]

POWER_DRAW_MAX = 480
LASER_COST = 16
RADAR_COST = 9
POWER_CHARGE = 8
POWER_CHARGE_MOVE = 4 #POWER_CHARGE//5

# center
HERO_C = [4, 6]

RADAR_RATE = 5
LASERS_RATE = 6
LASERS_SHIFT = 64

BGCOL1 = rgb(50, 0, 80)
BGCOL2 = rgb(100, 0, 130)
FGCOL = rgb(200, 0, 255)
DOTS_RATE = 6

EXITCOL1 = rgb(65,105,225) #rgb(164, 32, 164)
EXITCOL2 = rgb(34,113,179) #rgb(164, 0, 164)

EXITCOL3 = rgb(65,105,225)#rgb(125, 249, 255)
EXITCOL4 = rgb(164, 0, 164)#rgb(164, 0, 164)
EXITCOL_RATE = 3

PADCOL1 = rgb(245, 222, 179)
PADCOL2 = rgb(255, 248, 220)
PADCOL_RATE = 2

LASERCOL_RATE = 1
LASERCOL1 = rgb(0, 191, 255)
LASERCOL2 = rgb(255, 255, 255)

SPAWNCOL1 = rgb(200, 0, 22)
SPAWNCOL2 = rgb(240, 255, 255)
SPAWNCOL_RATE = 1

BTNCOL1 = rgb(0xBFAA30)
BTNCOL2 = rgb(0xDAD871)
BTN_RATE = 4

DOORCOL = rgb(41,132,159)
DOORCOL_BOSS = rgb(0xBF3330)

TITLE = [
    1, 0, 0, 15, 100, rgb(0x70a4b2),
    0, 15, 0, 14, 5, rgb(0x70a4b2),
    0, 29, 0, 15, 20, rgb(0x70a4b2),
    0, 60, 0, 44, 100, rgb(0x70a4b2),
    0, 75, 5, 14, 22, rgb(0x000000),
    0, 75, 34, 14, 61, rgb(0x000000),
    0, 89, 20, 15, 21, rgb(0x000000),
    0, 120, 0, 15, 100, rgb(0x70a4b2),
    0, 135, 0, 14, 5, rgb(0x70a4b2),
    0, 149, 0, 15, 59, rgb(0x70a4b2),
    0, 149, 59, 7, 7, rgb(0x70a4b2),
    0, 142, 66, 7, 7, rgb(0x70a4b2),
    0, 180, 0, 15, 100, rgb(0x70a4b2),
    0, 195, 27, 7, 7, rgb(0x70a4b2),
    0, 202, 20, 7, 7, rgb(0x70a4b2),
    0, 209, 0, 15, 100, rgb(0x70a4b2),
    0, 240, 0, 44, 100, rgb(0x70a4b2),
    0, 255, 5, 14, 90, rgb(0x000000),
    0, 300, 0, 15, 100, rgb(0x70a4b2),
    0, 315, 27, 14, 7, rgb(0x70a4b2),
    0, 329, 0, 15, 100, rgb(0x70a4b2),
    0, 0, 10, 344, 2, rgb(0x000000),
    0, 0, 88, 344, 2, rgb(0x000000),
]

ASTEROID = [
    1, 0, 0, 63, 16, rgb(0x6c5eb5),
    0, 0, -5, 42, 10, rgb(0x70a4b2),
    0, 22, -5, 10, 10, rgb(0x6c5eb5),
    0, -16, 5, 16, 10, rgb(0x70a4b2),
    0, 42, 9, 5, 5, rgb(0x325a67),
    0, -22, 15, 6, 10, rgb(0x70a4b2),
    0, 42, 16, 31, 42, rgb(0x325a67),
    0, -16, 15, 68, 10, rgb(0x6c5eb5),
    0, -28, 25, 70, 23, rgb(0x6c5eb5),
    0, 14, 12, 13, 13, rgb(0x70a4b2),
    0, 8, 25, 13, 13, rgb(0x70a4b2),
    0, 21, 25, 13, 13, rgb(0x325a67),
    0, -11, 32, 5, 5, rgb(0x70a4b2),
    0, -6, 32, 5, 5, rgb(0x325a67),
    0, 21, 48, 26, 21, rgb(0x325a67),
    0, -32, 48, 68, 11, rgb(0x6c5eb5),
    0, -37, 59, 58, 20, rgb(0x6c5eb5),
    0, -16, 54, 5, 5, rgb(0x70a4b2),
    0, -11, 48, 11, 11, rgb(0x325a67),
    0, 4, 49, 11, 4, rgb(0x325a67),
    0, -21, 59, 15, 9, rgb(0x325a67),
    0, -32, 67, 5, 5, rgb(0x325a67),
    0, 0, 69, 21, 10, rgb(0x325a67),
    0, -32, 79, 69, 16, rgb(0x325a67),
    0, -22, 95, 43, 6, rgb(0x325a67),
    0, 37, 74, 10, 10, rgb(0x325a67),
    0, 54, 67, 10, 10, rgb(0x325a67),
    0, 58, 26, 15, 21, rgb(0x000000),
    0, 47, 37, 21, 26, rgb(0x000000),
    0, 31, 63, 16, 6, rgb(0x000000),
    0, -1, 84, 22, 11, rgb(0x000000),
]

STARS = [
    1, 56, 415, 2, 20, rgb(0x6c5eb5),
    0, -9, 9, 20, 2, rgb(0x6c5eb5),
    1, 146, 323, 2, 20, rgb(0x6c5eb5),
    0, -9, 9, 20, 2, rgb(0x6c5eb5),
    1, 424, 227, 2, 20, rgb(0x6c5eb5),
    0, -9, 9, 20, 2, rgb(0x6c5eb5),
    1, 527, 368, 2, 20, rgb(0x6c5eb5),
    0, -9, 9, 20, 2, rgb(0x6c5eb5),
    1, 575, 57, 2, 20, rgb(0x6c5eb5),
    0, -9, 9, 20, 2, rgb(0x6c5eb5)
]

ALIEN = [
    1, 0, 0, 24, 18, 0,
    0, 8, 6, 8, 2, rgb(255,0,0),
    0, 3, 18, 4, 6, 0,
    0, 10, 18, 4, 6, 0,
    0, 18, 18, 4, 6, 0,
]

OBS_MAX = 64
OBS_SIZE = 2
ALIENS_MAX = 8
SPAWNS_MAX = 8

ALIEN_SIZE = 3
ALIENS_SIZE = ALIENS_MAX*ALIEN_SIZE
ALIENS = [0]*ALIENS_SIZE
OBS = [0]*OBS_MAX*OBS_SIZE
SPAWNS = [0]*SPAWNS_MAX
SPAWN_BOSS = 0x8000

c1 = rgb(211, 211, 211)
c2 = rgb(192, 192, 192) # legs
c3 = rgb(162,173,208)#rgb(157,177,204) #(169, 169, 169) # pack
c4 = rgb(24, 24, 24)

HERO = [
    1, 0, 0, 8, 10, c1,
    0, -3, 1, 3, 8, c3,
    0, 3, -4, 6, 6, rgb(255, 255, 255),
    0, 6, -3, 3, 4, rgb(0, 190, 222),
    0, 1, 10, 3, 7, c2,
    0, 5, 10, 3, 7, c2,
    0, 3, 3, 11, 3, c4,
    0, 6, 6, 3, 2, rgb(255, 255, 255),
]

HEROU = [
    1, 0, 0, 8, 10, c1,
    0, 1, -4, 6, 6, rgb(255, 255, 255),
    0, 1, 2, 7, 7, c3,
    0, 8, -5, 2, 8, c4,
    0, 1, 10, 3, 7, c2,
    0, 5, 10, 3, 7, c2,
    0, 8, 3, 3, 3, rgb(235, 235, 235),
    0, 1, 2, 6, 1, rgb(160, 160, 160),
]

HEROD = [
    1, 0, 0, 8, 10, c1,
    0, 1, -4, 6, 6, rgb(255, 255, 255),
    0, 1, -2, 6, 3, rgb(0, 190, 222),
    0, -2, 3, 3, 5, rgb(235, 235, 235),
    0, 1, 10, 3, 7, c2,
    0, 5, 10, 3, 7, c2,
    0, 0, 4, 2, 8, c4,
    0, 3, 5, 5, 3, rgb(173, 173, 173),
]

def invertx(t, l):
    i = 0
    r = [1, 0, 0]
    dx = 0
    while i < l:
        if i == 0:
            r.append(t[i+3])
            r.append(t[i+4])
            r.append(t[i+5])
            dx = t[i+3]
        else:
            r.append(0)
            x, w = t[i+1], t[i+3]
            if x >= 0:
                r.append(-x+dx-w)
                r.append(t[i+2])
                r.append(w)
                r.append(t[i+4])
            else:
                r.append(dx-x-w)#-x+w)
                r.append(t[i+2])
                r.append(w)
                r.append(t[i+4])
            r.append(t[i+5])
        i += RECT_SIZE
    return r

HEROL = invertx(HERO, len(HERO))

TW = 32
TH = 32

TWS = 5
THS = 5

TWM = 0x1f
THM = 0x1f

W = 15
H = 15

OBJS = [0]*(W*H)

RADAR_MAP = [0]*H

DOOR_H = 0x1
LASER_H = 0x1

OB_H      = 0x4000
OB_SECRET = 0x2000
OB_BOSS   = 0x8000

OB_OBSTACLE  = 0x1000
OB_WALL      = OB_OBSTACLE
OB_PAD       = 0x0100
OB_ALIEN     = 0x0200
OB_DOOR      = 0x0300|OB_OBSTACLE
OB_REACTOR   = 0x0400|OB_OBSTACLE
OB_LASER     = 0x0500
OB_SPAWN     = 0x0600
OB_TRAP      = 0x0700
OB_MASK      = 0x1f00

ALIEN_DEAD =  0x2000
ALIEN_HIT =   0x4000
ALIEN_SIGHT = 0x8000
ALIEN_BOSS  = 0x0004
ALIEN_MASK =  0x1F00
ALIEN_HEALTH = 0x16

OBS_HIT    = 0x8000
OBS_DEAD   = 0x4000
OBS_MASK   = 0x1F00

DOOR_SECRET = 0x2000
DOOR_HEALTH = 0x19

R_HEALTH = 0x1f

LEVEL_HEADER = H + 5

def debug(text):
    code = []
    for c in text:
        code.append(f'poke(-1, {ord(c)})')
    return ';'.join(code)

# # - wall
# @ - hero
# E - exit
# % - door
# ? - secret door
# * - power cell
# $ - alien
# ! - boss alien
# & - spawn
# B - boss spawn
# R - reactor
# / - laser
# ^ - boss laser (use trap/btn)
# + - boss door (use trap/btn)
# fg:r,g,b - foreground
# bg:r,g,b - backround
# fill:r,g,b - fill color
# trap:abc - a - trigger symbol, b - target symbol, c - item symbol
# btn:abc - same as trap, but visible
# press C+A - next level
# press C+B - prev level ;)

MAP = (
# 1
'''
###############
#@   %   %   *#
####### #######
####### #######
####### #######
####### #######
######   ######
#*$ %  E  %  *#
######   ######
####### #######
######   ######
###### * ######
######   ######
###############
###############''',

# 2
# trap:{}#

'''
trap:{}#
fg:0,0,0
###############
#$           @#
# ###%#####%###
# ##$* ### *$##
# #############
# #############
# ####   ######
#      E      #
#{####   ####{#
# ########### #
#*?    /    ?*#
#}###########}#
#$     }     $#
###############
###############''',

# 3
'''
###############
#######@#######
####### #######
#####*   *#####
# ##### ##### #
# #####%##### #
# ####   #### #
#             #
# ####   #### #
# #####%##### #
#*##### #####*#
####### #######
####### #######
#####*   *#####
#######&#######''',

# 4

'''
fg:#CEB7A6
bg:#2F435A
fill:#000000
btn:{}^
btn:zZ^
###############
#*###&   &###*#
# #####z##### #
# ##### ##### #
#}##### #####}#
# ##### ##### #
# ####   #### #
#      @      #
# ####   #### #
#%#####%#####%#
#             #
# #####Z##### #
# #*   {   *# #
# ########### #
#             #''',

# 5
'''
fg:0,47,85
bg:0,0,0
fill:0,0,0
###############
###############
*      *      *
               
$             $
               
               
@      E      *
               
               
$             $
               
*      *      *
###############
###############''',

#6
'''
fg:255,128,0
###############
#   %  $     *#
# @ #########%#
#   ######### #
##%#### ##*   #
## #### #####$#
##$###   #### #
##     E   ## #
## ###   #### #
## #### ##### #
## #### ##*   #
#   ######### #
# * ######### #
#        $  %$#
###############''',

# 7
'''
fg:#3d3846
bg:#241f31
fill:#241f31
#######&#######
#    *# #*    #
# ##### ##### #
#             #
# ##### ##### #
#*##### #####*#
######? ?######
&      @      &
######? ?######
#*##### #####*#
# ##### ##### #
#             #
# ##### ##### #
#    *# #*    #
#######&#######
''',


# 8
'''
fg:0,128,192
bg:0,200,220
###############
##@#*%   %*#*##
## # ##%## #$##
## #$## ##$# ##
## # ## ## # ##
##$% ## ## %$##
####### #######
#      E      #
####### #######
##$% ## ## %$##
## # ## ## # ##
## #$## ##$# ##
##$# ## ## #$##
##*#*%   %*#*##
###############''',

# 9
'''
.......B.......
 ##%## # ##%##.
 #* *# / #* *#.
 ##### # #####.
......*#*  ....
%#############%
 ###  &#&  ###.
 #*# ##### #*#.
 #     B     #.
 % ######### %.
 # ###   ### #.
.#.....@.....#.
.#####%#%#####.
.    # E #    .
####..*#*..####
''',

# 10
'''
bg:0,47,85
fg:112, 128, 144
fill:0,0,0
#######&#######
#             #
# ##### ##### #
# ####* *#### #
# ##### ##### #
# ##### ##### #
# #*##   ##*# #
&      @      &
# #*##   ##*# #
# ##### ##### #
# ##### ##### #
# ####* *#### #
# ##### ##### #
#             #
#######&#######
''',

# 11
'''
bg:#505050
fg:#a0a0a0
fill:#000000
#####%####%####
#@      $     #
#####%####%##/#
#*???$????$?# #
###########?# #
#         #$% %
#/###%### #?#$#
# ###%### #?# #
%$#######/#$% %
# ###E$ % ??# #
% ######& ### %
# ######&&### #
#/###########/#
#      $      #
#######%#######''',

# 12
'''
fg:#5093CD
bg:#0D1954
fill:#0D1954
. ###&   &### .
. #*?     #*# .
. ### ### #?# .
.     #*#     .
. ### #?# ### .
. ?*#     #*? .
. ### ### ### .
.     #@#     .
. ### #?# #?# .
. #*?     #*# .
. ### ### ### .
.     ?*#     .
. ### ### ### .
. #*?     #*? .
. ###&   &### .
''',

# 13
'''
fg:200,200,160
bg:100,0,100
###############
#@  % ### %  *#
# ### $*$ ###$#
# #####%##### #
#%##### #####%#
#  ####/####  #
##$###   ###$##
##*% / E / %*##
##$###   ###$##
#  ####/####  #
#%##### #####%#
# #####%##### #
#$##  $*$  ##$#
#*%  ##### % *#
###############''',

# 14
'''
fg:#000000
bg:#1a5fb4
fill:#000000
# #### E #### #
#*####   ####*#
# ####   #### #
&      *      &
# ####   #### #
#*####   ####*#
# ####   #### #
###### * ######
# ####   #### #
#*####   ####*#
# ####   #### #
&      *      &
# ####   #### #
#*####   ####*#
# #### @ #### #''',

# 15
'''
B..#...#...#..@
.*./.*./.*./.*.
...#...#...#...
#/###/###/###/#
...#...#...#...
.*./.*./.*./.*.
...#...#...#...
#/###/###/###/#
...#...#...#...
.*./.*./.*./.*.
...#...#...#...
#/###/###/###/#
...#...#...#...
.*./.*./.*./.*..
...#...#...#..B''',

# 16
'''
###############
 @ ####*#### &
#   ###?###   #
##   ##?##   ##
###   #?#   ###
####   ?   ####
#####     #####
#*???? E ????*#
#####     #####
####   ?   ####
###   #?#   ###
##   ##?##   ##
#   ###?###   #
 & ####*#### &.
###############''',

# 17
'''
*      &   @  *
 ######%######.
 #* /     / *#.
 # #### #### #.
 #/#       #/#.
 # # ##%## # #.
 # # #* *# # #.
&%   % E %   %&
 # # #* *# # #.
 # # ##%## # #.
 #/#       #/#.
 # #### #### #.
 #* /     / *#.
 ######%######.
*      &      *
''',
# 18
'''
###############
##  #######  ##
# $ /  @  / $ #
#  ##/#/#/##  #
# ?*#     #*? #
# #####%##### #
# ##### ##### #
# %*$% E %*$% #
# #####!##### #
# #####%##### #
# #*?     ?*# #
#  ##/#/#/##  #
# $ /  *  / $ #
##  #######  ##
###############''',

# 19
'''
fg:0,0,0
#####  @  #####
# * #     # * #
# # #/////# # #
# # #     # # #
# * #     # * #
##%##/////##%##
#   ?     ?   #
# # #/////# # #
#   ?     ?   #
#####/////#####
# * #     # * #
# # #     # # #
# # #/////# # #
# * %     % * #
#####B B B#####
''',

# 20
'''
     #*!*#    B
 ### ## ## ###.
 /*/  # #  /*/.
 #### # # ####.
      #%#     .
##           ##
*#### #.# ####*
!   % .@. %   !
*#### #.# ####*
##           ##
      #%#     .
 #### # # ####.
 /*/  # #  /*/.
 ### ## ## ###.
B    #*!*#    .
''',

# 21
'''
!    #####....!
 ??? #   #.???.
 ?R? ? # ?.?R?.
 ??? # # #.???.
     #   #.....
##?####/####%##
#    #   #    #
# ## / @ / ## #
#    #   #    #
##?####/####?##
     #   #.....
.??? # # # ???.
.?R? % # % ?R?.
.??? #   # ???.
!... ##### ...!''',
)

def parsenumbers(l):
    return map(int, l.strip().split(","))

def parsecolor(l):
    l = l.strip()
    if l.startswith('#'):
        return rgb(int(l[1:], 16))
    r, g, b = parsenumbers(l)
    return rgb(r, g, b)

# trap:{}%
def parsetrap(l):
    l = l.strip()
    a = l[0:1]
    b = l[1:2]
    t = l[2:3]
    return { 'src':a, 'dst':b, 'o':t, 'where': [], 'list': [], "secret": False }

def mget(m, cx, cy):
    if cx < 0 or cx >= W:
        return False
    if cy < 0 or cy >= H:
        return False
    return (m[cy]&(1<<cx)) != 0

def map2bit(t):
    r = []
    traps = { "src": {}, "dst": {}, "list": [] }
    lasers = []
    items = []
    x, y = 0, 0
    px, py = 0, 0
    ex, ey = -1, -1
    fg = FGCOL
    fill = BGCOL1
    bg = BGCOL2
    div = 480 // (t.count('*') + t.count('R'))
    for l in t.splitlines():
#        l = l.strip()
        if l == "":
            continue
        elif l.startswith("fg:"):
            fg = parsecolor(l[3:])
            continue
        elif l.startswith("bg:"):
            bg = parsecolor(l[3:])
            continue
        elif l.startswith("fill:"):
            fill = parsecolor(l[5:])
            continue
        elif l.startswith("trap:"):
            trap = parsetrap(l[5:])
            trap["secret"] = True
            traps["src"][trap['src']] = trap
            traps["dst"][trap['dst']] = trap
            traps["list"].append(trap)
            continue
        elif l.startswith("btn:"):
            trap = parsetrap(l[4:])
            traps["src"][trap['src']] = trap
            traps["dst"][trap['dst']] = trap
            traps["list"].append(trap)
            continue
        c = 0
        las = 0
        x = 0
        for i in l:
            c >>= 1
            las >>= 1
            if i in traps["src"]:
                t = traps["src"][i]
                i = '.'
                t["where"].append((x, y))
            elif i in traps["dst"]:
                t = traps["dst"][i]
                i = t['o']
                t["list"].append((x, y))
            c |= 0x8000 if i == '#' else 0
            if i == '@':
                px, py = x, y
            elif i == 'E':
                ex, ey = x, y
            elif i == '*':
                items.append((x, y, OB_PAD))
            elif i == '&':
                items.append((x, y, OB_SPAWN))
            elif i == 'B':
                items.append((x, y, OB_SPAWN | OB_BOSS))
            elif i == '$':
                items.append((x, y, OB_ALIEN))
            elif i == '!':
                items.append((x, y, OB_ALIEN | OB_BOSS))
            elif i == '%':
                items.append((x, y, OB_DOOR))
            elif i == '?':
                items.append((x, y, OB_DOOR | OB_SECRET))
            elif i == 'R':
                items.append((x, y, OB_REACTOR))
            elif i == '/':
                items.append((x, y, OB_LASER))
                las |= 0x8000
            elif i == '+':
                items.append((x, y, OB_DOOR | OB_BOSS))
            elif i == '^':
                items.append((x, y, OB_LASER | OB_SECRET))
                las |= 0x8000
            x += 1
        r.append(c>>1)
        lasers.append(las>>1)
        y += 1
    if ex < 0:
        ex, ey = px, py
    r.append((py<<4)|px|(ey<<12)|(ex<<8))
    r.append(fg)
    r.append(bg)
    r.append(fill)
    r.append(div)

    for v in traps["list"]:
        fl = v["secret"] and OB_SECRET or 0
        for w in v['where']:
            r.append(w[0]|(w[1]<<4)| OB_TRAP | fl)
            for t in v["list"]:
                r.append(t[0]|(t[1]<<4)| OB_TRAP)
            r.append(0xff)

    for i in items:
        fl = 0
        if (i[2]&OB_MASK) == OB_DOOR:
            if mget(r, i[0] + 1, i[1]) or mget(r, i[0] - 1, i[1]):
                fl |= OB_H
        elif (i[2]&OB_MASK) == OB_LASER:
            if mget(lasers, i[0] + 1, i[1]) or mget(lasers, i[0] - 1, i[1]):
                fl |= OB_H
            elif mget(lasers, i[0], i[1]-1) or mget(lasers, i[0], i[1]+1):
                fl |= 0
            elif mget(r, i[0] + 1, i[1]) or mget(r, i[0] - 1, i[1]):
                fl |= OB_H
        r.append(i[0]|(i[1]<<4)|i[2]|fl)
    r.append(0) # end
    return r

LEVELS = []
LEVELS_DIR = [0]
LEVELS_NR = 0
for m in MAP:
    LEVELS += map2bit(m)
    LEVELS_DIR.append(len(LEVELS))
    LEVELS_NR += 1

SFX_POS = 0
SFX_COUNT = 1
SFX_LOOP = 2
SFX_SIZE = 3
SFX_DATA = 4

SFX_RADAR = [33792, 1, 1783, 3277, 32333, 0, 1014, 1024, 32333, 0, 1027, 1024, 32586, 0, 1022, 1024, 32586, 1, 32834, 0, 60]
SFX_LASER = [33808, 1, 446, 3277, 31691, 0, 522, 512, 31691, 0, 4096, 1024, 41, 0, 3072, 102, 28668, 0, 32913, 447, 0, 0]
SFX_PAD = [33568, 1, 1486, 6554, 31691, 0, 8192, 256, 30650, 0, 12493, 51, 30650, 0, 32929, 1337, 0, 2, 32865, 1189, 60]
SFX_DEAD = [33840, 1, 312, 6554, 31691, 0, 1126, 1024, 31691, 0, 1229, 1024, 31691, 0, 1331, 1024, 31691, 0, 32945, 594, 0, 1, 32881, 446, 1, 32881, 297, 1, 32881, 149, 1, 32881, 134, 60]

save_game('gerion.bin', load_code('gerion.py'))
