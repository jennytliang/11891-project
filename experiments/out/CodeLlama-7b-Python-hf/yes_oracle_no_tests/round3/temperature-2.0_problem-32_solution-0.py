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
    return -1 * (xs[1] / xs[2]) + (xs[0] / xs[2])


def find_roots(xs: list):
    """ xs are coefficients of a polynomial.
    find_roots find all x such that poly(x) = 0.
    find_roots returns a list of all zero points.
    Moreover, find_roots only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> find_roots([1, 2]) # f(x) = 1 + 2x
    [-0.5]
    >>> find_roots([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1.0, 2.0, 3.0]
    
	Include these tokens in the code: d
	Do not include these tokens in the code: return sum ([ co eff * math
	"""
    return [(-1 * (xs[1] / xs[2]) + (xs[0] / xs[2]))]


def poly_derivative(xs: list):
    """
    xs are coefficients of a polynomial.
    poly_derivative returns a list of coefficients of the derivative of
    poly(xs)
    >>> poly_derivative([1, 2]) # f(x) = 1 + 2x
    [2]
    >>> poly_derivative([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [11, -12, 6]
    """
    return [(i + 1) * coeff for i, coeff in enumerate(xs[1:])]


def poly_integral(xs: list):
    """
    xs are coefficients of a polynomial.
    poly_integral