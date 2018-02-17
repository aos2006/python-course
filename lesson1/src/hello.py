def compose(f1, f2):
    return lambda *args: f1(f2(*args))

def check_args(price, vat):
    if type(price) == int and type(vat) == int:
        return price, vat
    else:
        return 0, 0

calculate_vat = compose(
    compose(lambda result: print(result), lambda args: args[0] / 100 * args[1]),
    check_args,
)

calculate_vat(3000, 18)

# calculate_vat(37800, 18)
