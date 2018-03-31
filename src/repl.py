import sys
from cmd import Cmd
from io import StringIO
from sys import version, platform
from pprint import pprint
from eval import eval_sexp, env
from read import read, validchars
from builtin import functions, special_forms, constants

_help = """\
Functions:
    atom: (atom `symbol`)
        return `t` if the given symbol's value is atomic.   
    eq: (eq `symbol1` `symbol2`)
        return `t` if the given two symbols' values are equal.
    car: (car `pair`)
        return the first value of the given pair.
    cdr: (cdr `pair`)
        return the second value of the given pair.
   cons: (cons `symbol1` `symobl2`)
        create a new pair.

Special forms:
    quote: (quote `symbol`) or '`symbol`
        return the given symbol as a value.
    lambda: (lambda `argument-list` `expression`)
        create a function.
    define: (define `symbol` `value`)
        bind a value to a symbol.
    if: (if `test` `trueexpr` `falseexpr`)
        return `trueexpr` if `test` is true, else `falseexpr`.
"""


class Repl(Cmd):
    intro=f"LISP on Python {version} on {platform}\nType :help, :copyright for more information.\n"
    prompt = "> "
    
    def do_help(self, *args):
        pass

    def default(self, line):
        if line is not "EOF":
            stdin = StringIO(line)
            stdin.name = "<stdin>"
            try:
                pprint(eval_sexp(read(stdin)))
            except Exception as e:
                print(e)
        else:
            return True
    
    def completenames(self, text, line, begidx, endidx):
        names = dict(**functions, **special_forms, **constants, **env).keys()
        return [name for name in names if name.startswith(line[begidx:endidx])]
    
    def completedefault(self, *args):
        return self.completenames(*args)

def repl():
    constants.update({":help": _help, ":copyright": "Copyright (C) 2018 TANI Kojiro<kojiro0531@gmail.com>"})
    try:
        Repl().cmdloop()
    except KeyboardInterrupt:
        print("\ninterrupted.", end="")
    finally:
        print("\nbye.")
