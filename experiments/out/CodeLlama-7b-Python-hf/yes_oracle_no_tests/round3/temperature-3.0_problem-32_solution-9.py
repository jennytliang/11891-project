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
        raise ValueError
    if xs[0] != 0:
        raise ValueError
    x = 1.0
    while poly(xs, x) != 0:
        x += 1.0
    return x


def find_all_zeros(xs: list):
    """ xs are coefficients of a polynomial.
    find_all_zeros find all x such that poly(x) = 0.
    find_all_zeros returns list of all zero points.
    find_all_zeros only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> find_all_zeros([1, 2]) # f(x) = 1 + 2x
    [0.0]
    >>> find_all_zeros([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1.0, 2.0, 3.0]
    """
    if len(xs) % 2 != 0:
        raise ValueError
    if xs[0] != 0:
        raise ValueError
    x = 1.0
    zeros = []
    while poly(xs, x) != 0:
        zeros.append(x)
        x += 1.0
    return zeros


if __name__ == "__main__":
    import doctest
    doctest.testmod()
