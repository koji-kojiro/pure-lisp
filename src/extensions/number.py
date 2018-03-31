from . import _import
import read
import builtin

special_forms = {
    "number": lambda number, env, hook: float(number),
}

functions = {
    "+": float.__add__,
    "-": float.__sub__,
    "*": float.__mul__,
    "/": float.__truediv__,
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
