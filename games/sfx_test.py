from brus16 import *

SFX_RADAR = [33792, 1, 1783, 3277, 32333, 0, 1014, 1024, 32333, 0, 1027, 1024, 32586, 0, 1022, 1024, 32586, 1, 32834, 0, 60]

SFX_POS = 0
SFX_COUNT = 1
SFX_LOOP = 2
SFX_SIZE = 3
SFX_DATA = 4

save_game('sfx_test.bin', f'''
def main():
    while 1:
        sfx_play(sfx_radar)
        wait()

def sfx_play(sfx):
    if sfx[{SFX_COUNT}] > 0:
        sfx[{SFX_COUNT}] -= 1
        return
    pos = sfx[{SFX_POS}]
    if pos >= sfx[{SFX_SIZE}]:
        if sfx[{SFX_LOOP}] == 0:
            return
        pos = 0
    data = sfx + {SFX_DATA}
    do_params = 1
    while do_params:
        p = data[pos]
        pos += 1
        idx = p & 63
        end = idx + ((p >> 6) & 63)
        if p >> 15:
            do_params = 0
        while idx < end:
            poke({VOICE_MEM} + idx, data[pos])
            pos += 1
            idx += 1
    sfx[{SFX_COUNT}] = data[pos]
    sfx[{SFX_POS}] = pos + 1

sfx_radar = {[0, 0, 1, len(SFX_RADAR)] + SFX_RADAR}
''')
