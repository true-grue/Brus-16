from brus16 import *



BG_COLOR = rgb(0x181c28)


DECOR_COLOR_CITY1  = rgb(0x303040)
DECOR_COLOR_CITY2  = rgb(0x303040)
WINDOW_COLOR_ON    = rgb(0xFFD566)


SNOW_ANIM_DELAY   = 4
WINDOW_ANIM_DELAY = 100
SUN_ANIM_DELAY    = 5
SANDSTORM_ANIM_DELAY = 0

GROUND_Y = SCREEN_H - 32
L1_Y     = SCREEN_H - 120
L2_Y     = SCREEN_H - 208
L3_Y     = SCREEN_H - 296


RECT_NUM = 64



PLATFORM_LEVELS = [

    [
        (40, 360, 560, 8,  rgb(0x2E2A45)),
        (80, 272, 480, 8,  rgb(0x2E2A45)),
        (120, 184, 400, 8, rgb(0x2E2A45)),
        (0,  448, 640, 8,  rgb(0x2E2A45)),
    ],

    [
        (40, 360, 560, 8,  rgb(0x8B5A2B)),
        (80, 272, 480, 8,  rgb(0x8B5A2B)),
        (120,184, 400, 8,  rgb(0x8B5A2B)),
        (0,  448, 640, 8,  rgb(0x8B5A2B)),
    ],

    [
        (40, 360, 560, 8,  rgb(0x162F35)),
        (80, 272, 480, 8,  rgb(0x162F35)),
        (120,184, 400, 8,  rgb(0x162F35)),
        (0,  448, 640, 8,  rgb(0x162F35)),
    ],

    [
        (0,   448, 640, 8,  rgb(0x1E1E1E)),
        (40,  360, 560, 8,  rgb(0x1E1E1E)),
        (80,  272, 480, 8,  rgb(0x1E1E1E)),
        (120, 184, 400, 8,  rgb(0x1E1E1E)),
    ],

    [
        (40, 360, 560, 8,  rgb(0x804020)),
        (80, 272, 480, 8,  rgb(0x804020)),
        (120,184, 400, 8,  rgb(0x804020)),
        (0,  448, 640, 8,  rgb(0x804020)),
    ],

    [
        (40, 360, 560, 12, rgb(0x4F3622)),
        (80, 272, 480, 12, rgb(0x4F3622)),
        (120,184, 400, 12, rgb(0x4F3622)),
        (0,  448, 640, 12, rgb(0x4F3622)),
    ],

    [
        (40, 360, 560, 8,  rgb(0x4A3A2A)),
        (80, 272, 480, 8,  rgb(0x4A3A2A)),
        (120,184, 400, 8,  rgb(0x4A3A2A)),
        (0,  447, 640, 8,  rgb(0x4A3A2A)),
    ],

    [
        (40, 360, 560, 8,  rgb(0x1E2233)),
        (80, 272, 480, 8,  rgb(0x1E2233)),
        (120,184, 400, 8,  rgb(0x1E2233)),
        (0,  448, 640, 8,  rgb(0x1E2233)),
    ],
]

LADDER_LEVELS = [
    # level 1 – город (Level1-final)
    [
        (320, 292, 18, 70,  rgb(0x3EE6FF)),
        (246, 203, 18, 73,  rgb(0x3EE6FF)),
        (480, 305, 18, 144, rgb(0x3EE6FF)),
        (92,  218, 18, 144, rgb(0x3EE6FF)),
        (491, 130, 18, 144, rgb(0x3EE6FF)),
    ],

    # level 2 – пляж (Level2-final (2))
    [
        (209, 339, 18, 87,  rgb(0xA87A3A)),
        (537, 324, 18, 123, rgb(0xA87A3A)),
        (394, 233, 18, 96,  rgb(0xA87A3A)),
        (275, 112, 18, 144, rgb(0xA87A3A)),
        (121, 232, 18, 114, rgb(0xA87A3A)),
    ],

    # level 3 – лес (Level3_final)
    [
        (103, 243, 20, 117, rgb(0x355347)),
        (530, 246, 20, 117, rgb(0x355347)),
        (286, 149, 20, 123, rgb(0x355347)),
        (298, 309, 23, 143, rgb(0x355347)),
    ],

    # level 4 – индустриальный (Level4_final)
    [
        (286, 339, 18, 110, rgb(0x4F3939)),
        (240, 234, 18, 70,  rgb(0x4F3939)),
        (124, 161, 18, 146, rgb(0x4F3939)),
        (275, 143, 18, 74,  rgb(0x4F3939)),
        (525, 217, 18, 143, rgb(0x4F3939)),
        (423, 325, 18, 74,  rgb(0x4F3939)),
        (383, 235, 18, 74,  rgb(0x4F3939)),
        (362, 143, 18, 74,  rgb(0x4F3939)),
    ],

    # level 5 – зима (Level5_final)
    [
        (506, 216, 18, 144, rgb(0xC0C0FF)),
        (267, 115, 18, 88,  rgb(0xC0C0FF)),
        (225, 210, 18, 84, rgb(0xC0C0FF)),
        (387, 320, 18, 128, rgb(0xC0C0FF)),
        (135, 319, 18, 129, rgb(0xC0C0FF)),
        (137, 62,  18, 223, rgb(0xC0C0FF)),
        (352, 226, 18, 88,  rgb(0xC0C0FF)),
        (379, 123, 18, 88,  rgb(0xC0C0FF)),
    ],

    # level 6 – пустыня / каньон (Level6_final (2))
    [
        (327, 115, 18, 112, rgb(0xA06932)),
        (242, 127, 18, 150, rgb(0xA06932)),
        (438, 206, 18, 94,  rgb(0xA06932)),
        (573, 312, 18, 140, rgb(0xA06932)),
        (230, 312, 18, 140, rgb(0xA06932)),
        (402, 245, 18, 140, rgb(0xA06932)),
        (288, 216, 18, 112, rgb(0xA06932)),
    ],

    # level 7 – лава (Level7_final)
    [
        (353, 141, 18, 168, rgb(0x803020)),
        (219, 209, 18, 65,  rgb(0x803020)),
        (151, 234, 18, 145, rgb(0x803020)),
        (319, 318, 18, 43,  rgb(0x803020)),
        (440, 305, 18, 144, rgb(0x803020)),
        (294, 207, 18, 65,  rgb(0x803020)),
        (232, 304, 18, 57,  rgb(0x803020)),
    ],

    # level 8 – космос (Level8_final)
    [
        (324, 307, 18, 142, rgb(0x7A4FFF)),
        (280, 128, 18, 144, rgb(0x7A4FFF)),
        (401, 287, 18, 106, rgb(0x7A4FFF)),
        (361, 118, 18, 97,  rgb(0x7A4FFF)),
        (538, 215, 18, 144, rgb(0x7A4FFF)),
        (195, 284, 18, 97,  rgb(0x7A4FFF)),
        (454, 215, 18, 97,  rgb(0x7A4FFF)),
        (131, 149, 18, 149, rgb(0x7A4FFF)),
    ],
]


PLATFORM_COUNT = max(len(level) for level in PLATFORM_LEVELS)
LADDER_COUNT   = 8

plat_x1 = [0] * PLATFORM_COUNT
plat_x2 = [0] * PLATFORM_COUNT
plat_y  = [0] * PLATFORM_COUNT

lad_x1 = [0] * LADDER_COUNT
lad_x2 = [0] * LADDER_COUNT
lad_y1 = [0] * LADDER_COUNT
lad_y2 = [0] * LADDER_COUNT

PLATFORM_LEVELS_FLAT = []
for level in PLATFORM_LEVELS:
    for (x, y, w, h, color) in level:
        PLATFORM_LEVELS_FLAT.extend([x, y, w, h, color])

    for _ in range(PLATFORM_COUNT - len(level)):
        PLATFORM_LEVELS_FLAT.extend([-1000, 0, 0, 0, BG_COLOR])

LADDER_LEVELS_FLAT = []
for level in LADDER_LEVELS:
    trimmed = level[:LADDER_COUNT]
    for (x, y, w, h, color) in trimmed:
        LADDER_LEVELS_FLAT.extend([x, y, w, h, color])

    for _ in range(LADDER_COUNT - len(trimmed)):
        LADDER_LEVELS_FLAT.extend([-1000, 0, 0, 0, BG_COLOR])

PLATFORM_H     = 8
PLATFORM_COLOR = rgb(0x804020)

PLATFORM_DATA = []
for _ in range(PLATFORM_COUNT):
    PLATFORM_DATA += [1, -1000, 0, 8, PLATFORM_H, PLATFORM_COLOR]

LADDER_W   = 18
LADDER_CLR = rgb(0xC0C0FF)

LADDER_DATA = []
for _ in range(LADDER_COUNT):
    LADDER_DATA += [1, -1000, 0, LADDER_W, 64, LADDER_CLR]




DECOR_COUNT = 32
MENU_HERO_LOCAL_INDICES = []
MENU_MASK_LOCAL_INDICES = []
MENU_WINDOW_LOCAL_INDEX = 0

def pad_decor(lst):
    while len(lst) < DECOR_COUNT:
        lst.append((-1000, 0, 8, 8, BG_COLOR))
    return lst[:DECOR_COUNT]



def make_decor_menu():
    global MENU_HERO_LOCAL_INDICES, MENU_MASK_LOCAL_INDICES, MENU_WINDOW_LOCAL_INDEX

    decor = []
    decor.append((14, 15, 85, 39, rgb(0x11141E)))
    decor.append((18, 20, 8, 30, rgb(0xC0BEBC)))
    decor.append((28, 20, 8, 30, rgb(0xC0BEBC)))
    decor.append((38, 20, 8, 30, rgb(0xC0BEBC)))
    decor.append((48, 20, 8, 30, rgb(0xC0BEBC)))
    decor.append((58, 20, 8, 30, rgb(0xC0BEBC)))
    decor.append((68, 20, 8, 30, rgb(0xC0BEBC)))
    decor.append((78, 20, 8, 30, rgb(0xC0BEBC)))
    decor.append((88, 20, 8, 30, rgb(0xC0BEBC)))
    decor.append((185, 95, 275, 90, rgb(0x11141E)))
    
    # --- стрелка ---
    decor.append((298, 226, 14, 68, rgb(0xC0BEBC)))
    decor.append((310, 232, 15, 56, rgb(0xC0BEBC)))
    decor.append((325, 242, 13, 37, rgb(0xC0BEBC)))
    decor.append((338, 251, 12, 19, rgb(0xC0BEBC)))

    # --- Д ---
    decor.append((190, 100, 40, 80, rgb(0xC0BEBC)))
    decor.append((190, 100, 5, 60, rgb(0x11141E)))
    decor.append((205, 110, 15, 50, rgb(0x11141E)))
    decor.append((200, 170, 20, 10, rgb(0x11141E)))

    # --- О ---
    decor.append((246, 100, 40, 80, rgb(0xC0BEBC)))
    decor.append((256, 110, 20, 60, rgb(0x11141E)))

    # --- Н ---
    decor.append((302, 100, 10, 80, rgb(0xC0BEBC)))
    decor.append((312, 135, 20, 10, rgb(0xC0BEBC)))
    decor.append((332, 100, 10, 80, rgb(0xC0BEBC)))

    # --- К ---
    decor.append((358, 100, 10, 80, rgb(0xC0BEBC)))
    decor.append((368, 135, 25, 10, rgb(0xC0BEBC)))
    decor.append((388, 100, 10, 35, rgb(0xC0BEBC)))
    decor.append((388, 145, 10, 35, rgb(0xC0BEBC)))

    # --- И ---
    decor.append((414, 100, 10, 80, rgb(0xC0BEBC)))
    decor.append((424, 145, 10, 20, rgb(0xC0BEBC)))
    decor.append((434, 135, 10, 20, rgb(0xC0BEBC)))
    decor.append((444, 100, 10, 80, rgb(0xC0BEBC)))

    # ====== ОКНО + ГЕРОИ В МЕНЮ ======

    # окно
    MENU_WINDOW_LOCAL_INDEX = len(decor)
    decor.append((269, 340, 102, 93, rgb(0x11141E)))  # "ОКНО ДЛЯ ДОНКИ И ПРИНЦЕССЫ"

    # список индексов частей героя (донки+принцесса)
    MENU_HERO_LOCAL_INDICES = []

    def add_hero_rect(x, y, w, h, color):
        idx = len(decor)
        decor.append((x, y, w, h, rgb(color)))
        MENU_HERO_LOCAL_INDICES.append(idx)

    # части принцессы и донки (без масок)
    add_hero_rect(361, 384, 5, 15, 0xFFE0C0)  # рука принцессы
    add_hero_rect(316, 366, 7, 15, 0x8C4A00)  # ухо донки
    add_hero_rect(287, 358, 31, 30, 0x8C4A00) # голова донки
    add_hero_rect(281, 389, 40, 40, 0x8C4A00) # тело донки
    add_hero_rect(292, 363, 25, 23, 0xC87A30) # лицо донки
    add_hero_rect(320, 391, 16, 12, 0x753E00) # рука донки
    add_hero_rect(353, 358, 9, 23, 0x804000)  # волосы принцессы
    add_hero_rect(334, 379, 27, 38, 0xFF88CC) # тело принцессы
    add_hero_rect(338, 358, 19, 22, 0xFFE0C0) # голова принцессы
    add_hero_rect(336, 352, 21, 10, 0x804000) # волосы принцессы
    add_hero_rect(337, 344, 17, 6, 0xFFEE44)  # корона принцессы
    add_hero_rect(294, 368, 8, 3, 0x000000)   # глаз донки
    add_hero_rect(308, 368, 8, 3, 0x000000)   # глаз донки
    add_hero_rect(330, 408, 35, 21, 0xFF88CC) # низ платья принцессы
    add_hero_rect(331, 358, 9, 23, 0x804000)  # волосы принцессы
    add_hero_rect(330, 385, 7, 16, 0xFFE0C0)  # рука принцессы
    add_hero_rect(351, 368, 5, 1, 0x000000)   # глаз принцессы
    add_hero_rect(343, 368, 5, 1, 0x000000)   # глаз принцессы
    add_hero_rect(344, 394, 12, 12, 0xDBDBDB) # салфетка
    add_hero_rect(344, 369, 2, 7, 0x94DDFC)   # слеза принцессы
    add_hero_rect(354, 369, 1, 5, 0x94DDFC)   # слеза принцессы
    add_hero_rect(332, 396, 18, 6, 0xFFE0C0)  # рука принцессы
    add_hero_rect(351, 399, 13, 6, 0xFFE0C0)  # рука принцессы
    add_hero_rect(272, 393, 11, 31, 0x753E00) # рука донки
    add_hero_rect(298, 378, 17, 3, 0x000000)  # рот донки
    add_hero_rect(289, 398, 27, 25, 0xC87A30) # живот донки
    add_hero_rect(304, 415, 2, 4, 0x8C4A00)   # живот донки
    add_hero_rect(280, 366, 7, 15, 0x8C4A00)  # ухо донки

    # маски ДОЛЖНЫ идти ПОСЛЕДНИМИ, чтобы перекрывать анимацию
    MENU_MASK_LOCAL_INDICES = []

    left_mask_idx = len(decor)
    decor.append((0, 336, 269, 144, rgb(0x181C28)))
    MENU_MASK_LOCAL_INDICES.append(left_mask_idx)

    right_mask_idx = len(decor)
    decor.append((371, 336, 269, 144, rgb(0x181C28)))
    MENU_MASK_LOCAL_INDICES.append(right_mask_idx)
    
    decor.append((0, 429, 640, 90, rgb(0x181C28)))  # "ОКНО ДЛЯ ДОНКИ И ПРИНЦЕССЫ"

    return decor




def make_decor_final():
    decor = []


    decor.append((0,   0, 640, 480, rgb(0x101820)))
    decor.append((0, 360, 116,   9, rgb(0x3F4138)))
    decor.append((0, 364, 134,  25, rgb(0x3F4138)))
    decor.append((0, 389, 639,  91, rgb(0x40362B)))
    decor.append((0, 400, 640,  60, rgb(0x4F4335)))
    decor.append((0, 421, 640,  59, rgb(0x77644F)))
    decor.append((2, 445, 638,  35, rgb(0x937C62)))


    decor.append((492,   0, 148, 155, rgb(0x012F49)))
    decor.append((522,   1, 118, 123, rgb(0x023D60)))
    decor.append((549,   9,  88,  96, rgb(0x035E94)))
    decor.append((565,  17,  65,  68, rgb(0x048ADB)))
    decor.append((582,  25,  40,  40, rgb(0x0EA2FA)))
    decor.append((591,  32,  24,  24, rgb(0x9DD9FD)))


    decor.append((119,  57,   4,  53, rgb(0x048ADB)))
    decor.append(( 90,  82,  61,   4, rgb(0x048ADB)))
    decor.append((212, 158,   2,  61, rgb(0x9DD9FD)))
    decor.append((180, 189,  67,   2, rgb(0x9DD9FD)))
    decor.append((491, 179,   6,  45, rgb(0x023D60)))
    decor.append((469, 199,  50,   5, rgb(0x023D60)))
    decor.append((383,  66,   4,  44, rgb(0x0EA2FA)))
    decor.append((358,  87,  56,   5, rgb(0x0EA2FA)))
    decor.append((347, 208,  63,   2, rgb(0x035E94)))
    decor.append((375, 186,   3,  45, rgb(0x035E94)))
    decor.append(( 66, 208,   2,  40, rgb(0x012F49)))
    decor.append(( 48, 228,  40,   1, rgb(0x012F49)))


    decor.append(( 67, 315,  35,  31, rgb(0x8C4A00)))
    decor.append(( 62, 347,  50,  40, rgb(0x8C4A00)))
    decor.append(( 69, 352,  30,  25, rgb(0xC87A30)))
    decor.append(( 68, 387,  13,  13, rgb(0x5A2A00)))
    decor.append(( 86, 387,  12,  14, rgb(0x5A2A00)))
    decor.append(( 48, 373,  15,  15, rgb(0x8C4A00)))
    decor.append((106, 374,  15,  15, rgb(0x8C4A00)))
    decor.append(( 74, 332,   2,   7, rgb(0x70C0FF)))
    decor.append(( 92, 332,   3,   7, rgb(0x70C0FF)))
    decor.append(( 74, 331,   8,   3, rgb(0x000033)))
    decor.append(( 86, 331,   8,   3, rgb(0x00002D)))


    decor.append((283, 361,  15,  31, rgb(0x203050)))
    decor.append((260, 324,  40,  46, rgb(0x3070FF)))
    decor.append((270, 304,  20,  20, rgb(0xFFE0C0)))
    decor.append((269, 294,  22,  10, rgb(0x402000)))
    decor.append((262, 370,  13,  30, rgb(0x203050)))
    decor.append((253, 342,  13,  19, rgb(0xFFE0C0)))
    decor.append((296, 342,  15,   8, rgb(0xFFE0C0)))


    decor.append((339, 376,  13,  30, rgb(0x203050)))
    decor.append((322, 372,  13,  30, rgb(0x203050)))
    decor.append((320, 323,  36,  62, rgb(0xFF88CC)))
    decor.append((329, 302,  19,  22, rgb(0xFFE0C0)))
    decor.append((330, 296,  21,  12, rgb(0x804000)))
    decor.append((331, 285,  17,   9, rgb(0xFFEE44)))
    decor.append((310, 337,  11,  12, rgb(0xFFE0C0)))
    decor.append((337, 342,  10,  20, rgb(0xFFE0C0)))
    decor.append((338, 298,  13,  24, rgb(0x804000)))


    decor.append((303, 338,   6,   4, rgb(0xFFEE44)))
    decor.append((279, 393,  28,  11, rgb(0x52554A)))


    decor.append((441, 403, 198,  18, rgb(0x52554A)))
    decor.append((460, 374, 180,  30, rgb(0x52554A)))
    decor.append((483, 355, 157,  23, rgb(0x52554A)))
    decor.append((506, 337, 134,  19, rgb(0x52554A)))
    decor.append((472, 400,  19,  12, rgb(0x383A32)))
    decor.append((520, 357,  28,  14, rgb(0x383A32)))
    decor.append((572, 386,  54,  26, rgb(0x383A32)))
    decor.append((580, 342,  28,  14, rgb(0x383A32)))

    return decor



def make_decor_level1_city():
    decor = []

    decor.append((2,   2, 638, 478, rgb(0x0B1020)))
    decor.append((0,   0, 222, 215, rgb(0x111A2A)))
    decor.append((0,   0, 177, 169, rgb(0x18243A)))
    decor.append((0,   0, 126, 119, rgb(0x26406A)))
    decor.append((517, 55, 112, 393, rgb(0x505060)))
    decor.append((527, 67,  96, 385, rgb(0x3A3F57)))
    decor.append((407,216,  78, 233, rgb(0x25293B)))
    decor.append((413,231,  63, 221, rgb(0x1F2134)))
    decor.append((319, 69,  76, 382, rgb(0x505060)))
    decor.append((326, 80,  62, 372, rgb(0x32364C)))
    decor.append((197,127, 110, 321, rgb(0x25293B)))
    decor.append((202,141,  89, 308, rgb(0x1F2134)))
    decor.append((13, 101,  72, 351, rgb(0x25293B)))
    decor.append((20, 108,  40, 343, rgb(0x181A29)))


    decor.append((252,162, 21, 50, rgb(0xFFB347)))
    decor.append((449,249, 17, 43, rgb(0xFFD566)))
    decor.append((116, 79, 51, 375, rgb(0x505060)))
    decor.append((426,348, 26, 26, rgb(0xFFB347)))
    decor.append((216,241, 21, 50, rgb(0xFFD566)))
    decor.append((123, 95, 34, 358, rgb(0x32364C)))
    decor.append((351,232, 28, 52, rgb(0xFFD566)))
    decor.append((129,163, 14, 44, rgb(0xFFD566)))
    decor.append((343,107, 24, 61, rgb(0xFFD566)))
    decor.append((24, 129, 24, 52, rgb(0xFFD566)))
    decor.append((35, 214, 19, 41, rgb(0xFF9F3C)))
    decor.append((542,182, 31, 57, rgb(0xFFD566)))
    decor.append((573, 76, 34, 59, rgb(0xFFD566)))


    decor.append((23, 22, 61, 58, rgb(0xE6F4FF)))
    decor.append((34, 36, 12,  9, rgb(0x14405A)))
    decor.append((40, 60, 21, 10, rgb(0x14405A)))
    decor.append((54, 38, 16,  4, rgb(0x14405A)))
    decor.append((32, 59, 37,  7, rgb(0x14405A)))

    return pad_decor(decor)






def make_decor_level2_beach():
    decor = []

    decor.append((0,   0, 640, 480, rgb(0x6FA3E8)))
    decor.append((0,   0, 306, 294, rgb(0x8CB6EE)))
    decor.append((2,   0, 257, 250, rgb(0xC8DCF7)))
    decor.append((0,   0, 212, 205, rgb(0xFFFCF0)))
    decor.append((0,   0, 180, 173, rgb(0xFCDC87)))
    decor.append((0,   0, 136, 137, rgb(0xF8CF72)))


    decor.append((193, 203, 26,  88, rgb(0x2E8B57)))
    decor.append((76,  159, 32,  60, rgb(0x1F6B3A)))
    decor.append((91,  161, 42,  34, rgb(0x2E8B57)))
    decor.append((102, 184, 27,  44, rgb(0x5FBF7A)))
    decor.append((99,  275, 5,  204, rgb(0x6B3A1A)))
    decor.append((241, 287, 33,  30, rgb(0x2E8B57)))
    decor.append((257, 298, 46,  20, rgb(0x1F6B3A)))
    decor.append((283, 293, 28,  92, rgb(0x6B3A1A)))
    decor.append((89,  140, 27, 145, rgb(0x2E8B57)))
    decor.append((25,  301, 19,  31, rgb(0x5FBF7A)))
    decor.append((182, 323, 17, 157, rgb(0x6B3A1A)))
    decor.append((175, 174, 30, 157, rgb(0x2E8B57)))
    decor.append((268, 235, 37,  66, rgb(0x1F6B3A)))
    decor.append((23,  298, 10, 181, rgb(0x6B3A1A)))
    decor.append((236, 375, 19, 104, rgb(0x6B3A1A)))
    decor.append((304, 257, 46,  78, rgb(0x2E8B57)))
    decor.append((8,   244, 44,  63, rgb(0x2E8B57)))
    decor.append((12,  252, 20,  27, rgb(0x5FBF7A)))
    decor.append((236, 362, 70,  23, rgb(0x6B3A1A)))


    decor.append((276, 468, 364, 12, rgb(0x037992)))
    decor.append((0,   456, 277, 24, rgb(0xE9C983)))
    decor.append((35,  461, 268, 19, rgb(0xE9C983)))


    decor.append((13,  19, 84, 83, rgb(0xFDE080)))
    decor.append((29,  39, 20, 20, rgb(0xFFECB0)))

    return pad_decor(decor)




def make_decor_level3_forest():
    decor = []

    decor.append((0,   397, 640,  83, rgb(0x503F34)))
    decor.append((2,   326, 638,  97, rgb(0x382C25)))
    decor.append((0,   330, 639,  65, rgb(0x1D1512)))
    decor.append((0,     0, 640, 120, rgb(0x10242A)))


    decor.append((334, 333, 24,  63, rgb(0x604B40)))
    decor.append((1,   111, 638, 119, rgb(0x0D1A1C)))
    decor.append((0,   209, 640, 134, rgb(0x091213)))
    decor.append((45,  298, 24,  50, rgb(0x604B40)))
    decor.append((291, 216, 94, 133, rgb(0x0E261B)))
    decor.append((0,     0, 640,  60, rgb(0x162F35)))
    decor.append((598, 333, 24,  63, rgb(0x604B40)))
    decor.append((197, 348, 28,  64, rgb(0x604B40)))


    decor.append((438,  26, 40,  40, rgb(0xF6FF96)))


    decor.append((465, 362, 24,  63, rgb(0x604B40)))


    decor.append((16,  108, 81, 198, rgb(0x0E261B)))
    decor.append((580, 204, 58,  77, rgb(0x0E261B)))
    decor.append((28,  136, 58,  76, rgb(0x113522)))
    decor.append((41,  148, 34,  40, rgb(0x267863)))
    decor.append((330, 140, 40, 160, rgb(0x113522)))
    decor.append((557, 271, 83,  75, rgb(0x0E261B)))
    decor.append((178, 236, 70, 134, rgb(0x12402E)))
    decor.append((180, 243, 60,  80, rgb(0x1F5C4A)))
    decor.append((185, 250, 40,  60, rgb(0x267863)))
    decor.append((434, 269, 88, 127, rgb(0x12402E)))
    decor.append((591, 232, 41,  87, rgb(0x113522)))
    decor.append((457, 273, 60,  90, rgb(0x1F5C4A)))
    decor.append((480, 290, 30,  60, rgb(0x267863)))


    decor.append((500, 305,  6, 10, rgb(0xF6FF96)))
    decor.append((198, 266,  6, 12, rgb(0xF6FF96)))
    decor.append((54,  158,  9,  8, rgb(0xF6FF96)))


    decor.append((453,  35, 19, 10, rgb(0x5A6200)))

    return pad_decor(decor)




def make_decor_level4_industrial():
    decor = []


    decor.append((597, 110, 31, 282, rgb(0x3A3A3A)))
    decor.append((578, 312, 44,  67, rgb(0x292929)))
    decor.append((11,  102, 31, 282, rgb(0x3A3A3A)))
    decor.append((13,  318, 44,  67, rgb(0x292929)))


    decor.append((0, 354, 640, 37, rgb(0x5B5B5B)))
    decor.append((0, 125, 639, 37, rgb(0x5B5B5B)))
    decor.append((0, 378, 640, 45, rgb(0x515151)))
    decor.append((0, 102, 640, 45, rgb(0x515151)))


    decor.append((0,   104, 31, 282, rgb(0x444444)))
    decor.append((609, 114, 31, 282, rgb(0x444444)))
    decor.append((593, 328, 46,  67, rgb(0x313131)))
    decor.append((0,   389, 640, 37, rgb(0x5B5B5B)))
    decor.append((0,   403, 640, 45, rgb(0x515151)))
    decor.append((0,   330, 44,  67, rgb(0x313131)))
    decor.append((0,   421, 640, 45, rgb(0x5B5B5B)))
    decor.append((0,   437, 640, 43, rgb(0x515151)))




    decor.append((501, 227, 36, 19, rgb(0x444444)))


    decor.append((331, 397, 14,  8, rgb(0x777777)))


    decor.append((1,  93, 639, 37, rgb(0x5B5B5B)))
    decor.append((0, 72, 640, 45, rgb(0x515151)))
    decor.append((0, 57, 640, 37, rgb(0x5B5B5B)))


    decor.append((1,   0, 639, 73, rgb(0x515151)))


    decor.append((0, 34, 640, 10, rgb(0x949494)))

    return pad_decor(decor)

def make_decor_level4_industrial_conv():
    decor = []  

    decor.append((503, 44,  9, 64, rgb(0x949494)))
    decor.append((497, 27, 21, 23, rgb(0x383838)))
    decor.append((423, 98, 31, 206, rgb(0x383838)))
    decor.append((444,166,133,118, rgb(0xAA7040)))
    decor.append((462,183, 99, 84, rgb(0x774F2D)))
    decor.append((431,158,155, 15, rgb(0x774F2D)))
    decor.append((436,277,148, 12, rgb(0x774F2D)))
    decor.append((423, 97,175, 29, rgb(0x383838)))

    return pad_decor(decor)



def make_decor_level5_winter():
    decor = []
    decor.append((0,   0, 640, 480, rgb(0x181C28)))
    decor.append((0, 454, 640,  26, rgb(0x381D0E)))
    decor.append((514,257, 27, 11, rgb(0xFFFFFF)))
    decor.append((21, 424, 27, 18, rgb(0xFFFFFF)))
    decor.append((40, 356, 560, 4, rgb(0xFFFFFF)))
    decor.append((80, 268, 480, 4, rgb(0xFFFFFF)))
    decor.append((120,180,400, 4, rgb(0xFFFFFF)))
    decor.append((0, 440, 640,14, rgb(0xFFFFFF)))
    decor.append((558,351, 21, 8, rgb(0xFFFFFF)))
    decor.append((557,268,  6,16, rgb(0xFFFFFF)))
    decor.append((516,180,  5,15, rgb(0xFFFFFF)))
    decor.append((34, 356,  6,16, rgb(0xFFFFFF)))
    decor.append((114,180,  6,16, rgb(0xFFFFFF)))
    decor.append((644, 22, 3, 3, rgb(0xFFFFFF)))
    decor.append((548,321, 3, 3, rgb(0xFFFFFF)))
    decor.append((596,182, 3, 3, rgb(0xFFFFFF)))
    decor.append((432,141, 3, 3, rgb(0xFFFFFF)))
    decor.append((468, 32, 3, 3, rgb(0xFFFFFF)))
    decor.append((260, 34, 3, 3, rgb(0xFFFFFF)))
    decor.append((254,138, 3, 3, rgb(0xFFFFFF)))
    decor.append((161, 85, 6, 4, rgb(0xFFFFFF)))
    decor.append((93,  56, 3, 3, rgb(0xFFFFFF)))
    decor.append((56, 195, 3, 3, rgb(0xFFFFFF)))
    decor.append((53, 294, 3, 3, rgb(0xFFFFFF)))
    decor.append((246,320, 3, 3, rgb(0xFFFFFF)))
    decor.append((341,233, 3, 3, rgb(0xFFFFFF)))
    decor.append((432,407, 6, 5, rgb(0xFFFFFF)))
    decor.append((0, 454, 640,  26, rgb(0x381D0E)))
    return pad_decor(decor)



def make_decor_level6_desert():
    decor = []
    decor.append((0,   0, 640,202, rgb(0xCFA66A)))
    decor.append((0, 198, 640, 60, rgb(0xA67845)))
    decor.append((0, 270, 640,210, rgb(0x775431)))
    decor.append((0, 252, 640, 61, rgb(0x8B633A)))
    decor.append((592,184, 25, 82, rgb(0x7B7D2F)))
    decor.append((487,218, 33, 95, rgb(0x7B7D2F)))
    decor.append((27, 139, 29,186, rgb(0x7B7D2F)))
    decor.append((192,  0,253,120, rgb(0xD7B582)))
    decor.append((256,  0,128, 83, rgb(0xFFEBB7)))
    decor.append((283,  0, 73, 60, rgb(0xFFE29A)))
    decor.append((303,  0, 34, 31, rgb(0xFFF6D5)))
    decor.append((446,308, 77, 5, rgb(0xCFA66A)))
    decor.append((509,256,  9, 9, rgb(0x000000)))
    decor.append((24, 182,  5, 6, rgb(0x000000)))
    decor.append((21, 229,  9, 9, rgb(0x000000)))
    decor.append((482,220,  8, 9, rgb(0x000000)))
    decor.append((42, 153,  9,10, rgb(0x000000)))
    decor.append((588,224,  6, 6, rgb(0x000000)))
    decor.append((611,204,  6, 6, rgb(0x000000)))
    decor.append((318,318,  9,10, rgb(0x6B4A2E)))
    decor.append((474,143, 12,10, rgb(0x6B4A2E)))
    decor.append((201,222,  9,10, rgb(0x6B4A2E)))
    decor.append((108, 69,  9,10, rgb(0x6B4A2E)))
    return pad_decor(decor)



def make_decor_level7_lava():
    decor = []
    decor.append((0,   413, 640, 49, rgb(0x69382E)))
    decor.append((559, 400,  81, 41, rgb(0x361D18)))
    decor.append((0,   425, 640, 55, rgb(0x361D18)))
    decor.append((0,   437, 640, 43, rgb(0x1A0E0C)))
    decor.append((0,    36, 640, 48, rgb(0x804437)))
    decor.append((0,    28, 640, 49, rgb(0x69382E)))
    decor.append((0,     0, 640, 64, rgb(0x4D2922)))
    decor.append((0,     0, 640, 51, rgb(0x361D18)))
    decor.append((0,   388,  53, 35, rgb(0x69382E)))
    decor.append((1,     0, 638, 35, rgb(0x1A0E0C)))
    decor.append((2,    63,  15,362, rgb(0x4D2922)))
    decor.append((628,  51,  12,374, rgb(0x4D2922)))
    decor.append((606, 366,  33, 69, rgb(0x361D18)))
    decor.append((71,  49,  8, 46, rgb(0xFFB300)))
    decor.append((587, 52,  5, 46, rgb(0xFFB300)))
    decor.append((583, 52, 17,  9, rgb(0xFFB300)))
    decor.append((602, 83,  5, 46, rgb(0xFFB300)))


    global LAVA_MAIN_LOCAL_INDEX
    LAVA_MAIN_LOCAL_INDEX = len(decor)
    decor.append((0, 457, 640, 23, rgb(0xFF5A00)))
    decor.append((0, 468, 640, 12, rgb(0xFF7A15)))
    decor.append((20,458,  40, 10, rgb(0xFFD566)))
    decor.append((240,456, 51,  4, rgb(0xFFE08A)))
    decor.append((498,456, 39, 11, rgb(0xFFD566)))

    return pad_decor(decor)



def make_decor_level8_space():
    decor = []
    decor.append((1,  299, 639,181, rgb(0x0C0F26)))
    decor.append((0,  155, 640,160, rgb(0x11142D)))
    decor.append((0,    1, 640,160, rgb(0x151535)))
    decor.append((204, 56, 28,  9, rgb(0x45464E)))
    decor.append((155, 46, 50, 29, rgb(0x333439)))
    decor.append((179, 53, 17, 13, rgb(0x1A226A)))
    decor.append((146, 66, 22, 10, rgb(0x45464E)))
    decor.append((146, 45, 22, 10, rgb(0x45464E)))
    decor.append((133, 45, 16, 7, rgb(0xFF4500)))
    decor.append((129, 48, 16, 7, rgb(0xE63700)))
    decor.append((129, 66, 13, 7, rgb(0xFF7A1A)))
    decor.append((130, 68, 16, 7, rgb(0xD44B00)))
    decor.append((137, 67, 15, 7, rgb(0xFF5C00)))
    decor.append((553, 34, 52, 50, rgb(0x5D3BFF)))
    decor.append((560, 40, 40, 40, rgb(0x131633)))
    decor.append((0,   10,  2,  2, rgb(0xFFFFFF)))
    decor.append((421,122,  4,  5, rgb(0xAACCFF)))
    decor.append((265,317,  5,  5, rgb(0xFFFFFF)))
    decor.append((106,125, 12, 12, rgb(0xAACCFF)))
    decor.append((158,336,  5,  5, rgb(0xFFFFFF)))
    return pad_decor(decor)



DECOR_LEVELS = [
    make_decor_level1_city(),
    make_decor_level2_beach(),
    make_decor_level3_forest(),
    make_decor_level4_industrial(),
    make_decor_level5_winter(),
    make_decor_level6_desert(),
    make_decor_level7_lava(),
    make_decor_level8_space(),
]

MENU_DECOR  = make_decor_menu()
FINAL_DECOR = make_decor_final()


MENU_HERO_INDICES = [1 + i for i in MENU_HERO_LOCAL_INDICES]
MENU_MASK_INDICES = [1 + i for i in MENU_MASK_LOCAL_INDICES]
MENU_HERO_COUNT   = len(MENU_HERO_INDICES)
MENU_HERO_BASE_X  = [MENU_DECOR[i][0] for i in MENU_HERO_LOCAL_INDICES]
MENU_HERO_BASE_Y  = [MENU_DECOR[i][1] for i in MENU_HERO_LOCAL_INDICES]








MENU_LEVEL_COUNTER_FIRST = 2
MENU_LEVEL_COUNTER_COUNT = 8

MENU_LEVEL_CELL_X = [18, 28, 38, 48, 58, 68, 78, 88]
MENU_LEVEL_CELL_Y = 20
MENU_LEVEL_CELL_W = 8
MENU_LEVEL_CELL_H = 30
MENU_LEVEL_CELL_COLOR = rgb(0xC0BEBC)
MENU_LEVEL_CELL_COLOR2 = rgb(0xE0DEDC)
# 🔽 НОВОЕ: индексы прямоугольников стрелки-кнопки в памяти
MENU_BUTTON_RECT_INDICES = [11, 12, 13, 14]
MENU_BUTTON_COUNT = len(MENU_BUTTON_RECT_INDICES)


WINDOW_LEVEL   = 1
WINDOW_INDICES = [14, 15, 17, 18, 20, 21, 22, 23, 24, 25, 26]
WINDOW_COUNT   = len(WINDOW_INDICES)
WINDOW_COLOR_OFF = DECOR_COLOR_CITY2

MOON_LEVEL = 1
MOON_MAIN_INDEX = 27
MOON_GLARE_INDICES = [28, 29, 30, 31]
MOON_GLARE_COUNT = len(MOON_GLARE_INDICES)
MOON_LIGHT_INDICES = [1, 2, 3]
MOON_LIGHT_COUNT = len(MOON_LIGHT_INDICES)

MOON_ANIM_DELAY = 6
MOON_REST_DELAY = 120
MOON_MAIN_BASE_X = 23
MOON_MAIN_BASE_Y = 22
MOON_GLARE_BASE_X = [34, 40, 54, 32]
MOON_GLARE_BASE_Y = [36, 60, 38, 59]
MOON_LIGHT_BASE_X = [0, 0, 0]
MOON_LIGHT_BASE_Y = [0, 0, 0]

SUN_LEVEL = 2
SUN_INDEX = 28

SUN_LAYER_INDICES = [1, 2, 3, 4, 5, 28, 29]
SUN_LAYER_COUNT   = len(SUN_LAYER_INDICES)


SUN_LAYER_BASE_W = [306, 257, 212, 180, 136, 84, 20]
SUN_LAYER_BASE_H = [294, 250, 205, 173, 137, 83, 20]


WATER_INDICES = [25]
WATER_COUNT   = len(WATER_INDICES)
WATER_BASE_Y  = [468]

SNOW_LEVEL         = 5
SNOW_LOCAL_INDICES = list(range(13, 27))
SNOW_COUNT         = len(SNOW_LOCAL_INDICES)

SNOW_BASE_X = []
for idx in SNOW_LOCAL_INDICES:
    x, y, w, h, c = DECOR_LEVELS[SNOW_LEVEL - 1][idx]
    SNOW_BASE_X.append(x)


SNOW_WAVE_LEN  = 8
SNOW_WAVE_MASK = SNOW_WAVE_LEN - 1
SNOW_WAVE_DX   = [0, 1, 1, 0, 0, -1, -1, 0]



FOREST_LEVEL = 3


FOREST_FIREFLY_INDICES = [27, 28, 29]
FOREST_FIREFLY_COUNT   = len(FOREST_FIREFLY_INDICES)


FOREST_GLOW_INDICES = [16, 17, 21, 22, 24, 25, 26]
FOREST_GLOW_COUNT   = len(FOREST_GLOW_INDICES)


FOREST_FIREFLY_BASE_X = [500, 198,  54]
FOREST_FIREFLY_BASE_Y = [305, 266, 158]


FOREST_GLOW_BASE_X = [ 28,  41, 180, 185, 591, 457, 480]
FOREST_GLOW_BASE_Y = [136, 148, 243, 250, 232, 273, 290]



FOREST_FIREFLY_COLOR1 = rgb(0xF6FF96)
FOREST_FIREFLY_COLOR2 = rgb(0xE4EF71)


FOREST_GLOW_COLOR_BASE = [
    rgb(0x113522),
    rgb(0x267863),
    rgb(0x1F5C4A),
    rgb(0x267863),
    rgb(0xE4EF71),
    rgb(0x1F5C4A),
    rgb(0x267863),
]

FOREST_GLOW_COLOR_LIT = [
    rgb(0x163C29),
    rgb(0x2C846E),
    rgb(0x256855),
    rgb(0x2C846E),
    rgb(0x163C29),
    rgb(0x256855),
    rgb(0x2C846E),
]



FOREST_PATH_LEN  = 8
FOREST_PATH_MASK = FOREST_PATH_LEN - 1
FOREST_PATH_DX = [ 0,  1,  1,  0,  0, -1, -1,  0]
FOREST_PATH_DY = [-1,  0,  1,  1,  0,  0, -1, -1]


FOREST_ANIM_DELAY = 7




CRANE_LEVEL = 4


CRANE_LOCAL_INDICES = [0, 1, 2, 3, 4, 5, 6, 7]
CRANE_PART_COUNT    = len(CRANE_LOCAL_INDICES)


CRANE_BASE_X = [503, 497, 423, 444, 462, 431, 436, 423]
CRANE_BASE_Y = [ 44,  27,  98, 166, 183, 158, 277,  97]
CRANE_W      = [  9,  21,  31, 133,  99, 155, 148, 175]
CRANE_H      = [ 64,  23, 206, 118,  84,  15,  12,  29]
CRANE_COLOR  = [
    rgb(0x949494),
    rgb(0x383838),
    rgb(0x383838),
    rgb(0xAA7040),
    rgb(0x774F2D),
    rgb(0x774F2D),
    rgb(0x774F2D),
    rgb(0x383838),
]


CRANE_OFFSET_START_RIGHT  = -600
CRANE_OFFSET_START_LEFT   =  260
CRANE_OFFSET_FINISH_RIGHT =  260
CRANE_OFFSET_FINISH_LEFT  = -600



LOW_GRAV_DELAY = 8
player_lowgrav_active = 0
player_lowgrav_timer = 0


STARFALL_COUNT = 5
star_x  = [0] * STARFALL_COUNT
star_y  = [0] * STARFALL_COUNT
star_dx = [0] * STARFALL_COUNT
star_dy = [0] * STARFALL_COUNT
star_timer = [0] * STARFALL_COUNT
STAR_RESPAWN = 120

SPACE_LEVEL = 8
ROCKET_START_SHIFT = 400



SPACE_CORE_STAR_LOCAL_INDEX = 14

SPACE_CORE_STAR_COLOR_DARK   = rgb(0x131633)
SPACE_CORE_STAR_COLOR_BRIGHT = rgb(0xAACCFF)
SPACE_ROCKET_BODY_LOCAL_INDICES = [3, 4, 5, 6, 7]
SPACE_ROCKET_FIRE_LOCAL_INDICES = [8, 9, 10, 11, 12]

SPACE_ROCKET_BODY_COUNT = len(SPACE_ROCKET_BODY_LOCAL_INDICES)
SPACE_ROCKET_FIRE_COUNT = len(SPACE_ROCKET_FIRE_LOCAL_INDICES)


SPACE_ROCKET_BODY_BASE_X = [
    DECOR_LEVELS[SPACE_LEVEL - 1][i][0] for i in SPACE_ROCKET_BODY_LOCAL_INDICES
]
SPACE_ROCKET_BODY_BASE_Y = [
    DECOR_LEVELS[SPACE_LEVEL - 1][i][1] for i in SPACE_ROCKET_BODY_LOCAL_INDICES
]


SPACE_ROCKET_FIRE_BASE_X = [
    DECOR_LEVELS[SPACE_LEVEL - 1][i][0] for i in SPACE_ROCKET_FIRE_LOCAL_INDICES
]
SPACE_ROCKET_FIRE_BASE_Y = [
    DECOR_LEVELS[SPACE_LEVEL - 1][i][1] for i in SPACE_ROCKET_FIRE_LOCAL_INDICES
]


ROCKET_CYCLE_FRAMES = 3600


ROCKET_FLY_FRAMES = 2000


ROCKET_SPEED = 1


FINAL_STAR_INDICES = list(range(3, 22))
FINAL_STAR_COUNT   = len(FINAL_STAR_INDICES)

FINAL_BIG_STAR_INDICES    = [7, 8, 9, 10, 11, 12]
FINAL_SMALL_STAR_INDICES  = [13, 14, 15, 16, 17, 18, 19, 20, 21]

FINAL_DONKEY_BODY_INDICES = [26, 27, 28]
FINAL_DONKEY_LIMB_INDICES = [29, 30, 31, 32]
FINAL_DONKEY_TEAR_INDICES = [33, 34]

FINAL_SHREK_INDICES       = [38, 39, 40, 41, 42, 43]
FINAL_FIONA_INDICES       = [45, 46, 47, 48, 49, 50, 51, 52]

FINAL_STAR_BASE_Y = [FINAL_DECOR[idx][1] for idx in FINAL_STAR_INDICES]

FINAL_DONKEY_BODY_BASE_Y = [FINAL_DECOR[idx][1] for idx in FINAL_DONKEY_BODY_INDICES]
FINAL_DONKEY_LIMB_BASE_Y = [FINAL_DECOR[idx][1] for idx in FINAL_DONKEY_LIMB_INDICES]

FINAL_SHREK_BASE_Y = [FINAL_DECOR[idx][1] for idx in FINAL_SHREK_INDICES]
FINAL_FIONA_BASE_Y = [FINAL_DECOR[idx][1] for idx in FINAL_FIONA_INDICES]

final_big_star_indices    = FINAL_BIG_STAR_INDICES
final_big_star_count      = len(FINAL_BIG_STAR_INDICES)

final_small_star_indices  = FINAL_SMALL_STAR_INDICES
final_small_star_count    = len(FINAL_SMALL_STAR_INDICES)

final_donkey_body_indices = FINAL_DONKEY_BODY_INDICES
final_donkey_body_count   = len(FINAL_DONKEY_BODY_INDICES)

final_donkey_limb_indices = FINAL_DONKEY_LIMB_INDICES
final_donkey_limb_count   = len(FINAL_DONKEY_LIMB_INDICES)

final_donkey_tear_indices = FINAL_DONKEY_TEAR_INDICES
final_donkey_tear_count   = len(FINAL_DONKEY_TEAR_INDICES)

final_shrek_indices  = FINAL_SHREK_INDICES
final_shrek_count    = len(FINAL_SHREK_INDICES)

final_fiona_indices  = FINAL_FIONA_INDICES
final_fiona_count    = len(FINAL_FIONA_INDICES)


DECOR_LEVELS_FLAT = []
for lvl in DECOR_LEVELS:
    for (x, y, w, h, c) in lvl:
        DECOR_LEVELS_FLAT += [x, y, w, h, c]

DECOR_DATA = []
for _ in range(DECOR_COUNT):
    DECOR_DATA += [1, -1000, 0, 8, 8, BG_COLOR]


SUN_PATH_LEN = 48
sun_path_x = []
sun_path_y = []
start_x = 40
end_x   = SCREEN_W - 80
dx = (end_x - start_x) // SUN_PATH_LEN if SUN_PATH_LEN != 0 else 0
for t in range(SUN_PATH_LEN):
    x = start_x + t * dx
    if t < SUN_PATH_LEN // 2:
        y = 80 - t // 4
    else:
        y = 80 - (SUN_PATH_LEN // 2) // 4 + (t - SUN_PATH_LEN // 2) // 4
    sun_path_x.append(x)
    sun_path_y.append(y)



DONKEY_X = 140
DONKEY_Y = L3_Y - 28

DONKEY_COLOR_DARK   = rgb(0x5a2a00)
DONKEY_COLOR_MID    = rgb(0x8c4a00)
DONKEY_COLOR_LIGHT  = rgb(0xc87a30)

DONKEY_DATA = [
    1, DONKEY_X,     DONKEY_Y + 8, 26, 18, DONKEY_COLOR_DARK,
    0, 5,            4,            16, 10, DONKEY_COLOR_LIGHT,
    0, 4,           -8,            14, 8,  DONKEY_COLOR_MID,
    0, 2,            18,           8,  6,  DONKEY_COLOR_DARK,
    0, 16,           18,           8,  6,  DONKEY_COLOR_DARK,
]
DONKEY_PARTS = len(DONKEY_DATA) // 6



PRINCESS_X = 460
PRINCESS_Y = L3_Y - 26

PRINCESS_COLOR_DRESS = rgb(0xff88cc)
PRINCESS_COLOR_SKIN  = rgb(0xffe0c0)
PRINCESS_COLOR_HAIR  = rgb(0x804000)
PRINCESS_COLOR_CROWN = rgb(0xffee44)

PRINCESS_DATA = [
    1, PRINCESS_X,      PRINCESS_Y + 8, 18, 18, PRINCESS_COLOR_DRESS,
    0, 4,               -8,             10, 8,  PRINCESS_COLOR_SKIN,
    0, 2,               -10,            14, 4,  PRINCESS_COLOR_HAIR,
    0, 6,               -14,            6,  3,  PRINCESS_COLOR_CROWN,
]
PRINCESS_PARTS = len(PRINCESS_DATA) // 6

PRINCESS_W = 18
PRINCESS_H = 24



PLAYER_W   = 20
PLAYER_H   = 24
PLAYER_BODY_CLR = rgb(0x3070ff)
PLAYER_HEAD_CLR = rgb(0xffe0c0)
PLAYER_LEG_CLR  = rgb(0x203050)

PLAYER_START_X = 40
PLAYER_START_Y = GROUND_Y - PLAYER_H

PLAYER_DATA = [
    1, PLAYER_START_X, PLAYER_START_Y + 4,  16, 14, PLAYER_BODY_CLR,
    0, 2,             -8,                  12, 8,  PLAYER_HEAD_CLR,
    0, 2,              14,                  4, 6,  PLAYER_LEG_CLR,
    0, 10,             14,                  4, 6,  PLAYER_LEG_CLR,
]
PLAYER_PARTS = len(PLAYER_DATA) // 6



BARREL_W   = 18
BARREL_H   = 18
BARREL_CLR = rgb(0xff8020)
BARREL_OUTLINE_CLR = rgb(0xff8020)

BARREL_START_X = DONKEY_X + 10
BARREL_START_Y = L3_Y - BARREL_H


MAX_BARRELS = 6

BARREL_DATA = []
for _ in range(MAX_BARRELS):
    BARREL_DATA += [1, -1000, 0, BARREL_W, BARREL_H, BARREL_OUTLINE_CLR]





DECOR_OVERLAY_COUNT = 24
OVERLAY_EXTRA_COUNT = 8


DUMMY_RECT_OVERLAY = [1, -1000, 0, 8, 8, 0]
MENU_BG_RECT = [1, 0, 0, 640, 480, rgb(0x181C28)]


DECOR_DATA_OVERLAY = []
for _ in range(DECOR_OVERLAY_COUNT):
    DECOR_DATA_OVERLAY += [1, -1000, 0, 8, 8, BG_COLOR]


PLATFORM_DATA_OVERLAY = []
for _ in range(PLATFORM_COUNT):
    PLATFORM_DATA_OVERLAY += [1, -1000, 0, 8, PLATFORM_H, PLATFORM_COLOR]


LADDER_DATA_OVERLAY = []
for _ in range(LADDER_COUNT):
    LADDER_DATA_OVERLAY += [1, -1000, 0, LADDER_W, 64, LADDER_CLR]



PLAYER_DATA_OVERLAY   = PLAYER_DATA
PRINCESS_DATA_OVERLAY = PRINCESS_DATA
DONKEY_DATA_OVERLAY   = DONKEY_DATA
BARREL_DATA_OVERLAY   = BARREL_DATA


OVERLAY_EXTRA_DATA = []
for i in range(OVERLAY_EXTRA_COUNT):

    OVERLAY_EXTRA_DATA += [
        1,
        -1000,
        0,
        CRANE_W[i],
        CRANE_H[i],
        CRANE_COLOR[i],
    ]


def make_bg_data_base_overlay():
    return (
        DUMMY_RECT_OVERLAY +
        DECOR_DATA_OVERLAY +
        PLATFORM_DATA_OVERLAY +
        LADDER_DATA_OVERLAY +
        PLAYER_DATA_OVERLAY +
        PRINCESS_DATA_OVERLAY +
        DONKEY_DATA_OVERLAY +
        BARREL_DATA_OVERLAY +
        OVERLAY_EXTRA_DATA
    )

BG_DATA_LEVEL_OVERLAY = make_bg_data_base_overlay()
BG_DATA_LEVEL_OVERLAY_SIZE = len(BG_DATA_LEVEL_OVERLAY)




BACKGROUND_RECT    = 0
DECOR_RECT_BASE    = 1
PLATFORM_RECT_BASE = DECOR_RECT_BASE + DECOR_COUNT
LADDER_RECT_BASE   = PLATFORM_RECT_BASE + PLATFORM_COUNT
DONKEY_RECT_BASE   = LADDER_RECT_BASE + LADDER_COUNT
PRINCESS_RECT_BASE = DONKEY_RECT_BASE + DONKEY_PARTS
PLAYER_RECT_BASE   = PRINCESS_RECT_BASE + PRINCESS_PARTS
BARREL_RECT_BASE   = PLAYER_RECT_BASE + PLAYER_PARTS



BACKGROUND_RECT_OVERLAY    = 0
DECOR_OVERLAY_RECT_BASE    = BACKGROUND_RECT_OVERLAY + 1
PLATFORM_OVERLAY_RECT_BASE = DECOR_OVERLAY_RECT_BASE + DECOR_OVERLAY_COUNT
LADDER_OVERLAY_RECT_BASE   = PLATFORM_OVERLAY_RECT_BASE + PLATFORM_COUNT
PLAYER_OVERLAY_RECT_BASE   = LADDER_OVERLAY_RECT_BASE + LADDER_COUNT
PRINCESS_OVERLAY_RECT_BASE = PLAYER_OVERLAY_RECT_BASE + PLAYER_PARTS
DONKEY_OVERLAY_RECT_BASE   = PRINCESS_OVERLAY_RECT_BASE + PRINCESS_PARTS
BARREL_OVERLAY_RECT_BASE   = DONKEY_OVERLAY_RECT_BASE + DONKEY_PARTS
FOREGROUND_OVERLAY_RECT_BASE = BARREL_OVERLAY_RECT_BASE + MAX_BARRELS
OVERLAY_RECT_BASE = FOREGROUND_OVERLAY_RECT_BASE






DUMMY_RECT = [1, -1000, 0, 8, 8, 0]

def make_bg_data_base():
    return (
        DUMMY_RECT +
        DECOR_DATA +
        PLATFORM_DATA +
        LADDER_DATA +
        DONKEY_DATA +
        PRINCESS_DATA +
        PLAYER_DATA +
        BARREL_DATA
    )


BG_DATA_LEVEL1 = make_bg_data_base()
BG_DATA_LEVEL2 = make_bg_data_base()
BG_DATA_LEVEL3 = make_bg_data_base()
BG_DATA_LEVEL4 = make_bg_data_base()
BG_DATA_LEVEL5 = make_bg_data_base()
BG_DATA_LEVEL6 = make_bg_data_base()
BG_DATA_LEVEL7 = make_bg_data_base()
BG_DATA_LEVEL8 = make_bg_data_base()


def make_bg_data_menu_full():
    rects = []
    rects += MENU_BG_RECT
    for (x, y, w, h, c) in MENU_DECOR:
        rects += [1, x, y, w, h, c]

    while len(rects) < RECT_NUM * 6:
        rects += [1, -1000, 0, 8, 8, 0]
    return rects

def make_bg_data_final_full():
    rects = []
    rects += DUMMY_RECT
    for (x, y, w, h, c) in FINAL_DECOR:
        rects += [1, x, y, w, h, c]
    while len(rects) < RECT_NUM * 6:
        rects += [1, -1000, 0, 8, 8, 0]
    return rects

BG_DATA_MENU  = make_bg_data_menu_full()
BG_DATA_FINAL = make_bg_data_final_full()


BG_DATA_LEVEL1_SIZE = len(BG_DATA_LEVEL1)
BG_DATA_LEVEL2_SIZE = len(BG_DATA_LEVEL2)
BG_DATA_LEVEL3_SIZE = len(BG_DATA_LEVEL3)
BG_DATA_LEVEL4_SIZE = len(BG_DATA_LEVEL4)
BG_DATA_LEVEL5_SIZE = len(BG_DATA_LEVEL5)
BG_DATA_LEVEL6_SIZE = len(BG_DATA_LEVEL6)
BG_DATA_LEVEL7_SIZE = len(BG_DATA_LEVEL7)
BG_DATA_LEVEL8_SIZE = len(BG_DATA_LEVEL8)
BG_DATA_MENU_SIZE   = len(BG_DATA_MENU)
BG_DATA_FINAL_SIZE  = len(BG_DATA_FINAL)



GRAV         = 2
WALK_SPEED   = 3
CLIMB_SPEED  = 2
BARREL_SPEED = 3

ARROW_COLOR = rgb(0x00ff00)

barrel_x_init       = [-1000] * MAX_BARRELS
barrel_y_init       = [-1000] * MAX_BARRELS
barrel_vx_init      = [0] * MAX_BARRELS
barrel_vy_init      = [0] * MAX_BARRELS
barrel_active_init  = [0] * MAX_BARRELS
barrel_falling_init = [0] * MAX_BARRELS
barrel_type_init    = [0] * MAX_BARRELS

spawn_delay_a = [1, 10, 50, 60, 50, 60, 50, 60]
spawn_delay_b = [1, 10, 90, 50, 60, 50, 60, 50]
barrel_speed_level = [3, 4, 4, 4, 4, 3, 3, 4]

LAVA_LEVEL = 7
LAVA_TOP_BASE_Y = DECOR_LEVELS[LAVA_LEVEL - 1][LAVA_MAIN_LOCAL_INDEX][1]




LAVA_BUBBLE_LOCAL_INDICES = [
    LAVA_MAIN_LOCAL_INDEX + 1,
    LAVA_MAIN_LOCAL_INDEX + 2,
    LAVA_MAIN_LOCAL_INDEX + 3,
    LAVA_MAIN_LOCAL_INDEX + 4,
]
LAVA_BUBBLE_COUNT = len(LAVA_BUBBLE_LOCAL_INDICES)


LAVA_BUBBLE_OFFSET_Y = [
    DECOR_LEVELS[LAVA_LEVEL - 1][i][1] - LAVA_TOP_BASE_Y
    for i in LAVA_BUBBLE_LOCAL_INDICES
]


LAVA_BUBBLE_BASE_H = [
    DECOR_LEVELS[LAVA_LEVEL - 1][i][3]
    for i in LAVA_BUBBLE_LOCAL_INDICES
]


save_game("donkey.bin", f"""
bg_data_level1 = {BG_DATA_LEVEL1}
bg_data_level2 = {BG_DATA_LEVEL2}
bg_data_level3 = {BG_DATA_LEVEL3}
bg_data_level4 = {BG_DATA_LEVEL4}
bg_data_level5 = {BG_DATA_LEVEL5}
bg_data_level6 = {BG_DATA_LEVEL6}
bg_data_level7 = {BG_DATA_LEVEL7}
bg_data_level8 = {BG_DATA_LEVEL8}
bg_data_menu   = {BG_DATA_MENU}
bg_data_final  = {BG_DATA_FINAL}
bg_data_level_overlay = {BG_DATA_LEVEL_OVERLAY}

BG_DATA_LEVEL1_SIZE = {BG_DATA_LEVEL1_SIZE}
BG_DATA_LEVEL2_SIZE = {BG_DATA_LEVEL2_SIZE}
BG_DATA_LEVEL3_SIZE = {BG_DATA_LEVEL3_SIZE}
BG_DATA_LEVEL4_SIZE = {BG_DATA_LEVEL4_SIZE}
BG_DATA_LEVEL5_SIZE = {BG_DATA_LEVEL5_SIZE}
BG_DATA_LEVEL6_SIZE = {BG_DATA_LEVEL6_SIZE}
BG_DATA_LEVEL7_SIZE = {BG_DATA_LEVEL7_SIZE}
BG_DATA_LEVEL8_SIZE = {BG_DATA_LEVEL8_SIZE}
BG_DATA_MENU_SIZE   = {BG_DATA_MENU_SIZE}
BG_DATA_FINAL_SIZE  = {BG_DATA_FINAL_SIZE}

BG_DATA_LEVEL_OVERLAY_SIZE = {BG_DATA_LEVEL_OVERLAY_SIZE}
DECOR_OVERLAY_COUNT   = {DECOR_OVERLAY_COUNT}
OVERLAY_EXTRA_COUNT   = {OVERLAY_EXTRA_COUNT}

BACKGROUND_RECT_OVERLAY    = {BACKGROUND_RECT_OVERLAY}
DECOR_OVERLAY_RECT_BASE    = {DECOR_OVERLAY_RECT_BASE}
PLATFORM_OVERLAY_RECT_BASE = {PLATFORM_OVERLAY_RECT_BASE}
LADDER_OVERLAY_RECT_BASE   = {LADDER_OVERLAY_RECT_BASE}
PLAYER_OVERLAY_RECT_BASE   = {PLAYER_OVERLAY_RECT_BASE}
PRINCESS_OVERLAY_RECT_BASE = {PRINCESS_OVERLAY_RECT_BASE}
DONKEY_OVERLAY_RECT_BASE   = {DONKEY_OVERLAY_RECT_BASE}
BARREL_OVERLAY_RECT_BASE   = {BARREL_OVERLAY_RECT_BASE}
FOREGROUND_OVERLAY_RECT_BASE = {FOREGROUND_OVERLAY_RECT_BASE}
OVERLAY_RECT_BASE = {OVERLAY_RECT_BASE}

final_big_star_count    = {final_big_star_count}
final_big_star_indices  = {final_big_star_indices}

final_small_star_count  = {final_small_star_count}
final_small_star_indices= {final_small_star_indices}

final_donkey_body_count   = {final_donkey_body_count}
final_donkey_body_indices = {final_donkey_body_indices}

final_donkey_limb_count   = {final_donkey_limb_count}
final_donkey_limb_indices = {final_donkey_limb_indices}

final_donkey_tear_count   = {final_donkey_tear_count}
final_donkey_tear_indices = {final_donkey_tear_indices}

final_shrek_count   = {final_shrek_count}
final_shrek_indices = {final_shrek_indices}

final_fiona_count   = {final_fiona_count}
final_fiona_indices = {final_fiona_indices}

final_star_base_y = {FINAL_STAR_BASE_Y}

final_donkey_body_base_y = {FINAL_DONKEY_BODY_BASE_Y}
final_donkey_limb_base_y = {FINAL_DONKEY_LIMB_BASE_Y}

final_shrek_base_y = {FINAL_SHREK_BASE_Y}
final_fiona_base_y = {FINAL_FIONA_BASE_Y}


FINAL_BREATH_DELAY  = 5
FINAL_BREATH_MAX    = 3
FINAL_COLOR1        = 0xFFFFFF
FINAL_COLOR2        = 0xE6F4FF



plat_x1 = {plat_x1}
plat_x2 = {plat_x2}
plat_y  = {plat_y}
PLATFORM_COUNT = {PLATFORM_COUNT}

lad_x1 = {lad_x1}
lad_x2 = {lad_x2}
lad_y1 = {lad_y1}
lad_y2 = {lad_y2}
LADDER_COUNT = {LADDER_COUNT}
LADDER_W = {LADDER_W}

platform_levels = {PLATFORM_LEVELS_FLAT}
ladder_levels   = {LADDER_LEVELS_FLAT}

DECOR_COUNT = {DECOR_COUNT}
decor_levels   = {DECOR_LEVELS_FLAT}

SNOW_LEVEL = {SNOW_LEVEL}
SNOW_COUNT = {SNOW_COUNT}
snow_indices = {SNOW_LOCAL_INDICES}
snow_base_x   = {SNOW_BASE_X}
SNOW_WAVE_LEN  = {SNOW_WAVE_LEN}
SNOW_WAVE_MASK = {SNOW_WAVE_MASK}
snow_wave_dx   = {SNOW_WAVE_DX}

WINDOW_LEVEL = {WINDOW_LEVEL}
WINDOW_COUNT = {WINDOW_COUNT}
window_indices = {WINDOW_INDICES}
window_color_on  = {WINDOW_COLOR_ON}
window_color_off = {WINDOW_COLOR_OFF}

MOON_LEVEL = {MOON_LEVEL}
moon_main_index   = {MOON_MAIN_INDEX}
moon_glare_count  = {MOON_GLARE_COUNT}
moon_glare_indices = {MOON_GLARE_INDICES}
MOON_ANIM_DELAY   = {MOON_ANIM_DELAY}
moon_main_base_x  = {MOON_MAIN_BASE_X}
moon_main_base_y  = {MOON_MAIN_BASE_Y}
moon_glare_base_x = {MOON_GLARE_BASE_X}
moon_glare_base_y = {MOON_GLARE_BASE_Y}
moon_light_count   = {MOON_LIGHT_COUNT}
moon_light_indices = {MOON_LIGHT_INDICES}
moon_light_base_x  = {MOON_LIGHT_BASE_X}
moon_light_base_y  = {MOON_LIGHT_BASE_Y}


SUN_LEVEL    = {SUN_LEVEL}
sun_index    = {SUN_INDEX}
SUN_PATH_LEN = {SUN_PATH_LEN}
sun_path_x   = {sun_path_x}
sun_path_y   = {sun_path_y}

sun_layer_count   = {SUN_LAYER_COUNT}
sun_layer_indices = {SUN_LAYER_INDICES}
sun_layer_base_w  = {SUN_LAYER_BASE_W}
sun_layer_base_h  = {SUN_LAYER_BASE_H}

water_count   = {WATER_COUNT}
water_indices = {WATER_INDICES}
water_base_y  = {WATER_BASE_Y}

SNOW_ANIM_DELAY   = {SNOW_ANIM_DELAY}
WINDOW_ANIM_DELAY = {WINDOW_ANIM_DELAY}
SUN_ANIM_DELAY    = {SUN_ANIM_DELAY}
MOON_REST_DELAY   = {MOON_REST_DELAY}
SANDSTORM_ANIM_DELAY    = {SANDSTORM_ANIM_DELAY}

FOREST_LEVEL = {FOREST_LEVEL}

FOREST_FIREFLY_COUNT   = {FOREST_FIREFLY_COUNT}
FOREST_FIREFLY_INDICES = {FOREST_FIREFLY_INDICES}
FOREST_FIREFLY_BASE_X  = {FOREST_FIREFLY_BASE_X}
FOREST_FIREFLY_BASE_Y  = {FOREST_FIREFLY_BASE_Y}

FOREST_GLOW_COUNT   = {FOREST_GLOW_COUNT}
FOREST_GLOW_INDICES = {FOREST_GLOW_INDICES}
FOREST_GLOW_BASE_X  = {FOREST_GLOW_BASE_X}
FOREST_GLOW_BASE_Y  = {FOREST_GLOW_BASE_Y}

FOREST_FIREFLY_COLOR1 = {FOREST_FIREFLY_COLOR1}
FOREST_FIREFLY_COLOR2 = {FOREST_FIREFLY_COLOR2}

FOREST_GLOW_COLOR_BASE = {FOREST_GLOW_COLOR_BASE}
FOREST_GLOW_COLOR_LIT  = {FOREST_GLOW_COLOR_LIT}

FOREST_PATH_LEN  = {FOREST_PATH_LEN}
FOREST_PATH_MASK = {FOREST_PATH_MASK}
FOREST_PATH_DX   = {FOREST_PATH_DX}
FOREST_PATH_DY   = {FOREST_PATH_DY}

FOREST_ANIM_DELAY = {FOREST_ANIM_DELAY}

CRANE_LEVEL = {CRANE_LEVEL}
crane_part_count    = {CRANE_PART_COUNT}
crane_local_indices = {CRANE_LOCAL_INDICES}
crane_base_x        = {CRANE_BASE_X}
crane_base_y        = {CRANE_BASE_Y}

CRANE_OFFSET_START_RIGHT  = {CRANE_OFFSET_START_RIGHT}
CRANE_OFFSET_START_LEFT   = {CRANE_OFFSET_START_LEFT}
CRANE_OFFSET_FINISH_RIGHT = {CRANE_OFFSET_FINISH_RIGHT}
CRANE_OFFSET_FINISH_LEFT  = {CRANE_OFFSET_FINISH_LEFT}


LAVA_LEVEL      = {LAVA_LEVEL}
LAVA_MAIN_INDEX = {LAVA_MAIN_LOCAL_INDEX}
lava_bubble_count    = {LAVA_BUBBLE_COUNT}
lava_bubble_indices  = {LAVA_BUBBLE_LOCAL_INDICES}
lava_bubble_offset_y = {LAVA_BUBBLE_OFFSET_Y}
lava_bubble_base_h   = {LAVA_BUBBLE_BASE_H}

SPACE_LEVEL = {SPACE_LEVEL}
ROCKET_START_SHIFT = {ROCKET_START_SHIFT}
space_core_star_local_index = {SPACE_CORE_STAR_LOCAL_INDEX}
space_core_star_color_dark   = {SPACE_CORE_STAR_COLOR_DARK}
space_core_star_color_bright = {SPACE_CORE_STAR_COLOR_BRIGHT}
space_rocket_body_count     = {SPACE_ROCKET_BODY_COUNT}
space_rocket_body_indices   = {SPACE_ROCKET_BODY_LOCAL_INDICES}
space_rocket_body_base_x    = {SPACE_ROCKET_BODY_BASE_X}
space_rocket_body_base_y    = {SPACE_ROCKET_BODY_BASE_Y}

space_rocket_fire_count     = {SPACE_ROCKET_FIRE_COUNT}
space_rocket_fire_indices   = {SPACE_ROCKET_FIRE_LOCAL_INDICES}
space_rocket_fire_base_x    = {SPACE_ROCKET_FIRE_BASE_X}
space_rocket_fire_base_y    = {SPACE_ROCKET_FIRE_BASE_Y}

ROCKET_CYCLE_FRAMES = {ROCKET_CYCLE_FRAMES}
ROCKET_FLY_FRAMES   = {ROCKET_FLY_FRAMES}
ROCKET_SPEED        = {ROCKET_SPEED}
rocket_timer        = 0


LOW_GRAV_DELAY = {LOW_GRAV_DELAY}
player_lowgrav_active = {player_lowgrav_active}
player_lowgrav_timer = {player_lowgrav_timer}


LOW_GRAV_DELAY = {LOW_GRAV_DELAY}
player_lowgrav_active = {player_lowgrav_active}
player_lowgrav_timer = {player_lowgrav_timer}

MENU_LEVEL_COUNTER_FIRST = {MENU_LEVEL_COUNTER_FIRST}
MENU_LEVEL_COUNTER_COUNT = {MENU_LEVEL_COUNTER_COUNT}
menu_level_cell_x = {MENU_LEVEL_CELL_X}
menu_level_cell_y = {MENU_LEVEL_CELL_Y}
menu_level_cell_w = {MENU_LEVEL_CELL_W}
menu_level_cell_h = {MENU_LEVEL_CELL_H}
menu_level_cell_color = {MENU_LEVEL_CELL_COLOR}
menu_button_color1 = {MENU_LEVEL_CELL_COLOR}      # базовый цвет
menu_button_color2 = {MENU_LEVEL_CELL_COLOR2}
menu_button_count   = {MENU_BUTTON_COUNT}
menu_button_indices = {MENU_BUTTON_RECT_INDICES}

MENU_BUTTON_ANIM_DELAY = 16
menu_button_timer = 0
menu_button_phase = 0

menu_hero_count   = {MENU_HERO_COUNT}
menu_hero_indices = {MENU_HERO_INDICES}
menu_hero_base_y  = {MENU_HERO_BASE_Y}
menu_hero_base_x  = {MENU_HERO_BASE_X}

final_star_count   = {FINAL_STAR_COUNT}
final_star_indices = {FINAL_STAR_INDICES}
final_star_color1  = 0xFFFFFF
final_star_color2  = 0xC4D9FF

DONKEY_PARTS   = {DONKEY_PARTS}
PRINCESS_PARTS = {PRINCESS_PARTS}
PLAYER_PARTS   = {PLAYER_PARTS}

player_w      = {PLAYER_W}
player_h      = {PLAYER_H}
player_half_w = {PLAYER_W // 2}

barrel_w = {BARREL_W}
barrel_h = {BARREL_H}
MAX_BARRELS = {MAX_BARRELS}

princess_w = {PRINCESS_W}
princess_h = {PRINCESS_H}

ground_y = {GROUND_Y}
screen_w = {SCREEN_W}
screen_h = {SCREEN_H}

grav         = {GRAV}
walk_speed   = {WALK_SPEED}
climb_speed  = {CLIMB_SPEED}
barrel_speed = {BARREL_SPEED}
player_grav  = {GRAV}

player_start_x = {PLAYER_START_X}
player_start_y = {PLAYER_START_Y}
player_x = {PLAYER_START_X}
player_y = {PLAYER_START_Y}
player_vx = 0
player_vy = 0
climbing_flag = 0
climb_ladder_x = 0

player_anim = 0
player_anim_timer = 0
player_dir = 1

barrel_x       = {barrel_x_init}
barrel_y       = {barrel_y_init}
barrel_vx      = {barrel_vx_init}
barrel_vy      = {barrel_vy_init}
barrel_active  = {barrel_active_init}
barrel_falling = {barrel_falling_init}
barrel_type    = {barrel_type_init}

barrel_spawn_x = {BARREL_START_X}
barrel_spawn_y = {BARREL_START_Y}
spawn_timer = 0
spawn_delay = 40

arrow_color          = {ARROW_COLOR}
barrel_color         = {BARREL_CLR}
barrel_outline_color = {BARREL_OUTLINE_CLR}

spawn_delay_a      = {spawn_delay_a}
spawn_delay_b      = {spawn_delay_b}
barrel_speed_level = {barrel_speed_level}

decor_rect_base    = {DECOR_RECT_BASE}
platform_rect_base = {PLATFORM_RECT_BASE}
ladder_rect_base   = {LADDER_RECT_BASE}
player_rect_base   = {PLAYER_RECT_BASE}
princess_rect_base = {PRINCESS_RECT_BASE}
donkey_rect_base   = {DONKEY_RECT_BASE}
barrel_rect_base   = {BARREL_RECT_BASE}


overlay_mode = 0


rand_state = 123

snow_phase   = 0
window_phase = 0
sun_phase    = 0
moon_phase   = 0

forest_anim_timer  = 0
forest_phase_move  = 0
forest_phase_color = 0

crane_state       = 0
crane_dir         = 0
crane_offset      = 0
crane_speed       = 0
crane_rest_timer  = 0
crane_rest_delay  = 0


BEACH_WATER_PHASE_MAX = 24
water_phase       = 0
water_anim_timer  = 0

snow_anim_timer   = 0
window_anim_timer = 0
sun_anim_timer    = 0
moon_anim_timer   = 0
sandstorm_anim_timer = 0

invert_control_active     = 0
invert_control_timer      = 0
invert_control_on_frames  = 120
invert_control_off_frames = 180

moon_rest_timer   = 0
moon_shake_active = 0

final_anim_timer  = 0
final_phase       = 0
donkey_idle_phase = 0
princess_idle_phase = 0
final_big_star_timer = 0
final_big_star_phase = 0
hero_idle_phase = 0
idle_timer = 0


menu_button_timer = 0        # таймер дыхания кнопок уровней
menu_button_phase = 0        # 0 — базовый цвет, 1 — светлый полутон


menu_hero_phase = 0          # фаза вертикального "дыхания"
menu_hero_timer = 0          # таймер вертикали
menu_hero_move_step = 0      # шаг движения по X (0..79)
menu_hero_move_timer = 0     # таймер для обновления шага X
menu_hero_pause_timer = 0    # пауза между "заездами" слева направо
menu_k_prev = 0 

FINAL_BIG_STAR_OUTER = 21
FINAL_BIG_STAR_INNER = 22

menu_hero_phase = 0
menu_hero_timer = 0

vertical_spawn_pending = 0
vertical_spawn_timer   = 0
vertical_spawn_delay   = 4

wind_dir = 0
wind_timer = 0
wind_change_interval = 240

lava_level_y      = {SCREEN_H}
lava_active       = 0
lava_start_timer  = 0
lava_start_delay  = 280
lava_anim_timer   = 0
lava_anim_delay   = 8
lava_bubble_phase = 0

STATE_MENU  = 0
STATE_PLAY  = 1
STATE_FINAL = 2

MAX_LEVEL = 8
current_level = 1

game_state = 0

def main():
    setup()
    while 1:
        frame()
        wait()

def setup():
    current_level = 1
    set_level_layout_mode()
    reset_game()
    apply_level_layout()
    load_bg_menu()
    reset_menu_heroes() 
    game_state = STATE_MENU


def frame():
    if game_state == STATE_MENU:
        frame_menu()
    elif game_state == STATE_PLAY:
        update()
    else:
        frame_final()

def rand8():
    rand_state = (rand_state * 109) + 89
    rand_state = rand_state & 255
    return rand_state

def barrel_set_rects(i, x, y):
    base_barrel = {RECT_MEM} + barrel_rect_base * {RECT_SIZE}

    bmain = base_barrel + i * {RECT_SIZE}

    bmain[{RECT_X}] = x
    bmain[{RECT_Y}] = y
    bmain[{RECT_W}] = barrel_w
    bmain[{RECT_H}] = barrel_h
    bmain[{RECT_COLOR}] = barrel_outline_color

def barrel_hide(i):
    base_barrel = {RECT_MEM} + barrel_rect_base * {RECT_SIZE}

    bmain = base_barrel + i * {RECT_SIZE}
    bmain[{RECT_X}] = -1000
    bmain[{RECT_Y}] = 0

def set_level_layout_mode():
    if current_level == CRANE_LEVEL:
        overlay_mode = 1

        decor_rect_base    = DECOR_OVERLAY_RECT_BASE
        platform_rect_base = PLATFORM_OVERLAY_RECT_BASE
        ladder_rect_base   = LADDER_OVERLAY_RECT_BASE
        player_rect_base   = PLAYER_OVERLAY_RECT_BASE
        princess_rect_base = PRINCESS_OVERLAY_RECT_BASE
        donkey_rect_base   = DONKEY_OVERLAY_RECT_BASE
        barrel_rect_base   = BARREL_OVERLAY_RECT_BASE
    else:
        overlay_mode = 0

        decor_rect_base    = {DECOR_RECT_BASE}
        platform_rect_base = {PLATFORM_RECT_BASE}
        ladder_rect_base   = {LADDER_RECT_BASE}
        player_rect_base   = {PLAYER_RECT_BASE}
        princess_rect_base = {PRINCESS_RECT_BASE}
        donkey_rect_base   = {DONKEY_RECT_BASE}
        barrel_rect_base   = {BARREL_RECT_BASE}

    
def update_level_colliders():
    base = {RECT_MEM} + platform_rect_base * {RECT_SIZE}
    base_idx = (current_level - 1) * PLATFORM_COUNT * 5

    i = 0
    while i < PLATFORM_COUNT:
        idx = base_idx + i * 5

        x = platform_levels[idx]
        y = platform_levels[idx + 1]
        w = platform_levels[idx + 2]
        h = platform_levels[idx + 3]
        color = platform_levels[idx + 4]

        addr = base + i * {RECT_SIZE}

        if (w <= 0) | (h <= 0):
            plat_x1[i] = -1000
            plat_x2[i] = -900
            plat_y[i]  = 0

            addr[{RECT_X}] = -1000
            addr[{RECT_Y}] = 0
            addr[{RECT_W}] = 8
            addr[{RECT_H}] = 8
            addr[{RECT_COLOR}] = 0
        else:
            plat_x1[i] = x
            plat_x2[i] = x + w
            plat_y[i]  = y

            addr[{RECT_X}] = x
            addr[{RECT_Y}] = y
            addr[{RECT_W}] = w
            addr[{RECT_H}] = h
            addr[{RECT_COLOR}] = color
        i = i + 1

    base = {RECT_MEM} + ladder_rect_base * {RECT_SIZE}
    base_idx = (current_level - 1) * LADDER_COUNT * 5

    i = 0
    while i < LADDER_COUNT:
        idx = base_idx + i * 5

        x = ladder_levels[idx]
        y = ladder_levels[idx + 1]
        w = ladder_levels[idx + 2]
        h = ladder_levels[idx + 3]
        color = ladder_levels[idx + 4]

        addr = base + i * {RECT_SIZE}

        if (w <= 0) | (h <= 0):
            lad_x1[i] = -1000
            lad_x2[i] = -900
            lad_y1[i] = 0
            lad_y2[i] = 0

            addr[{RECT_X}] = -1000
            addr[{RECT_Y}] = 0
            addr[{RECT_W}] = 8
            addr[{RECT_H}] = 8
            addr[{RECT_COLOR}] = 0
        else:
            lad_x1[i] = x
            lad_x2[i] = x + w
            lad_y1[i] = y
            lad_y2[i] = y + h

            addr[{RECT_X}] = x
            addr[{RECT_Y}] = y
            addr[{RECT_W}] = w
            addr[{RECT_H}] = h
            addr[{RECT_COLOR}] = color
        i = i + 1

def get_spawn_delay_for_level():
    idx = current_level - 1
    if idx < 0:
        idx = 0
    if idx >= MAX_LEVEL:
        idx = MAX_LEVEL - 1
    r = rand8()
    if r & 1:
        return spawn_delay_a[idx]
    return spawn_delay_b[idx]

def get_max_barrels_for_level():
    max_b = current_level
    if max_b > MAX_BARRELS:
        max_b = MAX_BARRELS
    return max_b

def apply_level_layout():
    set_level_layout_mode()
    update_level_colliders()

    if current_level == CRANE_LEVEL:


        base_index = (CRANE_LEVEL - 1) * DECOR_COUNT * 5
        addr = {RECT_MEM} + DECOR_OVERLAY_RECT_BASE * {RECT_SIZE}

        i = 0
        while i < DECOR_OVERLAY_COUNT:
            idx = base_index + i * 5
            x = decor_levels[idx]
            y = decor_levels[idx + 1]
            w = decor_levels[idx + 2]
            h = decor_levels[idx + 3]
            color = decor_levels[idx + 4]

            addr[{RECT_X}] = x
            addr[{RECT_Y}] = y
            addr[{RECT_W}] = w
            addr[{RECT_H}] = h
            addr[{RECT_COLOR}] = color

            i = i + 1
            addr = addr + {RECT_SIZE}


        idx = current_level - 1
        if idx < 0:
            idx = 0
        if idx >= MAX_LEVEL:
            idx = MAX_LEVEL - 1
        barrel_speed = barrel_speed_level[idx]

        spawn_delay = get_spawn_delay_for_level()
        spawn_timer = 0

        snow_phase   = 0
        window_phase = 0
        sun_phase    = 0

        snow_anim_timer   = 0
        window_anim_timer = 0
        sun_anim_timer    = 0

        vertical_spawn_pending = 0
        vertical_spawn_timer   = 0

        if current_level == 8:
            player_grav = 0
            player_lowgrav_active = 1
            player_lowgrav_timer = 0
        else:
            player_grav = grav
            player_lowgrav_active = 0

        wind_dir = 0
        wind_timer = 0

        lava_active       = 0
        lava_start_timer  = 0
        lava_anim_timer   = 0
        if current_level == LAVA_LEVEL:
            lava_level_y = ground_y
        else:
            lava_level_y = screen_h + 16

        crane_state       = 0
        crane_dir         = 0
        crane_offset      = 0
        crane_speed       = 0
        crane_rest_timer  = 0
        crane_rest_delay  = 0


        crane_hide_all()
        return


    base_index = (current_level - 1) * DECOR_COUNT * 5
    addr = {RECT_MEM} + decor_rect_base * {RECT_SIZE}

    i = 0
    while i < DECOR_COUNT:
        idx = base_index + i * 5
        x = decor_levels[idx]
        y = decor_levels[idx + 1]
        w = decor_levels[idx + 2]
        h = decor_levels[idx + 3]
        color = decor_levels[idx + 4]

        addr[{RECT_X}] = x
        addr[{RECT_Y}] = y
        addr[{RECT_W}] = w
        addr[{RECT_H}] = h
        addr[{RECT_COLOR}] = color

        i = i + 1
        addr = addr + {RECT_SIZE}


    idx = current_level - 1
    if idx < 0:
        idx = 0
    if idx >= MAX_LEVEL:
        idx = MAX_LEVEL - 1
    barrel_speed = barrel_speed_level[idx]

    spawn_delay = get_spawn_delay_for_level()
    spawn_timer = 0

    snow_phase   = 0
    window_phase = 0
    sun_phase    = 0

    snow_anim_timer   = 0
    window_anim_timer = 0
    sun_anim_timer    = 0

    vertical_spawn_pending = 0
    vertical_spawn_timer   = 0

    if current_level == 8:
        player_grav = grav - 1
        if player_grav < 1:
            player_grav = 1
    else:
        player_grav = grav

    invert_control_active = 0
    invert_control_timer  = 0

    wind_dir = 0
    wind_timer = 0

    lava_active       = 0
    lava_start_timer  = 0
    lava_anim_timer   = 0
    if current_level == LAVA_LEVEL:
        lava_level_y = ground_y
    else:
        lava_level_y = screen_h + 16

    crane_state       = 0
    crane_dir         = 0
    crane_offset      = 0
    crane_speed       = 0
    crane_rest_timer  = 0
    crane_rest_delay  = 0


    if current_level == CRANE_LEVEL:
        crane_hide_all()


def reset_menu_heroes():
    # сброс фаз и таймеров
    menu_hero_phase = 0
    menu_hero_timer = 0
    menu_hero_move_step = 0
    menu_hero_move_timer = 0
    menu_hero_pause_timer = 0

    # вернуть все части донки и принцессы на базовые позиции
    base = {RECT_MEM}
    i = 0
    while i < menu_hero_count:
        idx = menu_hero_indices[i]
        addr = base + idx * {RECT_SIZE}

        base_x = menu_hero_base_x[i]
        base_y = menu_hero_base_y[i]

        addr[{RECT_X}] = base_x
        addr[{RECT_Y}] = base_y

        i = i + 1


def update_menu_heroes():
    # если героев нет (на всякий случай) — ничего не делаем
    if menu_hero_count == 0:
        return

    base = {RECT_MEM}

    # ===== ВЕРТИКАЛЬНОЕ "ДЫХАНИЕ" =====
    menu_hero_timer = menu_hero_timer + 1
    if menu_hero_timer >= 6:
        menu_hero_timer = 0
        menu_hero_phase = (menu_hero_phase + 1) & 7

    dy = 0
    if menu_hero_phase < 2:
        dy = 0
    elif menu_hero_phase < 4:
        dy = 1
    elif menu_hero_phase < 6:
        dy = 2
    else:
        dy = 1

    # ===== ГОРИЗОНТАЛЬНОЕ ДВИЖЕНИЕ СЛЕВА НАПРАВО С ПЕРЕЗАПУСКОМ =====
    #
    # идея:
    #   menu_hero_move_step идёт от 0 до 79
    #   dx = menu_hero_move_step - 40
    #     => сначала -40 (слева, под маской),
    #        потом постепенно двигаемся вправо до +39,
    #        потом шаг сбрасывается в 0, включается пауза, и цикл повторяется
    #
    menu_hero_move_timer = menu_hero_move_timer + 1
    if menu_hero_move_timer >= 4:       # скорость движения по X (чем больше, тем медленнее)
        menu_hero_move_timer = 0

        if menu_hero_pause_timer > 0:
            menu_hero_pause_timer = menu_hero_pause_timer - 1
        else:
            menu_hero_move_step = menu_hero_move_step + 1
            if menu_hero_move_step >= 300:
                # закончили проход слева направо — делаем паузу и сбрасываемся влево
                menu_hero_move_step = 0
                menu_hero_pause_timer = 1   # длина паузы в кадрах перед следующим "заездом"

    dx = menu_hero_move_step - 100

    # ===== ПРИМЕНИТЬ X И Y КО ВСЕМ ЧАСТЯМ ГЕРОЕВ =====
    i = 0
    while i < menu_hero_count:
        idx = menu_hero_indices[i]
        addr = base + idx * {RECT_SIZE}

        base_x = menu_hero_base_x[i]
        base_y = menu_hero_base_y[i]

        addr[{RECT_X}] = base_x + dx
        addr[{RECT_Y}] = base_y + dy

        i = i + 1



def frame_menu():

    base = {RECT_MEM}
    
    k = peek({KEY_MEM + KEY_A})
    if k & (menu_k_prev <= 0):
        # "одиночное" нажатие: увеличиваем уровень
        current_level = current_level + 1
        if current_level > MAX_LEVEL:
            current_level = 1   # зацикливаем: после 8 → 1
    menu_k_prev = k

    
    # анимация Донки и принцессы в окне меню
    update_menu_heroes()

    # ===== ДЫХАНИЕ СТРЕЛКИ =====
    menu_button_timer = menu_button_timer + 1
    if menu_button_timer >= MENU_BUTTON_ANIM_DELAY:
        menu_button_timer = 0
        if menu_button_phase == 0:
            menu_button_phase = 1
        else:
            menu_button_phase = 0

    # текущий цвет стрелки
    current_arrow_color = menu_button_color1
    if menu_button_phase:
        current_arrow_color = menu_button_color2

    # применяем цвет ко всем прямоугольникам стрелки
    i = 0
    while i < menu_button_count:
        idx = menu_button_indices[i]
        addr = base + idx * {RECT_SIZE}
        addr[{RECT_COLOR}] = current_arrow_color
        i = i + 1

    # ===== СЧЁТЧИКИ УРОВНЕЙ (БЕЗ АНИМАЦИИ, КАК РАНЬШЕ) =====
    visible = current_level
    if visible < 1:
        visible = 1
    if visible > MENU_LEVEL_COUNTER_COUNT:
        visible = MENU_LEVEL_COUNTER_COUNT

    i = 0
    while i < MENU_LEVEL_COUNTER_COUNT:
        idx = MENU_LEVEL_COUNTER_FIRST + i
        addr = base + idx * {RECT_SIZE}
        if i < visible:
            addr[{RECT_X}] = menu_level_cell_x[i]
            addr[{RECT_Y}] = menu_level_cell_y
            addr[{RECT_W}] = menu_level_cell_w
            addr[{RECT_H}] = menu_level_cell_h
            addr[{RECT_COLOR}] = menu_level_cell_color   # фиксированный цвет, без дыхания
        else:
            addr[{RECT_X}] = -1000
            addr[{RECT_Y}] = 0
        i = i + 1

    # запуск уровня (как у тебя сейчас — по RIGHT)
    if peek({KEY_MEM + KEY_RIGHT}):
        set_level_layout_mode() 
        load_bg_level()
        reset_game()
        apply_level_layout()
        game_state = STATE_PLAY



def frame_final():

    base_decor = {RECT_MEM} + decor_rect_base * {RECT_SIZE}



    idle_timer = idle_timer + 1
    if idle_timer < 6:

        if peek({KEY_MEM + KEY_RIGHT}):
            current_level = 1
            set_level_layout_mode()
            reset_game()
            apply_level_layout()
            load_bg_menu()
            reset_menu_heroes()
            game_state = STATE_MENU
        return
    idle_timer = 0


    donkey_idle_phase = (donkey_idle_phase + 1) & 7

    dy_donkey = 0
    if donkey_idle_phase < 2:
        dy_donkey = 0
    elif donkey_idle_phase < 4:
        dy_donkey = 1
    elif donkey_idle_phase < 6:
        dy_donkey = 2
    else:
        dy_donkey = 1


    i = 0
    while i < final_donkey_body_count:
        idx = final_donkey_body_indices[i]
        addr = base_decor + idx * {RECT_SIZE}
        base_y = final_donkey_body_base_y[i]
        addr[{RECT_Y}] = base_y + dy_donkey
        i = i + 1


    i = 0
    while i < final_donkey_limb_count:
        idx = final_donkey_limb_indices[i]
        addr = base_decor + idx * {RECT_SIZE}
        base_y = final_donkey_limb_base_y[i]
        addr[{RECT_Y}] = base_y + dy_donkey
        i = i + 1


    hero_idle_phase = (hero_idle_phase + 1) & 7
    hero_phase = (hero_idle_phase + 2) & 7

    dy_hero = 0
    if hero_phase < 2:
        dy_hero = 0
    elif hero_phase < 4:
        dy_hero = 1
    elif hero_phase < 6:
        dy_hero = 2
    else:
        dy_hero = 1

    if dy_hero > 1:
        dy_hero = 1

    i = 0
    while i < final_shrek_count:
        idx = final_shrek_indices[i]
        addr = base_decor + idx * {RECT_SIZE}
        base_y = final_shrek_base_y[i]
        addr[{RECT_Y}] = base_y + dy_hero
        i = i + 1


    princess_idle_phase = (princess_idle_phase + 1) & 7
    princess_phase = (princess_idle_phase + 4) & 7

    dy_prin = 0
    if princess_phase < 2:
        dy_prin = 0
    elif princess_phase < 4:
        dy_prin = 1
    elif princess_phase < 6:
        dy_prin = 2
    else:
        dy_prin = 1
    if dy_prin > 1:
        dy_prin = 1

    i = 0
    while i < final_fiona_count:
        idx = final_fiona_indices[i]
        addr = base_decor + idx * {RECT_SIZE}
        base_y = final_fiona_base_y[i]
        addr[{RECT_Y}] = base_y + dy_prin
        i = i + 1


    if peek({KEY_MEM + KEY_RIGHT}):
        current_level = 1
        set_level_layout_mode()
        reset_game()
        apply_level_layout()
        load_bg_menu()
        game_state = STATE_MENU



def update_level_effects():
    if current_level == 6:
        wind_timer = wind_timer + 1
        if wind_timer >= wind_change_interval:
            wind_timer = 0
            r = rand8()
            if r & 1:
                wind_dir = 1
            else:
                wind_dir = -1
    else:
        wind_dir = 0
        wind_timer = 0
    

    if current_level == 8:
        invert_control_timer = invert_control_timer + 1

        if invert_control_active:

            if invert_control_timer >= invert_control_on_frames:
                invert_control_active = 0
                invert_control_timer = 0
        else:

            if invert_control_timer >= invert_control_off_frames:
                invert_control_active = 1
                invert_control_timer = 0
    else:

        invert_control_active = 0
        invert_control_timer = 0

def update():
    update_level_effects()
    handle_input()
    update_player()
    update_barrels()
    update_decor()
    check_collisions()
    check_win()

def handle_input():
    up    = peek({KEY_MEM + KEY_UP})
    down  = peek({KEY_MEM + KEY_DOWN})
    left  = peek({KEY_MEM + KEY_LEFT})
    right = peek({KEY_MEM + KEY_RIGHT})

    if current_level == 8:
        if invert_control_active:
            tmp   = left
            left  = right
            right = tmp

    speed = walk_speed

    if current_level == 5:
        if speed > 1:
            speed = speed - 1

    if current_level == 6:
        if wind_dir > 0:
            if left:
                if speed > 1:
                    speed = speed - 1
        if wind_dir < 0:
            if right:
                if speed > 1:
                    speed = speed - 1

    player_vx = 0

    cx = player_x + player_half_w
    top = player_y
    bottom = player_y + player_h

    on_ladder = 0
    ladder_cx = 0

    i = 0
    while i < LADDER_COUNT:
        x1 = lad_x1[i]
        x2 = lad_x2[i]
        y1 = lad_y1[i]
        y2 = lad_y2[i]
        if (cx >= x1) & (cx <= x2) & (bottom >= y1) & (top <= y2):
            on_ladder = 1
            ladder_cx = (x1 + x2) >> 1
        i = i + 1

    if left:
        climbing_flag = 0
        player_vx = -speed
        player_dir = -1
    elif right:
        climbing_flag = 0
        player_vx = speed
        player_dir = 1
    else:
        if on_ladder:
            if up:
                climbing_flag = 1
                climb_ladder_x = ladder_cx
                player_vy = -climb_speed
            elif down:
                climbing_flag = 1
                climb_ladder_x = ladder_cx
                player_vy = climb_speed
            else:
                if climbing_flag == 0:
                    climbing_flag = 1
                    climb_ladder_x = ladder_cx
                player_vy = 0
        else:
            climbing_flag = 0

    if current_level == 6:
        if climbing_flag == 0:
            player_vx = player_vx + wind_dir

def find_platform_below_player(x, y, h):
    foot_x = x + player_half_w
    foot_y = y + h
    best_y = 0
    found = 0

    i = 0
    while i < PLATFORM_COUNT:
        px1 = plat_x1[i]
        px2 = plat_x2[i]
        py  = plat_y[i]
        if (foot_x >= px1) & (foot_x <= px2):
            if (foot_y >= py - 4) & (foot_y <= py + 16):
                if (found == 0) | (py < best_y):
                    best_y = py
                    found = 1
        i = i + 1

    if found:
        return best_y
    return 0

def update_player_anim():
    base_player = {RECT_MEM} + player_rect_base * {RECT_SIZE}
    head = base_player + {RECT_SIZE}
    legL = base_player + {RECT_SIZE} * 2
    legR = base_player + {RECT_SIZE} * 3

    head[{RECT_X}] = 2
    head[{RECT_Y}] = -8

    if climbing_flag:
        moving_vert = 0
        if (player_vy < 0) | (player_vy > 0):
            moving_vert = 1

        if moving_vert:
            player_anim_timer = player_anim_timer + 1
            if player_anim_timer >= 6:
                player_anim_timer = 0
                if player_anim == 0:
                    player_anim = 1
                else:
                    player_anim = 0

            if player_anim == 0:
                legL[{RECT_X}] = 2
                legL[{RECT_Y}] = 12
                legR[{RECT_X}] = 10
                legR[{RECT_Y}] = 18
            else:
                legL[{RECT_X}] = 2
                legL[{RECT_Y}] = 18
                legR[{RECT_X}] = 10
                legR[{RECT_Y}] = 12
        else:
            legL[{RECT_X}] = 2
            legL[{RECT_Y}] = 14
            legR[{RECT_X}] = 10
            legR[{RECT_Y}] = 14
    else:
        moving = (player_vx < 0) | (player_vx > 0)
        if moving:
            player_anim_timer = player_anim_timer + 1
            if player_anim_timer >= 6:
                player_anim_timer = 0
                if player_anim == 0:
                    player_anim = 1
                else:
                    player_anim = 0
        else:
            player_anim_timer = 0
            player_anim = 0

        if player_anim == 0:
            legL[{RECT_X}] = 2
            legL[{RECT_Y}] = 14
            legR[{RECT_X}] = 10
            legR[{RECT_Y}] = 14
        else:
            if player_dir > 0:
                legL[{RECT_X}] = 1
                legL[{RECT_Y}] = 15
                legR[{RECT_X}] = 11
                legR[{RECT_Y}] = 13
            else:
                legL[{RECT_X}] = 3
                legL[{RECT_Y}] = 13
                legR[{RECT_X}] = 9
                legR[{RECT_Y}] = 15

def update_player():
    if climbing_flag == 0:
        if player_lowgrav_active:
            player_lowgrav_timer = player_lowgrav_timer + 1
            if player_lowgrav_timer >= LOW_GRAV_DELAY:
                player_lowgrav_timer = 0
                player_vy = player_vy + 1
        else:
            player_vy = player_vy + player_grav
        player_x = player_x + player_vx
        player_y = player_y + player_vy
    else:
        player_x = climb_ladder_x - player_half_w
        player_y = player_y + player_vy

    if player_x < 0:
        player_x = 0
    if player_x + player_w > screen_w:
        player_x = screen_w - player_w

    if climbing_flag == 0:
        py_under = find_platform_below_player(player_x, player_y, player_h)
        if py_under:
            target_y = py_under - player_h
            if player_y > target_y:
                player_y = target_y
                player_vy = 0

    floor_y = ground_y - player_h
    if player_y > floor_y:
        player_y = floor_y
        player_vy = 0

    body = {RECT_MEM} + player_rect_base * {RECT_SIZE}
    body[{RECT_X}] = player_x
    body[{RECT_Y}] = player_y + 4

    update_player_anim()

def spawn_one_barrel():
    max_b = get_max_barrels_for_level()

    active = 0
    i = 0
    while i < MAX_BARRELS:
        if barrel_active[i]:
            active = active + 1
        i = i + 1

    if active >= max_b:
        return

    i = 0
    while i < MAX_BARRELS:
        if barrel_active[i] == 0:
            barrel_active[i]  = 1
            barrel_type[i]    = 0
            barrel_x[i]       = barrel_spawn_x
            barrel_y[i]       = barrel_spawn_y
            barrel_vx[i]      = barrel_speed
            barrel_vy[i]      = 0
            barrel_falling[i] = 0

            barrel_set_rects(i, barrel_x[i], barrel_y[i])
            return
        i = i + 1

def spawn_vertical_barrel():
    max_b = get_max_barrels_for_level()

    active = 0
    i = 0
    while i < MAX_BARRELS:
        if barrel_active[i]:
            active = active + 1
        i = i + 1

    if active >= max_b:
        return

    i = 0
    while i < MAX_BARRELS:
        if barrel_active[i] == 0:
            barrel_active[i]  = 1
            barrel_type[i]    = 1

            r = rand8()
            offset = r & 15
            if r & 16:
                offset = -offset

            x = player_x + player_half_w - (barrel_w >> 1) + offset
            if x < 0:
                x = 0
            if x + barrel_w > screen_w:
                x = screen_w - barrel_w

            barrel_x[i]       = x
            barrel_y[i]       = -barrel_h
            barrel_vx[i]      = 0
            barrel_vy[i]      = 1
            barrel_falling[i] = 1

            barrel_set_rects(i, barrel_x[i], barrel_y[i])
            return
        i = i + 1

def start_spawn():
    r = rand8()
    if (r & 7) == 0:
        if vertical_spawn_pending == 0:
            vertical_spawn_pending = 1
            vertical_spawn_timer = 0
        else:
            spawn_one_barrel()
    else:
        spawn_one_barrel()

def update_one_barrel(i):
    if barrel_active[i] == 0:
        return

    if barrel_type[i] == 1:
        barrel_vy[i] = 5
        x = barrel_x[i]
        y = barrel_y[i] + barrel_vy[i]

        if y > screen_h + 40:
            barrel_active[i]  = 0
            barrel_x[i]       = -1000
            barrel_y[i]       = -1000
            barrel_vx[i]      = 0
            barrel_vy[i]      = 0
            barrel_falling[i] = 0
            barrel_hide(i)
            return

        barrel_x[i] = x
        barrel_y[i] = y
        barrel_set_rects(i, barrel_x[i], barrel_y[i])
        return

    old_vy = barrel_vy[i]
    barrel_vy[i] = barrel_vy[i] + grav

    x = barrel_x[i] + barrel_vx[i]
    y = barrel_y[i] + barrel_vy[i]

    foot_x = x + (barrel_w >> 1)
    foot_y = y + barrel_h
    best_y = 0
    found = 0

    j = 0
    while j < PLATFORM_COUNT:
        px1 = plat_x1[j]
        px2 = plat_x2[j]
        py  = plat_y[j]
        if (foot_x >= px1) & (foot_x <= px2):
            if (foot_y >= py - 4) & (foot_y <= py + 16):
                if (found == 0) | (py < best_y):
                    best_y = py
                    found = 1
        j = j + 1

    if found:
        target_y = best_y - barrel_h
        if y >= target_y:
            y = target_y
            if old_vy > 0:
                barrel_vx[i] = -barrel_vx[i]
            barrel_vy[i] = 0
            barrel_falling[i] = 0
    else:
        barrel_falling[i] = 1

    if y > screen_h + 40:
        barrel_active[i]  = 0
        x = -1000
        y = -1000
        barrel_vx[i]      = 0
        barrel_vy[i]      = 0
        barrel_falling[i] = 0
        barrel_hide(i)
        barrel_x[i] = x
        barrel_y[i] = y
        return

    barrel_x[i] = x
    barrel_y[i] = y
    barrel_set_rects(i, x, y)

def update_barrels():
    spawn_timer = spawn_timer + 1
    if spawn_timer >= spawn_delay:
        spawn_timer = 0
        start_spawn()

    if vertical_spawn_pending:
        vertical_spawn_timer = vertical_spawn_timer + 1
        if vertical_spawn_timer >= vertical_spawn_delay:
            vertical_spawn_timer = 0
            vertical_spawn_pending = 0
            spawn_vertical_barrel()

    i = 0
    while i < MAX_BARRELS:
        if barrel_active[i]:
            update_one_barrel(i)
        i = i + 1

def crane_hide_all():

    base_crane = {RECT_MEM} + OVERLAY_RECT_BASE * {RECT_SIZE}
    i = 0
    while i < crane_part_count:
        idx = crane_local_indices[i]
        addr = base_crane + idx * {RECT_SIZE}
        addr[{RECT_X}] = -1000
        addr[{RECT_Y}] = 0
        i = i + 1



def update_crane():

    if current_level != CRANE_LEVEL:
        return


    base_crane = {RECT_MEM} + OVERLAY_RECT_BASE * {RECT_SIZE}


    if crane_state == 0:
        crane_hide_all()

        crane_rest_timer = crane_rest_timer + 1


        if crane_rest_delay == 0:
            r = rand8()
            crane_rest_delay = 180 + (r & 127)

        if crane_rest_timer < crane_rest_delay:
            return


        crane_rest_timer = 0
        crane_rest_delay = 0

        r = rand8()
        if r & 1:
            crane_dir = 1
            crane_offset = CRANE_OFFSET_START_RIGHT
        else:
            crane_dir = -1
            crane_offset = CRANE_OFFSET_START_LEFT


        s = (rand8() & 3) + 5
        crane_speed = s

        crane_state = 1
        return


    if crane_dir > 0:
        crane_offset = crane_offset + crane_speed
    else:
        crane_offset = crane_offset - crane_speed


    i = 0
    while i < crane_part_count:
        idx = crane_local_indices[i]
        addr = base_crane + idx * {RECT_SIZE}

        bx = crane_base_x[i]
        by = crane_base_y[i]

        addr[{RECT_X}] = bx + crane_offset
        addr[{RECT_Y}] = by

        i = i + 1


    if crane_dir > 0:
        if crane_offset > CRANE_OFFSET_FINISH_RIGHT:
            crane_state      = 0
            crane_rest_timer = 0
            crane_speed      = 0
            crane_hide_all()
    else:
        if crane_offset < CRANE_OFFSET_FINISH_LEFT:
            crane_state      = 0
            crane_rest_timer = 0
            crane_speed      = 0
            crane_hide_all()


        

def update_decor():
    base_decor = {RECT_MEM} + decor_rect_base * {RECT_SIZE}


    if current_level == SNOW_LEVEL:
        snow_anim_timer = snow_anim_timer + 1
        if snow_anim_timer < SNOW_ANIM_DELAY:
            return
        snow_anim_timer = 0


        snow_phase = snow_phase + 1

        i = 0
        while i < SNOW_COUNT:
            idx = snow_indices[i]
            addr = base_decor + idx * {RECT_SIZE}


            y = addr[{RECT_Y}] + 1
            if y > screen_h:
                y = 0


            base_x = snow_base_x[i]
            phase = snow_phase + (i * 2)
            phase = phase & SNOW_WAVE_MASK
            dx = snow_wave_dx[phase]

            addr[{RECT_X}] = base_x + dx
            addr[{RECT_Y}] = y

            i = i + 1
        return




    if current_level == WINDOW_LEVEL:

        window_anim_timer = window_anim_timer + 1
        if window_anim_timer >= WINDOW_ANIM_DELAY:
            window_anim_timer = 0
            window_phase = window_phase + 1
            if window_phase >= 32:
                window_phase = 0

            i = 0
            while i < WINDOW_COUNT:
                idx = window_indices[i]
                addr = base_decor + idx * {RECT_SIZE}
                phase = window_phase + i
                if phase & 4:
                    addr[{RECT_COLOR}] = window_color_on
                else:
                    addr[{RECT_COLOR}] = window_color_off
                i = i + 1


        if moon_shake_active == 0:

            moon_rest_timer = moon_rest_timer + 1


            addr = base_decor + moon_main_index * {RECT_SIZE}
            addr[{RECT_X}] = moon_main_base_x
            addr[{RECT_Y}] = moon_main_base_y

            i = 0
            while i < moon_glare_count:
                idx = moon_glare_indices[i]
                addr = base_decor + idx * {RECT_SIZE}
                gx = moon_glare_base_x[i]
                gy = moon_glare_base_y[i]
                addr[{RECT_X}] = gx
                addr[{RECT_Y}] = gy
                i = i + 1


            i = 0
            while i < moon_light_count:
                idx = moon_light_indices[i]
                addr = base_decor + idx * {RECT_SIZE}
                lx = moon_light_base_x[i]
                ly = moon_light_base_y[i]
                addr[{RECT_X}] = lx
                addr[{RECT_Y}] = ly
                i = i + 1


            if moon_rest_timer >= MOON_REST_DELAY:
                moon_rest_timer   = 0
                moon_shake_active = 1
                moon_phase        = 0
                moon_anim_timer   = 0

            return


        moon_anim_timer = moon_anim_timer + 1
        if moon_anim_timer >= MOON_ANIM_DELAY:
            moon_anim_timer = 0
            moon_phase = moon_phase + 1
            if moon_phase >= 32:

                moon_phase        = 0
                moon_shake_active = 0


        main_dx = 0
        main_dy = 0


        glare_dx0 = 0
        glare_dy0 = 0

        if moon_phase >= 24:

            p_main = moon_phase - 24
            if p_main >= 8:
                p_main = p_main & 7


            if (p_main == 0) | (p_main == 4):
                main_dx = 1
            elif (p_main == 1) | (p_main == 5):
                main_dy = 1
            elif (p_main == 2) | (p_main == 6):
                main_dx = -1
            else:
                main_dy = -1


            p_glare_base = (p_main + 2) & 7
            if (p_glare_base == 0) | (p_glare_base == 4):
                glare_dx0 = 1
            elif (p_glare_base == 1) | (p_glare_base == 5):
                glare_dy0 = 1
            elif (p_glare_base == 2) | (p_glare_base == 6):
                glare_dx0 = -1
            else:
                glare_dy0 = -1


        addr = base_decor + moon_main_index * {RECT_SIZE}
        addr[{RECT_X}] = moon_main_base_x + main_dx
        addr[{RECT_Y}] = moon_main_base_y + main_dy


        i = 0
        while i < moon_light_count:
            idx = moon_light_indices[i]
            addr = base_decor + idx * {RECT_SIZE}
            lx = moon_light_base_x[i]
            ly = moon_light_base_y[i]

            dx = 0
            dy = 0

            if moon_phase >= 24:

                p_main = moon_phase - 24
                if p_main >= 8:
                    p_main = p_main & 7



                delay = (moon_light_count - 1 - i) << 1
                p = (p_main - delay) & 7


                if (p == 0) | (p == 4):
                    dx = 1
                elif (p == 1) | (p == 5):
                    dy = 1
                elif (p == 2) | (p == 6):
                    dx = -1
                else:
                    dy = -1

            addr[{RECT_X}] = lx + dx
            addr[{RECT_Y}] = ly + dy

            i = i + 1


        i = 0
        while i < moon_glare_count:
            idx = moon_glare_indices[i]
            addr = base_decor + idx * {RECT_SIZE}
            gx = moon_glare_base_x[i]
            gy = moon_glare_base_y[i]

            dx = 0
            dy = 0

            if moon_phase >= 24:

                p_main = moon_phase - 24
                if p_main >= 8:
                    p_main = p_main & 7


                if i == 0:

                    dx = glare_dx0
                    dy = glare_dy0
                elif i == 1:

                    if (p_main & 1) == 0:
                        dx = glare_dx0
                        dy = glare_dy0
                elif i == 2:

                    if (p_main & 3) == 0:
                        dx = glare_dx0
                        dy = glare_dy0
                else:

                    if p_main == 0:
                        dx = glare_dx0
                        dy = glare_dy0

            addr[{RECT_X}] = gx + dx
            addr[{RECT_Y}] = gy + dy

            i = i + 1

        return




    if current_level == SUN_LEVEL:

        sun_anim_timer = sun_anim_timer + 1
        if sun_anim_timer < SUN_ANIM_DELAY:
            return
        sun_anim_timer = 0

        sun_phase = sun_phase + 1
        if sun_phase >= 32:
            sun_phase = 0


        breath = 0
        p = sun_phase
        if p < 8:
            breath = 0
        elif p < 16:
            breath = 1
        elif p < 24:
            breath = 2
        else:
            breath = 1


        i = 0
        while i < sun_layer_count:
            idx = sun_layer_indices[i]
            addr = base_decor + idx * {RECT_SIZE}

            bw = sun_layer_base_w[i]
            bh = sun_layer_base_h[i]


            addr[{RECT_W}] = bw + breath
            addr[{RECT_H}] = bh + breath

            i = i + 1




        water_anim_timer = water_anim_timer + 1
        if water_anim_timer >= 3:
            water_anim_timer = 0


            water_phase = water_phase + 1
            if water_phase >= BEACH_WATER_PHASE_MAX:
                water_phase = 0







        breath = 0
        if water_phase >= 4:
            if water_phase < 8:
                breath = 1
            elif water_phase < 12:
                breath = 2
            elif water_phase < 16:
                breath = 1
            else:
                breath = 0


        i = 0
        while i < water_count:
            idx = water_indices[i]
            addr = base_decor + idx * {RECT_SIZE}
            by = water_base_y[i]

            dy = 0
            if breath == 1:
                dy = 1
            elif breath == 2:
                dy = 2

            addr[{RECT_Y}] = by + dy
            i = i + 1

    

    if current_level == FOREST_LEVEL:

        forest_anim_timer = forest_anim_timer + 1
        if forest_anim_timer < FOREST_ANIM_DELAY:
            return
        forest_anim_timer = 0


        forest_phase_move = forest_phase_move + 1
        if forest_phase_move >= FOREST_PATH_LEN:
            forest_phase_move = 0


        forest_phase_color = forest_phase_color + 1
        if forest_phase_color >= 16:
            forest_phase_color = 0


        i = 0
        while i < FOREST_FIREFLY_COUNT:
            idx = FOREST_FIREFLY_INDICES[i]
            addr = base_decor + idx * {RECT_SIZE}
            bx = FOREST_FIREFLY_BASE_X[i]
            by = FOREST_FIREFLY_BASE_Y[i]


            phase = forest_phase_move + (i * 2)
            phase = phase & FOREST_PATH_MASK

            dx = FOREST_PATH_DX[phase]
            dy = FOREST_PATH_DY[phase]

            addr[{RECT_X}] = bx + dx
            addr[{RECT_Y}] = by + dy


            if (forest_phase_color & 4):
                addr[{RECT_COLOR}] = FOREST_FIREFLY_COLOR2
            else:
                addr[{RECT_COLOR}] = FOREST_FIREFLY_COLOR1

            i = i + 1



        i = 0
        while i < FOREST_GLOW_COUNT:
            idx = FOREST_GLOW_INDICES[i]


            if idx != 24:
                addr = base_decor + idx * {RECT_SIZE}
                gx = FOREST_GLOW_BASE_X[i]
                gy = FOREST_GLOW_BASE_Y[i]


                phase2 = forest_phase_move + i
                phase2 = phase2 & FOREST_PATH_MASK

                dx = 0
                dy = 0

                if (phase2 & 1) == 0:
                    dx = FOREST_PATH_DX[phase2]
                    dy = FOREST_PATH_DY[phase2]

                addr[{RECT_X}] = gx + dx
                addr[{RECT_Y}] = gy + dy

                base_color = FOREST_GLOW_COLOR_BASE[i]
                lit_color  = FOREST_GLOW_COLOR_LIT[i]


                if (forest_phase_color & 4):
                    addr[{RECT_COLOR}] = lit_color
                else:
                    addr[{RECT_COLOR}] = base_color

            i = i + 1

        return
    

    if current_level == CRANE_LEVEL:
        update_crane()
        return


    if current_level == 6:

        sun_anim_timer = sun_anim_timer + 1
        if sun_anim_timer < SUN_ANIM_DELAY:
            return
        sun_anim_timer = 0


        sun_phase = sun_phase + 1
        if sun_phase >= 64:
            sun_phase = 0

        half = 32
        if sun_phase < half:
            t = sun_phase
        else:
            t = half - (sun_phase - half)


        breath = 0
        if t >= 8:
            breath = breath + 1
        if t >= 16:
            breath = breath + 1
        if t >= 24:
            breath = breath + 1


        sun_idx = 9
        addr = base_decor + sun_idx * {RECT_SIZE}

        base_w = 73
        base_h = 60

        addr[{RECT_W}] = base_w + breath
        addr[{RECT_H}] = base_h + breath



        if wind_dir != 0:
            sandstorm_anim_timer = sandstorm_anim_timer + 1
            if sandstorm_anim_timer >= SANDSTORM_ANIM_DELAY:
                sandstorm_anim_timer = 0

                i = 0
                while i < 4:
                    idx = 19 + i
                    waddr = base_decor + idx * {RECT_SIZE}

                    x = waddr[{RECT_X}]
                    y = waddr[{RECT_Y}]
                    w = waddr[{RECT_W}]


                    speed = 3
                    if i & 1:
                        speed = 4




                    r = rand8() & 3
                    if r == 0:
                        y = y - 1
                    elif r == 1:
                        y = y + 1



                    if wind_dir > 0:
                        x = x + speed
                        if x > screen_w:
                            x = -w
                            y = 40 + (rand8() & 127)
                    else:
                        x = x - speed
                        if x + w < 0:
                            x = screen_w
                            y = 40 + (rand8() & 127)

                    waddr[{RECT_X}] = x
                    waddr[{RECT_Y}] = y

                    i = i + 1


        return





    if current_level == LAVA_LEVEL:

        lava_start_timer = lava_start_timer + 1
        if lava_active == 0:
            if lava_start_timer >= lava_start_delay:
                lava_active = 1
        else:
            lava_anim_timer = lava_anim_timer + 1
            if lava_anim_timer >= lava_anim_delay:
                lava_anim_timer = 0


                lava_level_y = lava_level_y - 1
                if lava_level_y < 0:
                    lava_level_y = 0


                lava_bubble_phase = (lava_bubble_phase + 1) & 7


        addr = base_decor + LAVA_MAIN_INDEX * {RECT_SIZE}
        addr[{RECT_Y}] = lava_level_y
        addr[{RECT_H}] = screen_h - lava_level_y


        i = 0
        while i < lava_bubble_count:
            idx = lava_bubble_indices[i]
            addr = base_decor + idx * {RECT_SIZE}

            off_y = lava_bubble_offset_y[i]
            base_h = lava_bubble_base_h[i]



            y = lava_level_y + off_y
            h = base_h



            if i > 0:
                p = lava_bubble_phase
                stretch = 0
                if (p == 1) | (p == 7):
                    stretch = 1
                elif (p == 2) | (p == 6):
                    stretch = 2
                elif p == 3:
                    stretch = 3



                h = base_h + stretch
                y = y - stretch

            addr[{RECT_Y}] = y
            addr[{RECT_H}] = h

            i = i + 1

        return




    if current_level == SPACE_LEVEL:

        idx = space_core_star_local_index
        addr = base_decor + idx * {RECT_SIZE}

        if invert_control_active:
            addr[{RECT_COLOR}] = space_core_star_color_bright
        else:
            addr[{RECT_COLOR}] = space_core_star_color_dark



        rocket_timer = rocket_timer + 1
        if rocket_timer >= ROCKET_CYCLE_FRAMES:
            rocket_timer = 0



        if rocket_timer < ROCKET_FLY_FRAMES:

            t = rocket_timer



            offset = t * ROCKET_SPEED - ROCKET_START_SHIFT


            i = 0
            while i < space_rocket_body_count:
                idx = space_rocket_body_indices[i]
                addr = base_decor + idx * {RECT_SIZE}

                bx = space_rocket_body_base_x[i]
                by = space_rocket_body_base_y[i]

                addr[{RECT_X}] = bx + offset
                addr[{RECT_Y}] = by

                i = i + 1


            fire_phase = rocket_timer & 7
            fire_dx = 0
            if (fire_phase == 1) | (fire_phase == 5):
                fire_dx = 1
            elif (fire_phase == 3) | (fire_phase == 7):
                fire_dx = -1

            i = 0
            while i < space_rocket_fire_count:
                idx = space_rocket_fire_indices[i]
                addr = base_decor + idx * {RECT_SIZE}

                bx = space_rocket_fire_base_x[i]
                by = space_rocket_fire_base_y[i]

                addr[{RECT_X}] = bx + offset + fire_dx
                addr[{RECT_Y}] = by

                i = i + 1
        else:

            i = 0
            while i < space_rocket_body_count:
                idx = space_rocket_body_indices[i]
                addr = base_decor + idx * {RECT_SIZE}
                addr[{RECT_X}] = -1000
                addr[{RECT_Y}] = 0
                i = i + 1

            i = 0
            while i < space_rocket_fire_count:
                idx = space_rocket_fire_indices[i]
                addr = base_decor + idx * {RECT_SIZE}
                addr[{RECT_X}] = -1000
                addr[{RECT_Y}] = 0
                i = i + 1


        return

    
    


def check_collisions():
    px1 = player_x
    py1 = player_y
    px2 = px1 + player_w
    py2 = py1 + player_h

    i = 0
    while i < MAX_BARRELS:
        if barrel_active[i]:
            bx1 = barrel_x[i]
            by1 = barrel_y[i]
            bx2 = bx1 + barrel_w
            by2 = by1 + barrel_h

            if (px1 < bx2) & (px2 > bx1) & (py1 < by2) & (py2 > by1):
                game_over()
                return
        i = i + 1

    if current_level == LAVA_LEVEL:
        if lava_active:
            if py2 >= lava_level_y:
                game_over()
                return

def check_win():
    px1 = player_x
    py1 = player_y
    px2 = px1 + player_w
    py2 = py1 + player_h

    pr = {RECT_MEM} + princess_rect_base * {RECT_SIZE}
    rx1 = pr[{RECT_X}]
    ry1 = pr[{RECT_Y}]
    rx2 = rx1 + princess_w
    ry2 = ry1 + princess_h

    if (px1 < rx2) & (px2 > rx1) & (py1 < ry2) & (py2 > ry1):
        win_game()

def game_over():
    body = {RECT_MEM} + player_rect_base * {RECT_SIZE}

    y = body[{RECT_Y}]
    j = 0
    while j < 4:
        body[{RECT_Y}] = y
        i = 0
        while i < 15:
            wait()
            i = i + 1
        body[{RECT_Y}] = -1000
        i = 0
        while i < 30:
            wait()
            i = i + 1
        j = j + 1
    current_level = 1
    reset_game()
    apply_level_layout()
    load_bg_menu()
    reset_menu_heroes()
    game_state = STATE_MENU

def win_game():
    pr = {RECT_MEM} + princess_rect_base * {RECT_SIZE}
    y = pr[{RECT_Y}]
    j = 0
    while j < 4:
        pr[{RECT_Y}] = y
        i = 0
        while i < 15:
            wait()
            i = i + 1
        pr[{RECT_Y}] = -1000
        i = 0
        while i < 30:
            wait()
            i = i + 1
        j = j + 1

    if current_level < MAX_LEVEL:
        current_level = current_level + 1
        set_level_layout_mode()
        reset_game()
        apply_level_layout()
        load_bg_menu()
        reset_menu_heroes()
        game_state = STATE_MENU
    else:
        load_bg_final()
        game_state = STATE_FINAL
        final_anim_timer = 0
        final_phase      = 0

def reset_game():
    player_x = player_start_x
    player_y = player_start_y
    player_vx = 0
    player_vy = 0
    climbing_flag = 0
    climb_ladder_x = 0
    player_anim = 0
    player_anim_timer = 0
    player_dir = 1
    player_lowgrav_active = 0
    player_lowgrav_timer = 0
    invert_control_active = 0
    invert_control_timer  = 0
    
    i = 0
    while i < MAX_BARRELS:
        barrel_active[i]  = 0
        barrel_type[i]    = 0
        barrel_x[i]       = -1000
        barrel_y[i]       = -1000
        barrel_vx[i]      = 0
        barrel_vy[i]      = 0
        barrel_falling[i] = 0
        barrel_hide(i)
        i = i + 1

    spawn_timer = 0
    vertical_spawn_pending = 0
    vertical_spawn_timer   = 0

    body = {RECT_MEM} + player_rect_base * {RECT_SIZE}

    body[{RECT_X}] = player_x
    body[{RECT_Y}] = player_y + 4

def load_bg_menu():
    copy(bg_data_menu, {RECT_MEM}, BG_DATA_MENU_SIZE)

def load_bg_final():
    copy(bg_data_final, {RECT_MEM}, BG_DATA_FINAL_SIZE)

def load_bg_level():
    idx = current_level
    if idx < 1:
        idx = 1
    if idx > MAX_LEVEL:
        idx = MAX_LEVEL

    if idx == 1:
        copy(bg_data_level1, {RECT_MEM}, BG_DATA_LEVEL1_SIZE)
    elif idx == 2:
        copy(bg_data_level2, {RECT_MEM}, BG_DATA_LEVEL2_SIZE)
    elif idx == 3:
        copy(bg_data_level3, {RECT_MEM}, BG_DATA_LEVEL3_SIZE)
    elif idx == 4:
        copy(bg_data_level_overlay, {RECT_MEM}, BG_DATA_LEVEL_OVERLAY_SIZE)
    elif idx == 5:
        copy(bg_data_level5, {RECT_MEM}, BG_DATA_LEVEL5_SIZE)
    elif idx == 6:
        copy(bg_data_level6, {RECT_MEM}, BG_DATA_LEVEL6_SIZE)
    elif idx == 7:
        copy(bg_data_level7, {RECT_MEM}, BG_DATA_LEVEL7_SIZE)
    else:
        copy(bg_data_level8, {RECT_MEM}, BG_DATA_LEVEL8_SIZE)

def copy(src, dst, size):
    end = src + size
    while src != end:
        dst[0] = src[0]
        src = src + 1
        dst = dst + 1
""")
