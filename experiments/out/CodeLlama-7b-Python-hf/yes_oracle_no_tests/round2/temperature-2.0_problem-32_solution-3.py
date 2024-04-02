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
    if len(xs) % 2 != 0 or xs[len(xs) // 2] == 0:
        raise ValueError("There is no zero point.")
    else:
        return -xs[len(xs) // 2] / xs[len(xs) // 2 - 1]


def find_max(xs: list):
    """
    find_max returns max value of polynomial with coefficients xs
    >>> find_max([1, 2, 3]) # f(x) = 1 + 2x + 3x^2
    6
    """
    return poly(xs, 1)


def find_min(xs: list):
    """
    find_min returns min value of polynomial with coefficients xs
    >>> find_min([1, 2, 3]) # f(x) = 1 + 2x + 3x^2
    -7
    """
    return poly(xs, -1)


def find_inflection_point(xs: list):
    """
    find_inflection_point returns inflection point of polynomial with coefficients xs
    >>> find_inflection_point([1, 2, 3]) # f(x) = 1 + 2x + 3x^2
    1.5
    """
    if len(xs) % 2 == 0 or xs[len(xs) // 2] == 0:
        raise ValueError("There is no inflection point.")
    else:
        return -xs[len(xs) // 2 - 1] / xs[len(xs) // 2]


def find_maximum_value(xs: list, a: float, b: float):
    """
    find_maximum_value returns maximum value of polynomial with coefficients xs in interval [a, b]
    >>> find_maximum_value([1, -2, 0, 4], 1, 3) # f(x) = 1 - 2x + 0x^2 + 4x^3
    22
    """
    return max([poly(xs, x) for x in [