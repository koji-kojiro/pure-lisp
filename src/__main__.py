import sys
from repl import repl
from eval import eval_sexp
from read import read, peek_char, delimiters

if len(sys.argv) == 1:
    sexp = read(eof_error_p=False)
    while(sexp):
        eval_sexp(sexp)
        sexp = read(eof_error_p=False)
elif "--repl" in sys.argv:
    repl()
else:
    sys.exit("usage: {} [--repl]".format(sys.argv[0]))
