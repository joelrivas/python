# if cond == 'cond_a':
#     handle_a()
# elif cond == 'cond_b':
#     handle_b()
# else:
#     handle_default()


# def my_func(a, b):
#    return a + b


# funcs = [my_func]
# funcs[0](2, 3)

# func_dict = {
#     'cond_a': handle_a,
#     'cond_b': handle_b
# }

# func_dict[cond]()
# func_dict.get(cond, handle_default)()

# ----------------------------------------------------------------

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None


print(dispatch_if('mul', 2, 8))
# ----------------------------------------------------------------


def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y
    }.get(operator, lambda: None)()


print(dispatch_dict('mul', 2, 8))
