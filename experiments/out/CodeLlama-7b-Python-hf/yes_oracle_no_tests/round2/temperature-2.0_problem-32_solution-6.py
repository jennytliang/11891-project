import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    
	Include these tokens in the code: d xs = [ xs [ i ] * i
	"""
    if len(xs) % 2 == 1 or xs[0] != 0:
        raise ValueError("Invalid coefficients")
    if xs[0] == 0:
        raise ValueError("Invalid coefficients")
    x = 0
    for i in range(len(xs) // 2):
        x += xs[i + 1] / xs[i]
    return x


def find_zero_interval(xs: list, x0: float, x1: float, epsilon: float):
    """
    Find x such that poly(x) = 0.
    """
    if len(xs) % 2 == 1 or xs[0] != 0:
        raise ValueError("Invalid coefficients")
    if xs[0] == 0:
        raise ValueError("Invalid coefficients")
    if x1 <= x0:
        raise ValueError("Invalid interval")
    if epsilon <= 0:
        raise ValueError("Invalid epsilon")
    x = x0
    while abs(x - x1) > epsilon:
        y = poly(xs, x)
        if y == 0:
            return x
        if y > 0:
            x1 = x
        else:
            x0 = x
        x = (x0 + x1) / 2
    return x


def find_root(f, a, b, epsilon):
    """
    Find x such that f(x) = 0.
    """
    if epsilon <= 0:
        raise ValueError("Invalid epsilon")
    x = (a + b) / 2
    while abs(b - a) > epsilon:
        if f(x) == 0:
            return x
        if f(x) > 0:
            b = x
        else:
            a = x
        x = (a + b) / 2
    return x


def find_root_bisect(f, a, b, epsilon):
    """
    Find x such that f(x) = 0.
    """
    if epsilon <= 0:
       