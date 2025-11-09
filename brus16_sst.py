import os
import json
import brus16_cfg


def get_names(mod):
    return [(k, v) for k, v in vars(mod).items() if not k.startswith('_')]


def make_c_fields(fmt):
    lines = set()
    for fields in fmt:
        pos = 0
        for name, size in reversed(fields):
            lines.add(f'#define {name}_POS {pos}')
            lines.add(f'#define {name}_SIZE {size}')
            pos += size
    return list(sorted(lines))


def make_c_header(mod):
    lines = []
    for name, val in get_names(mod):
        if isinstance(val, list):
            lines += make_c_fields(val)
        else:
            lines.append(f'#define {name} {val}')
    return '\n'.join(lines) + '\n'


def get_isa(mod):
    formats = []
    ops = {}
    for name, val in get_names(mod):
        if isinstance(val, list):
            formats += val
        elif name.startswith('OP'):
            field, op = name.split('_', 1)
            ops.setdefault(field, []).append(op)
    return formats, ops


def wavedrom_to_svg(cmd, outfile):
    with open('temp.json', 'w') as f:
        f.write(json.dumps(cmd))
    os.system(f'npx wavedrom-cli -i temp.json > {outfile}')
    os.remove('temp.json')


MD = '''
### Format {i}

<div>
<img src="{outfile}">
</div>
'''.lstrip()


def isa_to_md(mod):
    md = []
    formats, ops = get_isa(mod)
    for i, fmt in enumerate(formats, 1):
        cmd = []
        for name, bits in reversed(fmt):
            field = {'name': name, 'bits': bits}
            if name in ops:
                field['attr'] = [f'{op} = {j}'
                                 for j, op in enumerate(ops[name])]
                field['type'] = 1
            cmd.append(field)
        outfile = f'docs/format_{i}.svg'
        wavedrom_to_svg({"reg": cmd}, outfile)
        md.append(MD.format(i=i, outfile=outfile))
    return '\n'.join(md)


if __name__ == '__main__':
    with open('brus16_cfg.h', 'w') as f:
        f.write(make_c_header(brus16_cfg))
    with open('docs/isa.md', 'w') as f:
        f.write(isa_to_md(brus16_cfg))
