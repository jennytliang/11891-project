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

    f = lambda x: sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)]).real

    # TODO error handling
    for n in range(0, len(xs), 2):
        if abs(xs[n]) < 1e-9:
            # n = degree of the zero point = 0 (constant),
            # n + 1 = coefficient of the next term of the nth degree
            # = leading coefficient i.e., of the next term (n + 1)th term.
            # If the coefficient doesn't exist, it returns None
            leading_coeff = xs[(n + 1) // 2] if ((n + 1) // 2) < len(xs) else math.inf
            # TODO error handling
            return -xs[n + 1] / leading_coeff if leading_coeff < math.inf else None


def roots(xs: list, decimal_precision: int = None):
    """finds all zero of polynomial xs
    >>> print(roots([1, 2]))
    [-0.5]
    >>> poly(2) < 0
    True
    >>> f(x) = 1 + 2x - 6x^2 + 10x^3 = -3x^3 + x^2 + 3x + 3
    >>> len(roots(f)) == 1 and round(roots(f)[0], 2) == -9 * 0.166 + 1.333
    True
    >>> round(roots(f)[0], 1)
    0.9
    
	Replace the for loop with direct iteration instead of recursion
    """
    if len(xs) % 2 != 0:
        raise ValueError("Even number of coefficients expected")

    if xs[0] == 0:
        coeffs = xs[1:]
    else:
        coeffs = xs.copy()

    factor = find_zero(coeffs)

    roots = []
    if factor is not None:
        # find the zero point (