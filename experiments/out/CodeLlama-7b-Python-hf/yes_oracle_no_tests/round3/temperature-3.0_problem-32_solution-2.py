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
    
	Include these tokens in the code: d xs = [ xs [ i ]
	Do not include these tokens in the code: return sum ([ co eff
	"""
    if len(xs) % 2 != 0:
        return None
    if xs[0] != 0 and xs[0] == max(xs):
        return None
    return -xs[0] / xs[1]


def f(x: float):
    """
    This is a function that is used for testing.
    """
    return math.pow(x, 3) - 2 * math.pow(x, 2) + math.pow(x, 1)


def fp(x: float):
    """
    This is a function that is used for testing.
    """
    return 3 * math.pow(x, 2) - 4 * x


def newton(x: float):
    """
    This is a function that is used for testing.
    """
    return x - f(x) / fp(x)


def find_zero_newton(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero_newton find x such that poly(x) = 0.
    find_zero_newton returns only only zero point, even if there are many.
    Moreover, find_zero_newton only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero_newton([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero_newton([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    
	Include these tokens in the code: d xs = [ xs [ i ]
	Do not include these tokens in the code: return sum ([ co eff
	"""
    if len(xs) % 2 != 0:
        return None
    if xs[0] != 0 and xs[0] == max(xs):
        return