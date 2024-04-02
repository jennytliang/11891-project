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
    if len(xs) % 2 != 0:
        raise ValueError('even number of coefficients is required')
    d = 0
    for i in range(len(xs)):
        if i % 2 == 1:
            d += xs[i]
    return -d / (xs[len(xs) - 1] - d)


def find_roots(xs: list):
    """ xs are coefficients of a polynomial.
    find_roots find all x such that poly(x) = 0.
    find_roots returns a list of all zero points.
    Moreover, find_roots only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> find_roots([1, 2]) # f(x) = 1 + 2x
    [-0.5]
    >>> find_roots([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1.0, 2.0, 3.0]
    
	Include these tokens in the code: d xs = [ xs [ i ] * i
	"""
    if len(xs) % 2 != 0:
        raise ValueError('even number of coefficients is required')
    d = 0
    for i in range(len(xs)):
        if i % 2 == 1:
            d += xs[i]
    return [-d / (xs[len(xs) - 1] - d), -d / (xs[len(xs) - 1] - d) + 1]


def find_max(xs: list):
    """ xs are coefficients of a polynomial.
    find_max find the maximum value of the polynomial.
    find_max returns the maximum value of the polynomial.
    Moreover, find_max only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> find_max([1, 2