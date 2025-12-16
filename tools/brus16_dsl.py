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

COMMOPS = {ast.Add, ast.Mult, ast.BitAnd, ast.BitOr, ast.BitXor,
           ast.Eq, ast.NotEq}

LOAD = [('LOAD', 0), ('PUSH_MR',)]

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
    if -256 <= x <= 255:
        return [('PUSH', x)]
    for shift in range(4):
        high, low = (x & 65535) >> shift, x & ((1 << shift) - 1)
        if high <= 8191:
            return [('PUSHU', high), ('SHL', shift), ('OR', low)]


def trans_load(env, name, lineno):
    match env.get(name):
        case 'var':
            return [('PUSHU', name), *LOAD]
        case 'arr' | ('func', _):
            return [('PUSHU', name)]
        case 'loc':
            return [('GET_LOCAL', name), ('PUSH_MR',)]
        case _:
            raise NameError(f"'{name}' at line {lineno}")


def trans_store(env, name, expr, lineno):
    expr = trans_expr(env, expr)
    if name not in env:
        env[name] = 'loc'
    match env[name]:
        case 'var':
            return [*expr, ('PUSHU', name), ('STORE', 0)]
        case 'loc':
            return [*expr, ('SET_LOCAL', name)]
        case _:
            raise NameError(f"'{name}' at line {lineno}")


def trans_expr(env, node, is_data=False):
    match node:
        case ast.Constant(int(val)):
            return val if is_data else push(val)
        case ast.Name(name):
            return name if is_data else trans_load(env, name, node.lineno)
        case ast.Subscript(x, y):
            x = trans_expr(env, x)
            y = trans_expr(env, y)
            return [*x, *y, ('ADD',), *LOAD]
        case ast.UnaryOp(ast.USub(), ast.Constant(int(val))):
            return -val if is_data else push(-val)
        case ast.UnaryOp(op, x):
            return [*trans_expr(env, x), UNOPS[type(op)]]
        case ast.BinOp(x, op, y) | ast.Compare(x, [op], [y]):
            x = trans_expr(env, x)
            y = trans_expr(env, y)
            if type(op) in COMMOPS and isinstance(x, ast.Constant):
                x, y = y, x
            return [*x, *y, (BINOPS[type(op)],)]
        case ast.Call(ast.Name(name), args):
            assert env.get(name) == ('func', len(args)) or name in MACROS, \
                f"'{name}' at line {node.lineno}"
            args = [trans_expr(env, x) for x in args]
            if name in MACROS:
                return MACROS[name](*args)
            return [*sum(reversed(args), []), ('CALL', name)]
        case _:
            raise SyntaxError(ast.unparse(node))


def trans_if(env, test, true, false, end_label):
    test = trans_expr(env, test)
    true = trans_block(env, true, end_label)
    false = trans_block(env, false, end_label)
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
    L1, end_label = next(new_label), next(new_label)
    body = trans_block(env, body, end_label)
    return [('LABEL', L1),
            *test,
            ('JZ', end_label),
            *body,
            ('JMP', L1),
            ('LABEL', end_label)]


def trans_stmt(env, node, end_label=None):
    match node:
        case ast.Assign([ast.Name(name) as n], expr):
            return trans_store(env, name, expr, n.lineno)
        case ast.Assign([ast.Subscript(addr, idx)], expr):
            addr = trans_expr(env, addr)
            idx = trans_expr(env, idx)
            expr = trans_expr(env, expr)
            return [*expr, *addr, *idx, ('ADD',), ('STORE', 0)]
        case ast.AugAssign(x, op, y):
            return trans_stmt(env, ast.Assign([x], ast.BinOp(x, op, y)))
        case ast.If(test, true, false):
            return trans_if(env, test, true, false, end_label)
        case ast.While(test, body, []):
            return trans_while(env, test, body)
        case ast.Return(None):
            return [('RET', None)]
        case ast.Break() if end_label is not None:
            return [('JMP', end_label)]
        case ast.Return(val):
            return [*trans_expr(env, val), ('RET', None)]
        case ast.Expr(ast.Call() as call):
            return trans_expr(env, call)
        case ast.Pass():
            return []
        case _:
            raise SyntaxError(ast.unparse(node))


def trans_block(env, block, end_label=None):
    return sum([trans_stmt(env, stmt, end_label) for stmt in block], [])


def replace_locs(locs, asm):
    for i in range(len(asm)):
        match asm[i]:
            case (('LOCALS' | 'RET') as op, None):
                asm[i] = (op, len(locs))
            case (('GET_LOCAL' | 'SET_LOCAL') as op, name):
                asm[i] = (op, locs[name])
    return asm


def trans_func(env, name, args, body):
    asm = [('LABEL', name), ('LOCALS', None)]
    for arg in args:
        env[arg.arg] = 'loc'
        asm.append(('SET_LOCAL', arg.arg))
    asm += trans_block(env, body) + [('RET', None)]
    locs = (k for k in env if env[k] == 'loc')
    return replace_locs({k: i for i, k in enumerate(locs)}, asm)


def optimize(asm):
    stack = []
    binops = set(BINOPS.values()) | {'SHRA', 'LTU'}
    for cmd in asm:
        stack.append(cmd)
        match stack:
            case [*_, ('ADD' | 'OR' | 'SHL' | 'LOCALS', 0)]:
                stack[-1:] = []
            case [*_, ('ADD', offs), (('LOAD' | 'STORE') as op, 0)]:
                stack[-2:] = [(op, offs)]
            case [*_, ('RET', _) as ret, (op, *_)] if op != 'LABEL':
                stack[-2:] = [ret]
            case [*_, ('PUSH', x), (op,)] if op in binops:
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
                asm.append(('DATA', name,
                            *(trans_expr(env, x, True) for x in arr)))
            case ast.Assign([ast.Name(name)], val):
                env[name] = 'var'
                asm.append(('DATA', name, trans_expr(env, val, True)))
            case ast.FunctionDef(name, args, body):
                env[name] = ('func', len(args.args))
                funcs.append((name, args.args, body))
            case _:
                raise SyntaxError(ast.unparse(node))
    for name, args, body in funcs:
        asm += trans_func(env.copy(), name, args, body)
    while (opt_asm := optimize(asm)) != asm:
        asm = opt_asm
    return asm
