from brus16 import *

def debug(text):
    code = []
    for c in text:
        code.append(f'poke(-1, {ord(c)})')
    return ';'.join(code)

save_game('debug.bin', f'''
def main():   
    x = 0
    while 1:
        {debug('x = 0x')}
        debug_val(x)
        {debug('\n')}
        wait()
        x += 1

def debug_val(x):
    d = (x >> 12) & 15
    poke(-1, d + 48 + (d > 9) * 7)
    d = (x >> 8) & 15
    poke(-1, d + 48 + (d > 9) * 7)
    d = (x >> 4) & 15
    poke(-1, d + 48 + (d > 9) * 7)
    d = x & 15
    poke(-1, d + 48 + (d > 9) * 7)
''')
