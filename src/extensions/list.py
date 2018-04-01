from functools import reduce
from itertools import permutations
from . import _import
import repl
import builtin

_help = """\

[Extension:list]
Functions:
    list: (list `symbol` ...)
        make a list with the given symbols as its elements.
    length: (length 'list`)
        return the length of the given list.
"""

repl._help += _help

functions = {
    "list": lambda *args: list(args),
    "car": lambda lst: lst[0],
    "cdr": lambda lst: lst[1:],
    "length": len,
}


def xxx_to_function(xxx):
    funcs = [functions[f"c{x}r"] for x in xxx]
    return reduce(lambda f, g: lambda x: f(g(x)), funcs, lambda x: x)

cxxxr = {
    f"c{xxx}r": xxx_to_function(xxx) for n in range(2, 5) for xxx in set(map("".join, permutations("ad" * n, n)))
}

builtin.functions.update(functions, **cxxxr)
