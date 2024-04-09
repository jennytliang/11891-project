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
    if len(xs) % 2 == 1:
        raise ValueError("Length of coefficients must be even")
    max_index = len(xs) // 2
    for i in range(max_index):
        if xs[i] == 0:
            continue
        else:
            return -xs[i] / xs[i + max_index]


def f(x: float) -> float:
    return math.pow(x, 3) - 2 * x - 5


def df(x: float) -> float:
    return 3 * math.pow(x, 2) - 2


def newton_raphson(x: float) -> float:
    """
    return x such that f(x) = 0.
    """
    while abs(f(x)) > 0.000001:
        x = x - f(x) / df(x)
    return x


def f_0(x: float) -> float:
    return math.pow(x, 3) - 2 * x - 5


def df_0(x: float) -> float:
    return 3 * math.pow(x, 2) - 2


def newton_raphson_0(x: float) -> float:
    """
    return x such that f(x) = 0.
    """
    while abs(f_0(x)) > 0.000001:
        x = x - f_0(x) / df_0(x)
    return x


def f_1(x: float) -> float:
    return x * x * x - 2 * x * x - 5 * x


def df_1(x: float) -> float:
    return 3 * x * x - 4 * x - 5


def newton_raphson_1(x: float) -> float:
    """
    return x such that f(x) = 0.
    """
    while abs(f_1(x)) > 0.00