from . import _import
import read
import repl
import builtin

_help ="""\

[Extension:string]
Functions:
    readline: (readline)
        read one line from standard input into a string.

Special forms:
    string: (string `symbol`)
        convert the given symbol to a string.
"""

repl._help += _help

class LispString(str):
    def __eq__(self, other):
        if isinstance(other, LispString):
           return str(self) == str(other)
        else:
           return False

    def upper(self):
        return LispString(str.upper(self))

    def lower(self):
        return LispString(str.lower(self))
   
    def capitalize(self):
        return LispString(str.capitalize(self))

special_forms = {
    "string": lambda string, env, hook: LispString(string),
}

functions = {
    "readline": lambda : LispString(input()),
    "string-upcase": LispString.upper,
    "string-downcase": LispString.lower,
    "string-capitalize": LispString.capitalize,
}

builtin.special_forms.update(special_forms)
builtin.functions.update(functions)

def read_string(stream):
    string = ""
    char = read.read_char(stream)
    while char is not "\"":
        string += char
        char = read.read_char(stream)
    return ["string", string]

read.readtable.update({"\"": read_string})
