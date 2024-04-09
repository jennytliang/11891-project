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
    n = len(xs)
    assert n % 2 == 0
    assert xs[n // 2] != 0
    return -xs[n // 2] / (xs[n // 2 - 1] - xs[n // 2])


def find_min(xs: list, min_x: float, max_x: float):
    """
    Find min of the polynomial with coefficients xs in the interval [min_x, max_x].
    return a tuple of (min_x, min_y)
    """
    min_y = float("inf")
    min_x = float("inf")
    for x in range(min_x, max_x + 1):
        y = poly(xs, x)
        if y < min_y:
            min_y = y
            min_x = x
    return min_x, min_y


def find_max(xs: list, min_x: float, max_x: float):
    """
    Find max of the polynomial with coefficients xs in the interval [min_x, max_x].
    return a tuple of (min_x, min_y)
    """
    max_y = float("-inf")
    max_x = float("-inf")
    for x in range(min_x, max_x + 1):
        y = poly(xs, x)
        if y > max_y:
            max_y = y
            max_x = x
    return max_x, max_y


def find_min_and_max(xs: list, min_x: float, max_x: float):
    """
    Find min and max of the polynomial with coefficients xs in the interval [min_x, max_x].
    return a tuple of (min_x, min_y, max_x, max_y)
    """
    min_y = float("inf")
    min_x = float("inf")
    max_y = float("-inf")
    max_x = float("-inf")
    for x in range(min_x, max_x + 1):