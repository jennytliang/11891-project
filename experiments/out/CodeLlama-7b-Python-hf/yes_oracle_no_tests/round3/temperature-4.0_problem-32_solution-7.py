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
    return -xs[0] / xs[1]


def find_roots(xs: list):
    """
    find_roots find all zero points of a polynomial.
    return list of all zero points.
    """
    return [(-xs[0]) / xs[i] for i in range(2, len(xs))]


def find_extrema(xs: list):
    """
    find_extrema find all extrema of a polynomial.
    return list of all extrema points.
    """
    return [(-xs[i] * xs[i + 1]) / (xs[i] - xs[i + 2]) for i in range(len(xs) - 3)]
