from brus16 import *

asm = save_game('sine.bin', f'''
def main():
    freq = {get_freq(880)}
    poke({OSC_MEM + OSC_ABS}, 1)
    poke({OSC_MEM + OSC_AMP}, {get_vol(0.1)})
    poke({OSC_MEM + OSC_DECAY}, {get_decay(10)})
    mod = 100
    while 1:
        poke({OSC_MEM + OSC_STEP}, freq + mod)
        mod = -mod
        wait()
        if freq > 0:
            freq -= 1
        poke({OSC_MEM + OSC_AMP}, 0)
''')
