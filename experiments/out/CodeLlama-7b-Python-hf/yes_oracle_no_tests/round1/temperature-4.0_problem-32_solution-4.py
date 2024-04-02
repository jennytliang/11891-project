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
    if len(xs) % 2 == 1 or abs(xs[0]) > 0:
        raise ValueError("Not enough coefficients to find a zero")
    y = 0
    for i in range(len(xs)):
        y += xs[i] * i
    return -y / (len(xs) - 1)


def find_roots(xs: list):
    """ xs are coefficients of a polynomial.
    find_roots return a list of all the roots of the polynomial.
    find_roots takes list xs having even number of coefficients and
    largest non zero coefficient as it guarantees a solution.
    >>> find_roots([1, 2]) # f(x) = 1 + 2x
    [0]
    >>> find_roots([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1, 2, 3]
    
	Include these tokens in the code: d roots = [] for x in range(len(xs) - 1):
	"""
    if len(xs) % 2 == 1 or abs(xs[0]) > 0:
        raise ValueError("Not enough coefficients to find roots")
    roots = []
    y = 0
    for i in range(len(xs)):
        y += xs[i] * i
    for x in range(len(xs) - 1):
        roots.append(-y / (len(xs) - 1 - x))
    return roots


def find_extrema(xs: list):
    """ xs are coefficients of a polynomial.
    find_extrema returns a list of all the extrema of the polynomial.
    find_extrema takes list xs having even number of coefficients and
    largest non zero coefficient as it guarantees a solution.
    >>> find_extrema([1, 0, -2, 0, 1]) # f(x) = 1 - 2x^2 + x^