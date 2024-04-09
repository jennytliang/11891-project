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
    if len(xs) % 2 != 0 or xs[0] != 0:
        raise ValueError(
            "find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.")
    return -xs[1] / (2 * xs[2])


def find_roots(xs: list):
    """
    Evaluates polynomial with coefficients xs at point x.
    find_roots returns list of all zero points.
    >>> find_roots([1, 2]) # f(x) = 1 + 2x
    [-0.5]
    >>> find_roots([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1.0, 2.0, 3.0]
    """
    if len(xs) % 2 != 0 or xs[0] != 0:
        raise ValueError(
            "find_roots only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.")
    return [-xs[1] / (2 * xs[2])]


def eval_at_x(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    >>> eval_at_x([1, 2], 3) # f(x) = 1 + 2x
    8
    """
    return poly(xs, x)


def eval_at_xs(xs: list, xs_: list):
    """
    Evaluates polynomial with coefficients xs at points xs_.
    >>> eval_at_xs([1, 2], [3, 4]) # f(x) = 1 + 2x
    [8, 16]
    """
    return [eval_at_x(xs, x) for x in xs_]


def diff(xs: list):
    """
    Computes the derivative of polynomial with coefficients xs.
