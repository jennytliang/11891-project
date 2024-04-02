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
    
	Include these tokens in the code: d xs = [ xs [ i ]
	Do not include these tokens in the code: return sum ([ co eff
	"""
    if len(xs) % 2 != 0:
        raise ValueError("There must be even number of coefficients.")
    if xs[0] != 0:
        raise ValueError("The largest non zero coefficient must be 0.")
    return -xs[1] / xs[2]


def find_all_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_all_zero find x such that poly(x) = 0.
    find_all_zero returns all zero points.
    Moreover, find_all_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> find_all_zero([1, 2]) # f(x) = 1 + 2x
    [-0.5]
    >>> find_all_zero([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1.0, 2.0, 3.0]
    
	Include these tokens in the code: d xs = [ xs [ i ]
	Do not include these tokens in the code: return sum ([ co eff
	"""
    if len(xs) % 2 != 0:
        raise ValueError("There must be even number of coefficients.")
    if xs[0] != 0:
        raise ValueError("The largest non zero coefficient must be 0.")

    roots = []
    for i in range(2, len(xs), 2):
        roots.append(-xs[i] / xs[i + 1])
    return roots


def diff(xs: list):
    """ xs are coefficients of a polynomial.
    diff returns list of coefficients of the derivative polynomial.
    >>> diff([1, 2, 3, 4]) # f(x) = 1 + 2x + 3x^2 + 4x^3
    [2, 6, 12]
    
	Include these tokens in the code: