import brus16_cfg


def make_fmt(fmt):
    lines = set()
    for fields in fmt:
        pos = 0
        for name, size in reversed(fields):
            lines.add(f'#define {name}_POS {pos}')
            lines.add(f'#define {name}_SIZE {size}')
            pos += size
    return list(sorted(lines))


def make_h(mod):
    lines = []
    for name in vars(mod):
        val = getattr(mod, name)
        if isinstance(val, list):
            lines += make_fmt(val)
        elif not name.startswith('__'):
            lines.append(f'#define {name} {val}')
    return '\n'.join(lines) + '\n'


with open('brus16_cfg.h', 'w') as f:
    f.write(make_h(brus16_cfg))
