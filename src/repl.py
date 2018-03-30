from io import StringIO
from read import read
from pprint import pprint
from eval import eval_sexp

def readline(prompt):
    try:
        stdin = StringIO(input(prompt))
        stdin.name = "<stdin>"
        return stdin
    except EOFError:
        return

def repl(prompt="LISP> "):
    line = readline(prompt)
    while line:
        try:
            pprint(eval_sexp(read(line)))
        except Exception as e:
            print(e)
        line = readline(prompt)
    print("\nbye.")
