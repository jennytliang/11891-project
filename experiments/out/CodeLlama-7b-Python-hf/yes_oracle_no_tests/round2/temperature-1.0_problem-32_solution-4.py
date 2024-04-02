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
    return - xs[0] / xs[1] if xs[1] != 0 else 0 

    # pass


def inverse_poly(xs: list):
    """
    Inverting polynomial.
    Finds the coefficients of inverse of poly, that is
    a polynomial that is the inverse of poly if it exists.
    Example:
        poly(xs, x) = poly(xs, 0)      # zero
        poly(xs, x) = poly(xs, 1)      # identity
        poly(xs, x) = poly(xs, -1/+0)  # reflection
        poly(xs, x) = poly(xs, 1/x)    # scaling
    returns coefficients of inverse if it exist
    """
    if poly(xs, 0) == 0:
        xs.pop(0)

    if len(xs) <= 0:
        raise ValueError("Coefficient list is empty")

    if len(xs) % 2 != 0 or abs(xs[-1]) <= 1e-56:
        raise ValueError(f"Does not exist")

    n = [0 for _ in range(len(xs) - 1, 0, -2)]

    i = len(n)
    while i > 0:
        n[i] = xs[2*i - 1] / xs[-1]
        i -= 1

    return (1, *n)

