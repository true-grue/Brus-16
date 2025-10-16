import brus16_cfg as ISA


def IMM13(arg): return arg
def SIMM9(arg): return arg


F1 = ISA.FORMAT[0]
F2 = ISA.FORMAT[1]
COMMANDS = {
    ('JMP', 1): (F1, 1, ISA.OP_JMP, IMM13),
    ('JZ', 1): (F1, 1, ISA.OP_JZ, IMM13),
    ('CALL', 1): (F1, 1, ISA.OP_CALL, IMM13),
    ('PUSH_ADDR', 1): (F1, 1, ISA.OP_PUSH_ADDR, IMM13),
    ('ADD', 0): (F2, 0, ISA.OP_ADD, 0, 0),
    ('SUB', 0): (F2, 0, ISA.OP_SUB, 0, 0),
    ('MUL', 0): (F2, 0, ISA.OP_MUL, 0, 0),
    ('AND', 0): (F2, 0, ISA.OP_AND, 0, 0),
    ('OR', 0): (F2, 0, ISA.OP_OR, 0, 0),
    ('XOR', 0): (F2, 0, ISA.OP_XOR, 0, 0),
    ('SHL', 0): (F2, 0, ISA.OP_SHL, 0, 0),
    ('SHR', 0): (F2, 0, ISA.OP_SHR, 0, 0),
    ('SHRA', 0): (F2, 0, ISA.OP_SHRA, 0, 0),
    ('EQ', 0): (F2, 0, ISA.OP_EQ, 0, 0),
    ('NEQ', 0): (F2, 0, ISA.OP_NEQ, 0, 0),
    ('LT', 0): (F2, 0, ISA.OP_LT, 0, 0),
    ('LE', 0): (F2, 0, ISA.OP_LE, 0, 0),
    ('GT', 0): (F2, 0, ISA.OP_GT, 0, 0),
    ('GE', 0): (F2, 0, ISA.OP_GE, 0, 0),
    ('LTU', 0): (F2, 0, ISA.OP_LTU, 0, 0),
    ('ADD', 1): (F2, 0, ISA.OP_ADD, 1, SIMM9),
    ('SUB', 1): (F2, 0, ISA.OP_SUB, 1, SIMM9),
    ('MUL', 1): (F2, 0, ISA.OP_MUL, 1, SIMM9),
    ('AND', 1): (F2, 0, ISA.OP_AND, 1, SIMM9),
    ('OR', 1): (F2, 0, ISA.OP_OR, 1, SIMM9),
    ('XOR', 1): (F2, 0, ISA.OP_XOR, 1, SIMM9),
    ('SHL', 1): (F2, 0, ISA.OP_SHL, 1, SIMM9),
    ('SHR', 1): (F2, 0, ISA.OP_SHR, 1, SIMM9),
    ('SHRA', 1): (F2, 0, ISA.OP_SHRA, 1, SIMM9),
    ('EQ', 1): (F2, 0, ISA.OP_EQ, 1, SIMM9),
    ('NEQ', 1): (F2, 0, ISA.OP_NEQ, 1, SIMM9),
    ('LT', 1): (F2, 0, ISA.OP_LT, 1, SIMM9),
    ('LE', 1): (F2, 0, ISA.OP_LE, 1, SIMM9),
    ('GT', 1): (F2, 0, ISA.OP_GT, 1, SIMM9),
    ('GE', 1): (F2, 0, ISA.OP_GE, 1, SIMM9),
    ('LTU', 1): (F2, 0, ISA.OP_LTU, 1, SIMM9),
    ('LOAD', 0): (F2, 0, ISA.OP_LOAD, 0, 0),
    ('STORE', 0): (F2, 0, ISA.OP_STORE, 0, 0),
    ('GET_LOCAL', 1): (F2, 0, ISA.OP_LOAD, 1, SIMM9),
    ('SET_LOCAL', 1): (F2, 0, ISA.OP_STORE, 1, SIMM9),
    ('LOCALS', 1): (F2, 0, ISA.OP_LOCALS, 1, SIMM9),
    ('SET_FP', 0): (F2, 0, ISA.OP_SET_FP, 0, 0),
    ('RET', 1): (F2, 0, ISA.OP_RET, 1, SIMM9),
    ('PUSH_INT', 1): (F2, 0, ISA.OP_PUSH_INT, 1, SIMM9),
    ('PUSH_MR', 0): (F2, 0, ISA.OP_PUSH_MR, 0, 0),
    ('WAIT', 0): (F2, 0, ISA.OP_WAIT, 0, 0)
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
