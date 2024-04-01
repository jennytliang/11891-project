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
    assert len(xs) % 2 == 0
    assert max([abs(c) for c in xs[: len(xs) // 2 + 1]]) != 0
    return -xs[0] / xs[1]


def find_roots(xs: list):
    """ xs are coefficients of a polynomial.
    find_roots find x such that poly(x) = 0.
    find_roots returns all zero points.
    >>> find_roots([1, 2]) # f(x) = 1 + 2x
    [-0.5]
    >>> find_roots([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1.0, 2.0, 3.0]
    """
    return [
        -xs[0] / xs[i]
        for i in range(1, len(xs))
        if xs[i] != 0 and xs[i - 1] * xs[i] < 0
    ]


def find_extremum(xs: list):
    """ xs are coefficients of a polynomial.
    find_extremum find x such that poly'(x) = 0.
    find_extremum returns all zero points.
    >>> find_extremum([1, 2]) # f(x) = 1 + 2x
    []
    >>> find_extremum([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [2.0]
    """
    return [
        -xs[i] / (xs[i + 1] - xs[i - 1])
        for i in range(2, len(xs) - 2)
        if xs[i - 2] * xs[i + 1] < 0
    ]
