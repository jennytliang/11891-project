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
    # first check if the coefficient list is valid
    assert len(xs) % 2 == 0
    assert max([abs(coeff) for coeff in xs[1:]]) != 0
    # find the first non zero coefficient
    first_non_zero = 0
    while xs[first_non_zero] == 0:
        first_non_zero += 1
    # find the second non zero coefficient
    second_non_zero = first_non_zero + 1
    while xs[second_non_zero] == 0:
        second_non_zero += 1
    # find the zero point
    return -xs[first_non_zero] / xs[second_non_zero]


def find_zeros(xs: list):
    """ xs are coefficients of a polynomial.
    find_zeros find x such that poly(x) = 0.
    find_zeros returns all zero points.
    find_zeros only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> find_zeros([1, 2]) # f(x) = 1 + 2x
    [-0.5]
    >>> find_zeros([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1.0, 2.0, 3.0]
    """
    # first check if the coefficient list is valid
    assert len(xs) % 2 == 0
    assert max([abs(coeff) for coeff in xs[1:]]) != 0
    # find the first non zero coefficient
    first_non_zero = 0
    while xs[first_non_zero] == 0:
        first_non_zero += 1
    # find the second non zero coefficient
    second_non_zero = first_non_zero + 1
    while xs[second_non_zero] == 0:
        second_non_zero +=