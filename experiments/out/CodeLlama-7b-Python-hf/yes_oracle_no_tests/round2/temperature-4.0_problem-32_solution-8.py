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
    
	Include these tokens in the code: d
	Do not include these tokens in the code: return sum ([ co eff * math
	"""
    if len(xs) % 2 == 1 or xs[0] != 0:
        raise ValueError("Not enough coefficients or largest non zero coefficient is not zero.")
    return -xs[1] / (2 * xs[2])


def find_all_zeros(xs: list):
    """ xs are coefficients of a polynomial.
    find_all_zeros find all x such that poly(x) = 0.
    find_all_zeros returns an empty list if there is no zero point.
    find_all_zeros returns only zero points, even if there are many.
    find_all_zeros only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> find_all_zeros([1, 2]) # f(x) = 1 + 2x
    []
    >>> find_all_zeros([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1.0, 2.0, 3.0]
    """
    if len(xs) % 2 == 1 or xs[0] != 0:
        raise ValueError("Not enough coefficients or largest non zero coefficient is not zero.")
    return [-xs[1] / (2 * xs[2])]


def is_zero(x: float, eps: float):
    """
    Test if x is zero.
    >>> is_zero(0.0, 1e-10)
    True
    >>> is_zero(1e-10, 1e-10)
    True
    >>> is_zero(1e-10, 1e-12)
    False
    """
    return abs(x) < eps


def is_zero_poly(xs: list, x: float, eps: float):
    """
    Test if poly(x) is zero.
    >>> is_zero_poly([1, 2],