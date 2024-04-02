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
    return -1 * poly(xs, 1) / poly(xs, 2)


def find_roots(xs: list):
    """
    xs are coefficients of a polynomial.
    find_roots finds all roots of the polynomial.
    >>> find_roots([1, 2]) # f(x) = 1 + 2x
    [0.5]
    >>> find_roots([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1.0, 2.0, 3.0]
    """
    return [find_zero(xs[i:]) for i in range(len(xs) // 2)]


def find_max(xs: list):
    """
    find_max returns the max value of the polynomial.
    >>> find_max([1, 2]) # f(x) = 1 + 2x
    3.0
    >>> find_max([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    11.0
    """
    return poly(xs, 1)


def find_min(xs: list):
    """
    find_min returns the min value of the polynomial.
    >>> find_min([1, 2]) # f(x) = 1 + 2x
    -1.0
    >>> find_min([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    -6.0
    """
    return poly(xs, 0)


def poly_interpolation(xs: list, ys: list):
    """
    poly_interpolation returns the coefficients of