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


def find_maximum(xs: list):
    """
    xs are coefficients of a polynomial.
    find_maximum returns the point where the polynomial
    has the maximum value.
    >>> round(find_maximum([1, 2]), 2) # f(x) = 1 + 2x
    1.0
    >>> round(find_maximum([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    x = 0
    for i in range(len(xs)):
        x += xs[i] * math.pow(x, i)
    return x


def find_minimum(xs: list):
    """ xs are coefficients of a polynomial.
    find_minimum returns the point where the polynomial
    has the minimum value.
    >>> round(find_minimum([1, 2]), 2) # f(x) = 1 + 2x
    1.0
    >>> round(find_minimum([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    x = 0
    for i in range(len(xs)):
        x += xs[i] * math.pow(x, i)
    return x


def find_extremum(xs: list):
    """ xs are coefficients of a polynomial.
    find_extremum returns the point where the polynomial
    has the extremum value.
    >>> round(find_extremum([1, 2]), 2) # f(x) = 1 + 2x
    1.0
    >>> round(find_extremum([-6, 11, -6, 1]), 2) # (