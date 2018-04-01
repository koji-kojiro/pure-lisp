from . import _import
import read
import repl
import builtin

_help ="""\

[Extension:number]
Functions:
    +, -, *, /: (+ `number` ...)
        perform general numerical operations over the given numbers.

Special forms:
    number: (number `symbol`)
        convert the given symbol to a number.
"""

repl._help += _help

special_forms = {
    "number": lambda number, env, hook: float(number),
}

from functools import reduce

def make_operator(op):
    return lambda *args: reduce(op, args)

functions = {
    "+": make_operator(float.__add__),
    "-": make_operator(float.__sub__),
    "*": make_operator(float.__mul__),
    "/": make_operator(float.__truediv__),
}

builtin.special_forms.update(special_forms)
builtin.functions.update(functions)

from string import digits

def value_error(stream):
    "Wrong number literal in file {name} at file position {position} (row: {row}, col: {col})"
    raise ValueError(value_error.__doc__.format(**read.describe_stream(stream)))

def read_number(stream):
    num_string = ""
    stream.seek(stream.tell() -1)
    char = read.peek_char(stream)
    while char in digits + ".":
        num_string += read.read_char(stream)
        char = read.peek_char(stream)
    return ["number", num_string]

read.readtable.update({key: read_number for key in digits})
