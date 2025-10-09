import brus16_isa as ISA


def IMM13(arg): return arg
def SIMM9(arg): return arg


COMMANDS = {
    ('JMP', 1): (ISA.F1, 1, ISA.JMP, IMM13),
    ('JZ', 1): (ISA.F1, 1, ISA.JZ, IMM13),
    ('CALL', 1): (ISA.F1, 1, ISA.CALL, IMM13),
    ('PUSH_ADDR', 1): (ISA.F1, 1, ISA.PUSH_ADDR, IMM13),
    ('ADD', 0): (ISA.F2, 0, ISA.ADD, 0, 0),
    ('SUB', 0): (ISA.F2, 0, ISA.SUB, 0, 0),
    ('MUL', 0): (ISA.F2, 0, ISA.MUL, 0, 0),
    ('AND', 0): (ISA.F2, 0, ISA.AND, 0, 0),
    ('OR', 0): (ISA.F2, 0, ISA.OR, 0, 0),
    ('XOR', 0): (ISA.F2, 0, ISA.XOR, 0, 0),
    ('SHL', 0): (ISA.F2, 0, ISA.SHL, 0, 0),
    ('SHR', 0): (ISA.F2, 0, ISA.SHR, 0, 0),
    ('SHRA', 0): (ISA.F2, 0, ISA.SHRA, 0, 0),
    ('EQ', 0): (ISA.F2, 0, ISA.EQ, 0, 0),
    ('NEQ', 0): (ISA.F2, 0, ISA.NEQ, 0, 0),
    ('LT', 0): (ISA.F2, 0, ISA.LT, 0, 0),
    ('LE', 0): (ISA.F2, 0, ISA.LE, 0, 0),
    ('GT', 0): (ISA.F2, 0, ISA.GT, 0, 0),
    ('GE', 0): (ISA.F2, 0, ISA.GE, 0, 0),
    ('LTU', 0): (ISA.F2, 0, ISA.LTU, 0, 0),
    ('ADD', 1): (ISA.F2, 0, ISA.ADD, 1, SIMM9),
    ('SUB', 1): (ISA.F2, 0, ISA.SUB, 1, SIMM9),
    ('MUL', 1): (ISA.F2, 0, ISA.MUL, 1, SIMM9),
    ('AND', 1): (ISA.F2, 0, ISA.AND, 1, SIMM9),
    ('OR', 1): (ISA.F2, 0, ISA.OR, 1, SIMM9),
    ('XOR', 1): (ISA.F2, 0, ISA.XOR, 1, SIMM9),
    ('SHL', 1): (ISA.F2, 0, ISA.SHL, 1, SIMM9),
    ('SHR', 1): (ISA.F2, 0, ISA.SHR, 1, SIMM9),
    ('SHRA', 1): (ISA.F2, 0, ISA.SHRA, 1, SIMM9),
    ('EQ', 1): (ISA.F2, 0, ISA.EQ, 1, SIMM9),
    ('NEQ', 1): (ISA.F2, 0, ISA.NEQ, 1, SIMM9),
    ('LT', 1): (ISA.F2, 0, ISA.LT, 1, SIMM9),
    ('LE', 1): (ISA.F2, 0, ISA.LE, 1, SIMM9),
    ('GT', 1): (ISA.F2, 0, ISA.GT, 1, SIMM9),
    ('GE', 1): (ISA.F2, 0, ISA.GE, 1, SIMM9),
    ('LTU', 1): (ISA.F2, 0, ISA.LTU, 1, SIMM9),
    ('LOAD', 0): (ISA.F2, 0, ISA.LOAD, 0, 0),
    ('STORE', 0): (ISA.F2, 0, ISA.STORE, 0, 0),
    ('GET_LOCAL', 1): (ISA.F2, 0, ISA.LOAD, 1, SIMM9),
    ('SET_LOCAL', 1): (ISA.F2, 0, ISA.STORE, 1, SIMM9),
    ('LOCALS', 1): (ISA.F2, 0, ISA.LOCALS, 1, SIMM9),
    ('SET_FP', 0): (ISA.F2, 0, ISA.SET_FP, 0, 0),
    ('ICALL', 0): (ISA.F2, 0, ISA.ICALL, 0, 0),
    ('RET', 1): (ISA.F2, 0, ISA.RET, 1, SIMM9),
    ('PUSH_INT', 1): (ISA.F2, 0, ISA.PUSH_INT, 1, SIMM9),
    ('PUSH_MR', 0): (ISA.F2, 0, ISA.PUSH_MR, 0, 0),
    ('POP', 0): (ISA.F2, 0, ISA.POP, 0, 0),
    ('WAIT', 0): (ISA.F2, 0, ISA.WAIT, 0, 0)
}


def encode(fmt, fields):
    cmd = 0
    shift = 0
    for i in reversed(range(len(fmt))):
        name, bits = fmt[i]
        val = fields[i]
        mask = (1 << bits) - 1
        cmd |= (val & mask) << shift
        shift += bits
    return cmd


def pass1(asm):
    labels = {}
    asm_code, data = [], []
    for cmd in asm:
        match cmd:
            case ('LABEL', name):
                labels[name] = len(asm_code)
            case ('DATA', name, *vals):
                labels[name] = len(data)
                data += vals
            case _:
                asm_code.append(cmd)
    return labels, asm_code, data


def pass2(labels, asm_code, data):
    code = []
    for op, *args in asm_code:
        args = [labels.get(x, x) for x in args]
        fmt, *fields = COMMANDS[(op, len(args))]
        fields = [f(*args) if callable(f) else f for f in fields]
        code.append(encode(fmt, fields))
    return labels, code, data


def assemble(asm):
    return pass2(*pass1(asm))


def to_le(x):
    return int.to_bytes(x & 0xffff, 2, 'little')


def save(filename, code, data):
    with open(filename, 'wb') as f:
        header = to_le(len(code)) + to_le(len(data))
        code = b''.join(to_le(x) for x in code)
        data = b''.join(to_le(x) for x in data)
        f.write(header + code + data)
