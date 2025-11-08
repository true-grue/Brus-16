CODE_SIZE = 8192
DATA_SIZE = 8192
STACK_SIZE = 32
RSTACK_SIZE = 16

SCREEN_W = 640
SCREEN_H = 480

RECT_NUM = 64
RECT_SIZE = 6
RECT_MEM = DATA_SIZE - RECT_NUM * RECT_SIZE
RECT_ABS = 0
RECT_X = 1
RECT_Y = 2
RECT_W = 3
RECT_H = 4
RECT_COLOR = 5

KEY_NUM = 16
KEY_MEM = RECT_MEM - KEY_NUM
KEY_UP = 0
KEY_DOWN = 1
KEY_LEFT = 2
KEY_RIGHT = 3
KEY_A = 4
KEY_B = 5
KEY_UP2 = 6
KEY_DOWN2 = 7
KEY_LEFT2 = 8
KEY_RIGHT2 = 9
KEY_A2 = 10
KEY_B2 = 11

FORMATS = [
    [('F', 1), ('OP1', 2), ('IMM', 13)],
    [('F', 1), ('OP2', 5), ('I', 1), ('SIMM', 9)]
]

OP_JMP = 0
OP_JZ = 1
OP_CALL = 2
OP_PUSHU = 3

OP_ADD = 0
OP_SUB = 1
OP_MUL = 2
OP_AND = 3
OP_OR = 4
OP_XOR = 5
OP_SHL = 6
OP_SHR = 7
OP_SHRA = 8
OP_EQ = 9
OP_NEQ = 10
OP_LT = 11
OP_LE = 12
OP_GT = 13
OP_GE = 14
OP_LTU = 15
OP_LOAD = 16
OP_STORE = 17
OP_LOCALS = 18
OP_SET_FP = 19
OP_RET = 20
OP_PUSH = 21
OP_PUSH_MR = 22
OP_WAIT = 23


def _make_fields(fmt):
    lines = set()
    for fields in fmt:
        pos = 0
        for name, size in reversed(fields):
            lines.add(f'#define {name}_POS {pos}')
            lines.add(f'#define {name}_SIZE {size}')
            pos += size
    return list(sorted(lines))


def _make_header():
    lines = []
    for name, val in globals().items():
        if isinstance(val, list):
            lines += _make_fields(val)
        elif not name.startswith('_'):
            lines.append(f'#define {name} {val}')
    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    with open('brus16_cfg.h', 'w') as _f:
        _f.write(_make_header())
