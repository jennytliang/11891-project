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
    
	Include these tokens in the code: d
	Do not include these tokens in the code: return sum ([ co eff * math
	"""
    if len(xs) % 2 != 0:
        return "There are odd number of coefficients."
    if max([abs(i) for i in xs[1::2]]) != xs[0]:
        return "The largest coefficient is non zero."
    x = 1
    while poly(xs, x) != 0:
        x += 1
    return x


def f(x: float):
    return 3 * x ** 3 + 2 * x ** 2 + 4 * x + 1


def f_prime(x: float):
    return 9 * x ** 2 + 4 * x + 4


def f_second_derivative(x: float):
    return 18 * x + 4


def newton_method(x_0: float, max_iter=100):
    """
    newton_method finds a root of f in [a, b]
    newton_method returns (x, i) where x is a root of f and i is the number of iterations.
    >>> newton_method(0, 100)
    (1.0, 0)
    """
    x = x_0
    for i in range(max_iter):
        x = x - f(x) / f_prime(x)
        if f_prime(x) == 0:
            return x, i
    return x, i


def bisect(f, a, b, max_iter=100):
    """
    bisect finds a root of f in [a, b]
    bisect returns (x, i) where x is a root of f and i is the number of iterations.
    >>> bisect(lambda x: x ** 3 - x - 1, 1, 2)
    (1.6180339887498949, 0)
    """
    x = (a + b) / 2
    for i in range(max_iter):
        if f(a) * f(x) > 0:
            a = x
