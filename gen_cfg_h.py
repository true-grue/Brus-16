import brus16_cfg
from brus16_cfg import FORMATS, FIELDS


def gen_consts(mod):
    lines = []
    for n, v in vars(mod).items():
        if not n.startswith('_') and isinstance(v, int):
            lines.append(f'#define {n} {v}')
    return lines


def gen_formats(formats):
    lines = set()
    for fmt in formats:
        pos = 0
        for name, bits in reversed(fmt):
            lines.add(f'#define {name}_POS {pos}')
            lines.add(f'#define {name}_SIZE {bits}')
            pos += bits
    return sorted(lines)


def gen_fields(fields):
    lines = []
    for f in fields:
        for i, n in enumerate(fields[f]):
            lines.append(f'#define {f}_{n} {i}')
    return lines


def gen_cfg_h():
    lines = gen_consts(brus16_cfg)
    lines += gen_formats(FORMATS)
    lines += gen_fields(FIELDS)
    return '\n'.join(lines) + '\n'


with open('brus16_cfg.h', 'w') as f:
    f.write(gen_cfg_h())
