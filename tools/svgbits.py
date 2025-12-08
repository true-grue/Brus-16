# Author: Peter Sovietov
def svg(width, height, body):
    return (f'<svg version="1.1" viewBox="0 0 {width} {height}" '
            'width="{width}" height="{height}" '
            f'xmlns="http://www.w3.org/2000/svg">{body}</svg>')


def rect(x, y, w, h, stroke='black', fill='none'):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'stroke="{stroke}" fill="{fill}" />')


def text(label, x, y):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" '
            f'dominant-baseline="middle">{label}</text>')


def make_indices(bits, lane, x, y, w):
    pos = 0
    for name, size, _ in lane:
        start = bits - pos - 1
        yield text(start, x + pos * w + w / 2, y / 2)
        if size > 1:
            end_x = x + (pos + size - 1) * w + w / 2
            yield text(start - size + 1, end_x, y / 2)
        pos += size        


def add_lane(lane, x, y, w, h):
    pos = 0
    gap = round(h * 0.1)
    for name, size, color in lane:
        fx, fw = x + pos * w, w * size
        for i in range(size):
            yield rect(fx + i * w, y, w, h, fill=color)
        if size > 1:
            yield rect(fx + gap, y + gap, fw - gap * 2, h - gap * 2,
                       stroke='none', fill=color)
        yield rect(fx, y, fw, h)
        yield text(name, fx + fw / 2, y + h / 2)
        pos += size


def svgbits(lanes, x=2, y=20, w=40, h=30):
    bits = sum(size for _, size, _ in lanes[0])
    lines = [*make_indices(bits, lanes[0], x, y, w)]
    for i, lane in enumerate(lanes):
        lines += add_lane(lane, x, y + i * h, w, h)
    return svg(x + bits * w + 2, y + len(lanes) * h + 2, '\n'.join(lines))
