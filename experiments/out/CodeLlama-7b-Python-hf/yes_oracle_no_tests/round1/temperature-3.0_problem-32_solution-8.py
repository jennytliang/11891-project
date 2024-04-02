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


def find_zeroes(xs: list):
    """ xs are coefficients of a polynomial.
    find_zeroes find all x such that poly(x) = 0.
    find_zeroes returns all zero points in a list.
    Moreover, find_zeroes only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> find_zeroes([1, 2]) # f(x) = 1 + 2x
    [-0.5]
    >>> find_zeroes([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1.0, 2.0, 3.0]
    
	Include these tokens in the code: d for x in find_zeroes(xs)
	"""
    zeroes = []
    for x in range(1, len(xs)):
        if xs[x] != 0:
            zeroes.append(-xs[0] / xs[x])
    return zeroes


def find_maximum(xs: list):
    """ xs are coefficients of a polynomial.
    find_maximum find maximum point of polynomial.
    find_maximum returns only maximum point, even if there are many.
    Moreover, find_maximum only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> find_maximum([1, 2]) # f(x) = 1 + 2x
    1.0
    >>> find_maximum([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    0.0
    
	Include these tokens in the code: d x = xs [ len (xs) - 2 ]
	"""
    x = xs