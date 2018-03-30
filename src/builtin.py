from enum import Enum

special_forms = {
    "quote": lambda symbol, *args: symbol,
    "lambda": lambda arglist, body, env, hook: lambda *args: hook(body, dict(zip(arglist, args), **env)),
    "define": lambda symbol, value, env, hook: [env.update({symbol: hook(value)}), "nil"][-1],
    "if": lambda test, trueform, falseform, env, hook: hook(trueform if hook(test) else falseform),
}

functions = {
    "atom": lambda symbol: type(symbol) is not list,
    "cons": lambda a, d: [a, d],
    "car": lambda cons: cons[0],
    "cdr": lambda cons: cons[1],
    "eq": lambda one, other: "t" if one is other else "nil",
}

constants = {
    "nil": (),
    "t": True,
}

Kind = Enum("Kind", ["Special", "Function", "Constant", "Lambda", "Bounded", "Unbounded"])

def symbol_value(symbol, env):
    if callable(symbol):
        return symbol, Kind.Lambda
    elif symbol in special_forms.keys():
        return special_forms[symbol], Kind.Special
    elif symbol in functions.keys():
        return functions[symbol], Kind.Function
    elif symbol in constants.keys():
        return constants[symbol], Kind.Constant
    elif symbol in env.keys():
        return env[symbol], Kind.Bounded
    else:
        return symbol, Kind.Unbounded
