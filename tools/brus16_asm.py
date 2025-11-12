# Author: Peter Sovietov
from .brus16_cfg import FIELDS, COMMANDS


def encode(fmt, fields):
    cmd = 0
    shift = 0
    for i in reversed(range(len(fmt))):
        (name, bits), val = fmt[i], fields[i]
        mask = (1 << bits) - 1
        cmd |= (val & mask) << shift
        shift += bits
    return cmd


def pass1(ir):
    labels = {}
    new_ir, data = [], []
    for cmd in ir:
        match cmd:
            case ('LABEL', name):
                labels[name] = len(new_ir)
            case ('DATA', name, *vals):
                labels[name] = len(data)
                data += vals
            case _:
                new_ir.append(cmd)
    return labels, new_ir, data


def parse_val(field, val, args):
    name, bits = field
    match val:
        case str() if val.startswith('#'):
            return args[int(val[1:]) - 1]
        case str():
            return FIELDS[name].index(val)
        case _:
            return val


def pass2(labels, ir, data):
    code = []
    for op, *args in ir:
        args = [labels.get(x, x) for x in args]
        fmt, *vals = COMMANDS[(op, len(args))]
        vals = [parse_val(fmt[i], v, args) for i, v in enumerate(vals)]
        code.append(encode(fmt, vals))
    return labels, code, data


def assemble(ir):
    return pass2(*pass1(ir))


def save(filename, code, data):
    with open(filename, 'wb') as f:
        total = [len(code), len(data), *code, *data]
        f.write(b''.join((x & 0xffff).to_bytes(2, 'little') for x in total))
