from brus16 import *

save_game('sine.bin', f'''
def main():
    poke({VOICES_MEM + VOICE_ABS}, 1)
    poke({VOICES_MEM + VOICE_STEP}, {get_freq(440)})
    poke({VOICES_MEM + VOICE_AMP}, {get_vol(0.1)})
    poke({VOICES_MEM + VOICE_DECAY}, {get_decay(1000)})
    while 1:
        wait()
        poke({VOICES_MEM + VOICE_AMP}, 0)
''')
