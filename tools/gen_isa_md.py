import sys
from brus16_cfg import FORMATS, FIELDS, COMMANDS
from svgbits import svgbits


BITS = 16

COLORS = {
    'F': '#e3f4d7',
    'OP0': '#fff6d5',
    'OP1': '#fff6d5',
    'IMM': '#d5e5ff',
    'SIMM': '#d5e5ff'
}


def gen_format(format):
    fmt = [(n, v, COLORS.get(n, 'white')) for n, v in format]
    return svgbits([fmt], BITS)


def parse_field(name, val, size):
    color = COLORS.get(name, 'white')
    match val:
        case str() if val.startswith('#'):
            return (name, size, color)
        case str() if name in FIELDS:
            return (f'{FIELDS[name].index(val)}', size, color)
        case _:
            return (val, size, color)


def get_label(op, arity, fmt, vals):
    args = []
    for i in range(arity):
        arg = f'#{i + 1}'
        if arg in vals:
            field, _ = fmt[vals.index(arg)]
            args.append(field.lower())
    return ' '.join([op, ', '.join(args)])


def gen_command(op, arity, fmt, vals):
    cmd = [parse_field(n, v, size) for (n, size), v in zip(fmt, vals)]
    return get_label(op, arity, fmt, vals), svgbits([cmd], BITS)


def gen_md():
    lines = ['## Brus-16 instruction set']
    for i, format in enumerate(FORMATS):
        lines.append(f'### Format {i}')
        filename = f'images/fmt_{i}.svg'
        with open(f'{PATH}/{filename}', 'w') as f:
            f.write(gen_format(format))
        lines.append('#### Encoding')
        lines.append(f'![]({filename})')
        lines.append(f'#### Instructions')
        for j, ((op, arity), cmd) in enumerate(COMMANDS.items()):
            fmt, *vals = cmd
            if format == fmt:
                filename = f'images/cmd_{j}.svg'
                label, svg = gen_command(op, arity, fmt, vals)
                lines.append(label)
                with open(f'{PATH}/{filename}', 'w') as f:
                    f.write(svg)
                lines.append(f'![]({filename})')
    return '\n\n'.join(lines)


PATH = sys.argv[1]
with open(f'{PATH}/isa.md', 'w') as f:
    f.write(gen_md())
