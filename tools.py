from brus16_cfg import RECT_MEM, RECT_SIZE


def to_rgb565(x):
    return ((x >> 8) & 0xf800) | ((x >> 5) & 0x07e0) | ((x >> 3) & 0x001f)


def get_rect_addr(rect, offs=0):
    return RECT_MEM + rect * RECT_SIZE + offs


def asm_to_text(asm):
    lines = []
    for cmd in asm:
        lines.append(' '.join(str(x) for x in cmd))
    return '\n'.join(lines)
