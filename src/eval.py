import pprint
from builtin import symbol_value, Kind

env = {}

def eval_sexp(sexp, env=env):
    eval_in_env = lambda _: eval_sexp(_, env)
    if type(sexp) is list:
        if not sexp:
            return sexp
        car = sexp[0]
        func, kind = symbol_value(car if type(car) is str else eval_in_env(car), env)
        if kind is Kind.Special:
            return func(*sexp[1:], env, eval_sexp)
        elif kind is Kind.Unbounded:
            raise ValueError("The function {} is unbounded.".format(car))
        else:
            if not callable(func):
                func = eval_in_env(func)   
            return func(*list(map(eval_in_env, sexp[1:])))
    else:
        value, kind = symbol_value(sexp, env)
        if kind is Kind.Unbounded:
            raise ValueError("The symbol {} is unbounded.".format(sexp))
        return value

