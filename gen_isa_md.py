from brus16_cfg import FORMATS, FIELDS, COMMANDS
from svgbits import svgbits


COLORS = {
    'F': '#e3f4d7',
    'OP0': '#fff6d5',
    'OP1': '#fff6d5',
    'IMM': '#d5e5ff',
    'SIMM': '#d5e5ff'
}


PATH = 'docs'


def parse_field(name, val, size):
    color = COLORS.get(name, 'white')
    match val:
        case str() if val.startswith('#'):
            return (name, size, color)
        case str() if name in FIELDS:
            return (f'{val}={FIELDS[name].index(val)}', size, color)
        case _:
            return (val, size, color)


def gen_images():
    for i, format in enumerate(FORMATS):
        fmt = [(n, v, COLORS.get(n, 'white')) for n, v in format]
        with open(f'{PATH}/fmt_{i}.svg', 'w') as f:
            f.write(svgbits([fmt], 16))
        lanes = []
        for cmd in COMMANDS.values():
            fmt, *vals = cmd
            if format == fmt:
                lanes.append([parse_field(n, v, size)
                              for (n, size), v in zip(fmt, vals)])
        with open(f'{PATH}/cmd_{i}.svg', 'w') as f:
            f.write(svgbits(lanes, 16))


def gen_md():
    lines = ['## Brus-16 instruction set\n']
    gen_images()
    for i, format in enumerate(FORMATS):
        lines.append(f'### Format {i}\n')
        lines.append(f'Encoding\n\n![](fmt_{i}.svg)\n')
        lines.append(f'Instructions\n\n![](cmd_{i}.svg)\n')
    return '\n'.join(lines)


with open(f'{PATH}/isa.md', 'w') as f:
    f.write(gen_md())
