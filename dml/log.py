import dml.constants as c

#------------------------------------------------------------------------------------

def ln(x, terms=100):
    if x <= 0:
        raise ValueError("ln is undefined for non-positive values")
    
    e = c.MathematicalConstants.E
    n = 0
    while x > 2:
        x /= e
        n += 1
    while x < 1:
        x *= e
        n -= 1
    
    y = (x - 1) / (x + 1)
    y_pow = y
    result = 0.0

    for i in range(terms):
        result += y_pow / (2 * i + 1)
        y_pow *= y * y

    return 2 * result + n

def log(x, base = 10, terms=100):
    ln_x = ln(x, terms)
    ln_base = ln(base, terms)
    if ln_base == 0:
        raise ZeroDivisionError("Base must not be 1")
    return ln_x / ln_base

def log2(x):
    return log(x, 2)

def log10(x):
    return log(x, 10)