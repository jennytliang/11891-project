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
    assert len(xs) % 2 == 0 and max([abs(coeff) for coeff in xs]) != 0
    return -xs[0] / xs[1]


def find_roots(xs: list):
    """
    Finds all roots of a polynomial with coefficients xs.
    It returns a list of all roots of the polynomial.
    >>> find_roots([1, 2]) # f(x) = 1 + 2x
    [-2.0]
    >>> find_roots([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [-1.0, -2.0, -3.0]
    """
    assert len(xs) % 2 == 0 and max([abs(coeff) for coeff in xs]) != 0
    return [-xs[0] / xs[1]] if xs[1] != 0 else []


def find_extrema(xs: list):
    """
    Finds all extrema of a polynomial with coefficients xs.
    It returns a list of all extrema of the polynomial.
    >>> find_extrema([1, 2]) # f(x) = 1 + 2x
    []
    >>> find_extrema([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1.0, 2.0, 3.0]
    """
    assert len(xs) % 2 == 0 and max([abs(coeff) for coeff in xs]) != 0
    return [x / xs[1] for x in find_roots(xs)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
