from brus16_cfg import RECT_MEM, RECT_SIZE


def to_rgb565(val):
    r = (val >> 16) & 0xff
    g = (val >> 8) & 0xff
    b = val & 0xff
    r5 = (r >> 3) & 0x1f
    g6 = (g >> 2) & 0x3f
    b5 = (b >> 3) & 0x1f
    return (r5 << 11) | (g6 << 5) | b5


def get_rect_addr(rect, offs=0):
    return RECT_MEM + rect * RECT_SIZE + offs


def get_asm_text(asm):
    lines = []
    for cmd in asm:
        lines.append(' '.join(str(x) for x in cmd))
    return '\n'.join(lines)
