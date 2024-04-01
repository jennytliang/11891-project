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
    assert n > 2
    assert abs(xs[n // 2]) > 0

    return -xs[n // 2] / xs[n // 2 - 1]


def find_roots(xs: list):
    """
    Return list of roots of the polynomial.
    >>> find_roots([1, -2, 0, 1])
    [-2.0, -1.0, 1.0]
    """
    n = len(xs)
    assert n % 2 == 0
    assert n > 2
    assert abs(xs[n // 2]) > 0

    roots = []
    for i in range(1, n, 2):
        roots.append(-xs[i] / xs[i - 1])

    return roots


def find_real_roots(xs: list):
    """
    Return list of real roots of the polynomial.
    >>> find_real_roots([1, -2, 0, 1])
    [-1.0, 1.0]
    """
    n = len(xs)
    assert n % 2 == 0
    assert n > 2
    assert abs(xs[n // 2]) > 0

    roots = []
    for i in range(1, n, 2):
        if xs[i] * xs[i - 1] > 0:
            roots.append(-xs[i] / xs[i - 1])

    return roots


if __name__ == "__main__":
    import doctest

    doctest.testmod()
