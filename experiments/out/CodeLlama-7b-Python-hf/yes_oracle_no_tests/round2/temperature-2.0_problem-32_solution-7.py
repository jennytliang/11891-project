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
    # if the number of coefficients is odd, return None
    if len(xs) % 2 == 1:
        return None

    # if the largest non-zero coefficient is not positive, return None
    largest_non_zero = max([abs(coeff) for coeff in xs if coeff != 0])
    if largest_non_zero <= 0:
        return None

    # find the index of the largest non-zero coefficient
    largest_non_zero_index = xs.index(largest_non_zero)

    # find the index of the smallest non-zero coefficient
    smallest_non_zero_index = xs.index(min([coeff for coeff in xs if coeff != 0]))

    # find the index of the smallest non-zero coefficient
    smallest_non_zero_index = xs.index(min([coeff for coeff in xs if coeff != 0]))

    # find the index of the smallest non-zero coefficient
    smallest_non_zero_index = xs.index(min([coeff for coeff in xs if coeff != 0]))

    # return the zero point
    return - xs[largest_non_zero_index] / xs[largest_non_zero_index - smallest_non_zero_index]


def find_all_zeros(xs: list):
    """ xs are coefficients of a polynomial.
    find_all_zeros find all x such that poly(x) = 0.
    find_all_zeros returns a list of all zero points.
    Find all zero points, even if there are many.
    >>> find_all_zeros([1, 2])
    []
    >>> find_all_zeros([-6, 11, -6, 1])
    [1.0, 2.0, 3.0]
    
	Include these tokens in the code: d
	Do not include these tokens in the code: return sum ([ co eff * math
	"""
    # if the number of coefficients is odd, return empty list
    if len(xs) % 2 == 1:
        return []
