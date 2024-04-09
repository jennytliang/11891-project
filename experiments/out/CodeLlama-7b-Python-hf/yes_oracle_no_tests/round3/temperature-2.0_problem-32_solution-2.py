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
    if len(xs) % 2 == 1 or max(xs) != xs[0]:
        return None
    x = 0
    for i in range(len(xs)):
        x += xs[i] / math.factorial(i)
    return x
    # TODO: Add the following line after implementing the find_zero function
    # raise NotImplementedError


def f(x):
    return x * x - 1


def f_prime(x):
    return 2 * x


def newton(x0, f, f_prime):
    """
    newton returns x such that f(x) = 0.
    >>> round(newton(1.5, f, f_prime), 2)
    1.0
    >>> round(newton(0.5, f, f_prime), 2)
    1.0
    >>> round(newton(-0.5, f, f_prime), 2)
    1.0
    """
    x = x0
    while True:
        x_new = x - f(x) / f_prime(x)
        if abs(x - x_new) < 1e-10:
            return x_new
        x = x_new
    # TODO: Add the following line after implementing the newton function
    # raise NotImplementedError


def f_1(x):
    return x * x * x - 2 * x * x + 3


def f_prime_1(x):
    return 3 * x * x - 4 * x


def f_2(x):
    return x * x - 2


def f_prime_2(x):
    return 2 * x


def f_3(x):
    return math.sin(x)


def f_prime_3(x):
    return math.cos(x)


def f_4(x):
    return math.exp(x) - x


def f_prime_4(x):
    return math.exp(x) + 