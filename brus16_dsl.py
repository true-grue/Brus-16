# Author: Peter Sovietov
import ast

UNOPS = {
    ast.Invert: ('XOR', -1),
    ast.USub: ('MUL', -1)
}


BINOPS = {
    ast.Add: 'ADD',
    ast.Sub: 'SUB',
    ast.Mult: 'MUL',
    ast.LShift: 'SHL',
    ast.RShift: 'SHR',
    ast.BitAnd: 'AND',
    ast.BitOr: 'OR',
    ast.BitXor: 'XOR',
    ast.Eq: 'EQ',
    ast.NotEq: 'NEQ',
    ast.Lt: 'LT',
    ast.LtE: 'LE',
    ast.Gt: 'GT',
    ast.GtE: 'GE',
}


LOAD = [('LOAD', 0), ('PUSH_MR',)]
def GET_LOCAL(name): return [('GET_LOCAL', name), ('PUSH_MR',)]


MACROS = {
    'poke': lambda addr, val: [*val, *addr, ('STORE', 0)],
    'peek': lambda addr: [*addr, *LOAD],
    'shra': lambda x, y: [*x, *y, ('SHRA',)],
    'ltu': lambda x, y: [*x, *y, ('LTU',)],
    'set_fp': lambda addr: [*addr, ('SET_FP',)],
    'wait': lambda: [('WAIT',)]
}


def label_gen(i=0):
    while True:
        yield f'L{i}'
        i += 1


new_label = label_gen()


def push(x):
    if -4096 <= x <= 4095:
        return [('PUSH', x)]
    else:
        return [('PUSH', x >> 3),
                ('SHL', 3),
                ('OR', x & 7)]


def trans_load(env, name):
    match env.get(name):
        case 'var':
            return [('PUSH', name), *LOAD]
        case 'arr' | ('func', _):
            return [('PUSH', name)]
        case 'loc':
            return GET_LOCAL(name)
        case _:
            raise RuntimeError(name)


def trans_store(env, name, expr):
    expr = trans_expr(env, expr)
    if name not in env:
        env[name] = 'loc'
    match env[name]:
        case 'var':
            return [*expr, ('PUSH', name), ('STORE', 0)]
        case 'loc':
            return [*expr, ('SET_LOCAL', name)]
        case _:
            raise RuntimeError(name)


def is_func(env, name, arity):
    return env.get(name) == ('func', arity) or name in MACROS


def trans_expr(env, node):
    match node:
        case ast.Constant(int(val)):
            return push(val)
        case ast.Name(name):
            return trans_load(env, name)
        case ast.Subscript(x, y):
            x = trans_expr(env, x)
            y = trans_expr(env, y)
            return [*x, *y, ('ADD',), *LOAD]
        case ast.UnaryOp(ast.USub(), ast.Constant(int(val))):
            return push(-val)
        case ast.UnaryOp(op, x):
            return [*trans_expr(env, x), UNOPS[type(op)]]
        case ast.BinOp(x, op, y) | ast.Compare(x, [op], [y]):
            x = trans_expr(env, x)
            y = trans_expr(env, y)
            return [*x, *y, (BINOPS[type(op)],)]
        case ast.Call(ast.Name(name), args) if is_func(env, name, len(args)):
            args = [trans_expr(env, x) for x in args]
            if name in MACROS:
                return MACROS[name](*args)
            return [*sum(reversed(args), []), ('CALL', name)]
        case _:
            raise RuntimeError(ast.unparse(node))


def trans_if(env, test, true, false):
    test = trans_expr(env, test)
    true = trans_block(env, true)
    false = trans_block(env, false)
    L1, L2 = next(new_label), next(new_label)
    return [*test,
            ('JZ', L1),
            *true,
            ('JMP', L2),
            ('LABEL', L1),
            *false,
            ('LABEL', L2)]


def trans_while(env, test, body):
    test = trans_expr(env, test)
    body = trans_block(env, body)
    L1, L2 = next(new_label), next(new_label)
    return [('LABEL', L1),
            *test,
            ('JZ', L2),
            *body,
            ('JMP', L1),
            ('LABEL', L2)]


def trans_stmt(env, node):
    match node:
        case ast.Assign([ast.Name(name)], expr):
            return trans_store(env, name, expr)
        case ast.Assign([ast.Subscript(addr, idx)], expr):
            addr = trans_expr(env, addr)
            idx = trans_expr(env, idx)
            expr = trans_expr(env, expr)
            return [*expr, *addr, *idx, ('ADD',), ('STORE', 0)]
        case ast.AugAssign(target, op, val):
            return trans_stmt(env, ast.Assign([target],
                                             ast.BinOp(target, op, val)))
        case ast.If(test, true, false):
            return trans_if(env, test, true, false)
        case ast.While(test, body, []):
            return trans_while(env, test, body)
        case ast.Return(None):
            return [('RET', None)]
        case ast.Return(val):
            return [*trans_expr(env, val), ('RET', None)]
        case ast.Expr(ast.Call() as call):
            return trans_expr(env, call)
        case ast.Pass():
            return []
        case _:
            raise RuntimeError(ast.unparse(node))


def trans_block(env, block):
    return sum([trans_stmt(env, stmt) for stmt in block], [])


def replace_locs(locs, asm):
    for i in range(len(asm)):
        match asm[i]:
            case ('LOCALS', None):
                asm[i] = ('LOCALS', len(locs))
            case (('GET_LOCAL' | 'SET_LOCAL') as op, name):
                asm[i] = (op, locs[name])
            case ('RET', None):
                asm[i] = ('RET', len(locs))
    return asm


def trans_func(env, name, args, body):
    asm = [('LABEL', name), ('LOCALS', None)]
    for arg in args:
        env[arg.arg] = 'loc'
        asm.append(('SET_LOCAL', arg.arg))
    asm += trans_block(env, body)
    if ('RET', None) not in asm:
        asm.append(('RET', None))
    locs = (k for k in env if env[k] == 'loc')
    return replace_locs({k: i for i, k in enumerate(locs)}, asm)


def optimize(asm):
    stack = []
    binops = set(BINOPS.values()) | {'SHRA', 'LTU'}
    for cmd in asm:
        stack.append(cmd)
        match stack:
            case [*_, ('ADD' | 'OR' | 'LOCALS', 0)]:
                stack[-1:] = []
            case [*_, ('ADD', offs), (('LOAD' | 'STORE') as mop, 0)]:
                stack[-2:] = [(mop, offs)]
            case [*_, ('RET', _) as ret, ('JMP', _)]:
                stack[-2:] = [ret]
            case [*_, ('PUSH', x), (op,)] if op in binops and -256 <= x <= 255:
                stack[-2:] = [(op, x)]
    return stack


def translate(src):
    env = {}
    asm = []
    funcs = []
    for node in ast.parse(src).body:
        match node:
            case ast.Assign([ast.Name(name)], ast.List(arr)):
                env[name] = 'arr'
                asm.append(('DATA', name, *(ast.literal_eval(x) for x in arr)))
            case ast.Assign([ast.Name(name)], val):
                env[name] = 'var'
                asm.append(('DATA', name, ast.literal_eval(val)))
            case ast.FunctionDef(name, args, body):
                env[name] = ('func', len(args.args))
                funcs.append((name, args.args, body))
            case _:
                raise RuntimeError(ast.unparse(node))
    for name, args, body in funcs:
        asm += trans_func(env.copy(), name, args, body)
    while (opt_asm := optimize(asm)) != asm:
        asm = opt_asm
    return asm
