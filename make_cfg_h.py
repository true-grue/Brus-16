import brus16_cfg


def make_fmt(fmt):
    lines = []
    for i, fields in enumerate(fmt):
        pos = 0
        for name, size in reversed(fields):
            lines.append(f'#define F{i + 1}_{name}_POS {pos}')
            lines.append(f'#define F{i + 1}_{name}_SIZE {size}')
            pos += size
    return lines


def make_h(mod):
    lines = []
    for name in vars(mod):
        val = getattr(mod, name)
        if name == 'FORMAT':
            lines += make_fmt(val)
        elif not name.startswith('__'):
            lines.append(f'#define {name} {val}')
    return '\n'.join(lines) + '\n'


with open('brus16_cfg.h', 'w') as f:
    f.write(make_h(brus16_cfg))
