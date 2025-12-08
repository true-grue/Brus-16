import sys
from brus16_cfg import FORMATS, FIELDS, COMMANDS
from svgbits import svgbits


COLORS = {
    'F': '#e3f4d7',
    'I': '#f4d7d7',
    'OP0': '#fff6d5',
    'OP1': '#fff6d5',
    'IMM': '#d5e5ff',
    'SIMM': '#d5e5ff'
}


def gen_format(format):
    return [(n, v, COLORS.get(n, 'white')) for n, v in format]


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
    return ' '.join([op, *args])


def gen_command(op, arity, fmt, vals):
    cmd = [parse_field(n, v, size) for (n, size), v in zip(fmt, vals)]
    return get_label(op, arity, fmt, vals), cmd


def gen_md():
    lines = ['## Brus-16 instruction set']
    for i, format in enumerate(FORMATS):
        lines.append(f'### Format {i}')
        lines.append('#### Encoding')
        lines.append(svgbits([gen_format(format)]))
        lines.append(f'#### Instructions')
        for j, ((op, arity), cmd) in enumerate(COMMANDS.items()):
            fmt, *vals = cmd
            if format == fmt:
                label, cmd = gen_command(op, arity, fmt, vals)
                lines.append(f'{svgbits([cmd])}')
                lines.append(label)
    return '\n\n'.join(lines) + '\n'


PATH = sys.argv[1]
with open(f'{PATH}/isa.md', 'w') as f:
    f.write(gen_md())
