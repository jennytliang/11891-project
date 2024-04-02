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
    # if len (xs) % 2 == 1:
    #     raise ValueError ("Number of coefficients must be even.")
    # if xs[0] != 0:
    #     raise ValueError ("Largest non-zero coefficient must be 0.")
    # # your code here
    # return
    # if len (xs) % 2 == 1:
    #     raise ValueError ("Number of coefficients must be even.")
    # if xs[0] != 0:
    #     raise ValueError ("Largest non-zero coefficient must be 0.")
    # # your code here
    # return
    # if len (xs) % 2 == 1:
    #     raise ValueError ("Number of coefficients must be even.")
    # if xs[0] != 0:
    #     raise ValueError ("Largest non-zero coefficient must be 0.")
    # # your code here
    # return
    if len(xs) % 2 == 1:
        raise ValueError("Number of coefficients must be even.")
    if xs[0] != 0:
        raise ValueError("Largest non-zero coefficient must be 0.")
    # your code here
    return (1 - xs[1] / xs[2]) / (xs[3] / xs[2] - xs[1] / xs[2])


def find_zeros(xs: list):
    """ xs are coefficients of a polynomial.
    find_zeros find x such that poly(x) = 0.
    find_zeros returns a list of all zero points.
    Moreover, find_zeros only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> find_zeros ([ 1, 2, 1, 2, 1, 2 ]) # f(x) = 1 + 2x + 2x^2 + 2x^3 + 2x^4 + 2x^5
    [1.0, 1.0, 1.0]
    >>> find_zeros ([ 1, 2, 1