# Author: Peter Sovietov
def make_svg(width, height, body):
    return (f'<svg version="1.1" width="{width}" height="{height}" '
            f'xmlns="http://www.w3.org/2000/svg">{body}</svg>')


def rect(x, y, w, h, stroke='black', fill='none'):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'stroke="{stroke}" fill="{fill}" />')


def text(x, y, txt, fill='black', anchor='middle', baseline='middle'):
    return (f'<text x="{x}" y="{y}" fill="{fill}" text-anchor="{anchor}" '
            f'dominant-baseline="{baseline}">{txt}</text>')


def add_bits(bits, x, y, w):
    return [text(x + i * w + w / 2, y / 2, str(bits - i - 1))
            for i in range(bits)]


def add_lane(lane, x, y, w, h):
    lines = []
    pos = 0
    gap = round(h * 0.1)
    for name, size, color in lane:
        fx, fw = x + pos * w, w * size
        lines += [rect(fx + i * w, y, w, h, fill=color) for i in range(size)]
        if size > 1:
            lines.append(rect(fx + gap, y + gap, fw - gap * 2,
                              h - gap * 2, stroke='none', fill=color))
        lines.append(rect(fx, y, fw, h))
        lines.append(text(fx + fw / 2, y + h / 2, name))
        pos += size
    return lines


def svgbits(lanes, bits, x=2, y=20, w=40, h=30):
    svg_w, svg_h = x + bits * w + 2, y + len(lanes) * h + 2
    lines = [rect(0, 0, svg_w, svg_h, stroke='white', fill='white')]
    lines += add_bits(bits, x, y, w)
    for i, lane in enumerate(lanes):
        lines += add_lane(lane, x, y + i * h, w, h)
    return make_svg(svg_w, svg_h, '\n'.join(lines))
