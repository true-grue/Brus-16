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
KEY_C = 6
KEY_D = 7
KEY_UP2 = 8
KEY_DOWN2 = 9
KEY_LEFT2 = 10
KEY_RIGHT2 = 11
KEY_A2 = 12
KEY_B2 = 13
KEY_C2 = 14
KEY_D2 = 15

VOICE_NUM = 16
VOICE_SIZE = 4
VOICE_MEM = KEY_MEM - VOICE_NUM * VOICE_SIZE
VOICE_ABS = 0
VOICE_AMP = 1
VOICE_DECAY = 2
VOICE_STEP = 3

SYSTEM_MEM = VOICE_MEM

FORMATS = [
    [('F', 1), ('OP0', 5), ('I', 1), ('SIMM', 9)],
    [('F', 1), ('OP1', 2), ('IMM', 13)]
]

FIELDS = {
    'OP0': ['ADD', 'SUB', 'MUL', 'AND', 'OR', 'XOR', 'SHL', 'SHR', 'SHRA',
            'EQ', 'NEQ', 'LT', 'LE', 'GT', 'GE', 'LTU', 'LOAD', 'STORE',
            'LOCALS', 'SET_FP', 'RET', 'PUSH', 'PUSH_MR', 'WAIT'],
    'OP1': ['JMP', 'JZ', 'CALL', 'PUSHU']
}

F0 = FORMATS[0]
F1 = FORMATS[1]

COMMANDS = {
    ('JMP', 1): (F1, 1, 'JMP', '#1'),
    ('JZ', 1): (F1, 1, 'JZ', '#1'),
    ('CALL', 1): (F1, 1, 'CALL', '#1'),
    ('PUSHU', 1): (F1, 1, 'PUSHU', '#1'),
    ('ADD', 0): (F0, 0, 'ADD', 0, 0),
    ('SUB', 0): (F0, 0, 'SUB', 0, 0),
    ('MUL', 0): (F0, 0, 'MUL', 0, 0),
    ('AND', 0): (F0, 0, 'AND', 0, 0),
    ('OR', 0): (F0, 0, 'OR', 0, 0),
    ('XOR', 0): (F0, 0, 'XOR', 0, 0),
    ('SHL', 0): (F0, 0, 'SHL', 0, 0),
    ('SHR', 0): (F0, 0, 'SHR', 0, 0),
    ('SHRA', 0): (F0, 0, 'SHRA', 0, 0),
    ('EQ', 0): (F0, 0, 'EQ', 0, 0),
    ('NEQ', 0): (F0, 0, 'NEQ', 0, 0),
    ('LT', 0): (F0, 0, 'LT', 0, 0),
    ('LE', 0): (F0, 0, 'LE', 0, 0),
    ('GT', 0): (F0, 0, 'GT', 0, 0),
    ('GE', 0): (F0, 0, 'GE', 0, 0),
    ('LTU', 0): (F0, 0, 'LTU', 0, 0),
    ('ADD', 1): (F0, 0, 'ADD', 1, '#1'),
    ('SUB', 1): (F0, 0, 'SUB', 1, '#1'),
    ('MUL', 1): (F0, 0, 'MUL', 1, '#1'),
    ('AND', 1): (F0, 0, 'AND', 1, '#1'),
    ('OR', 1): (F0, 0, 'OR', 1, '#1'),
    ('XOR', 1): (F0, 0, 'XOR', 1, '#1'),
    ('SHL', 1): (F0, 0, 'SHL', 1, '#1'),
    ('SHR', 1): (F0, 0, 'SHR', 1, '#1'),
    ('SHRA', 1): (F0, 0, 'SHRA', 1, '#1'),
    ('EQ', 1): (F0, 0, 'EQ', 1, '#1'),
    ('NEQ', 1): (F0, 0, 'NEQ', 1, '#1'),
    ('LT', 1): (F0, 0, 'LT', 1, '#1'),
    ('LE', 1): (F0, 0, 'LE', 1, '#1'),
    ('GT', 1): (F0, 0, 'GT', 1, '#1'),
    ('GE', 1): (F0, 0, 'GE', 1, '#1'),
    ('LTU', 1): (F0, 0, 'LTU', 1, '#1'),
    ('LOAD', 1): (F0, 0, 'LOAD', 0, '#1'),
    ('STORE', 1): (F0, 0, 'STORE', 0, '#1'),
    ('GET_LOCAL', 1): (F0, 0, 'LOAD', 1, '#1'),
    ('SET_LOCAL', 1): (F0, 0, 'STORE', 1, '#1'),
    ('LOCALS', 1): (F0, 0, 'LOCALS', 1, '#1'),
    ('SET_FP', 0): (F0, 0, 'SET_FP', 0, 0),
    ('RET', 1): (F0, 0, 'RET', 1, '#1'),
    ('PUSH', 1): (F0, 0, 'PUSH', 1, '#1'),
    ('PUSH_MR', 0): (F0, 0, 'PUSH_MR', 0, 0),
    ('WAIT', 0): (F0, 0, 'WAIT', 0, 0)
}
