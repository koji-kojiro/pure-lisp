import sys
import pkgutil
import argparse
from read import read
from eval import eval_sexp
from repl import repl, Repl

def list_extensions():
    import extensions
    modules = [info.name for info in  pkgutil.iter_modules(extensions.__path__)]
    return [module for module in modules if not module.startswith("_")]

def enable_extensions(*args):
    extensions = list(args) if args else list_extensions()
    __import__("extensions", fromlist=extensions)
    Repl.intro += f"[Enabled extensions: {extensions}]\n"

def run_source(fname):
    with open(fname, "r") as f:
        sexp = read(f, eof_error_p=False)
        while sexp:
            eval_sexp(sexp)
            sexp = read(f, eof_error_p=False)

parser = argparse.ArgumentParser()
parser.add_argument("file", help="lisp source code.", nargs="?")
parser.add_argument("-e", "--ext", help="enable extensions.", nargs="*", metavar="ext", choices=list_extensions())
parser.add_argument("--list-ext", help="list avilable extensions.", action="store_true")
args = parser.parse_args()

if args.list_ext:
    sys.exit("\n".join(list_extensions()))

if args.ext is not None:
    enable_extensions(*args.ext)

if args.file:
    run_source(args.file)
else:
    repl()
