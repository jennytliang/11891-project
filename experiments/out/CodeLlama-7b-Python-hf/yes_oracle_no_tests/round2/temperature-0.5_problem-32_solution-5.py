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
    # if len(xs) % 2 == 0:
    #     raise ValueError("list must have even number of coefficients")
    # if xs[0] != 0:
    #     raise ValueError("largest non zero coefficient must be the first coefficient")
    # if xs[0] == 0 and xs[1] == 0 and xs[2] == 0:
    #     raise ValueError("zero list")
    # if xs[0] == 0 and xs[1] == 0 and xs[2] != 0:
    #     raise ValueError("zero list")
    # if xs[0] == 0 and xs[1] != 0 and xs[2] != 0:
    #     raise ValueError("zero list")
    # if xs[0] != 0 and xs[1] == 0 and xs[2] != 0:
    #     raise ValueError("zero list")
    # if xs[0] != 0 and xs[1] != 0 and xs[2] == 0:
    #     raise ValueError("zero list")
    # if xs[0] != 0 and xs[1] != 0 and xs[2] != 0:
    #     return -xs[1] / (2 * xs[2])
    # else:
    #     return 0
    if len(xs) % 2 == 1:
        raise ValueError("list must have even number of coefficients")
    if xs[0] == 0 and xs[1] == 0:
        raise ValueError("zero list")
    if xs[0] == 0 and xs[1] != 0:
        return -xs[1] / xs[2]
    if xs[0] != 0 and xs[1] == 0:
        return 0
    else:
        return -xs[1] / (2 * xs[2])


def find_roots(xs: list):
    """ xs are coefficients of a polynomial.
    find_roots returns all roots of the polynomial.
    Note that the roots are not necessarily distinct.
    """
    if len