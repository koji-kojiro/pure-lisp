from builtin import functions

def pprint(value, end="\n"):
    if value is True:
        print("t", end=end)
    elif type(value) is list:
        if not value:
            print("nil", end=end)
        else:
            print("(", end="")
            for element in value[:-1]:
                pprint(element, end=" ")
            pprint(value[-1], end=")\n")
    else:
        print(value, end=end)
    return "nil"

functions.update(print=lambda value: pprint(value))
