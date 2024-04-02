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
    # if xs has odd number of coefficients or largest nonzero coefficient is 0, raise ValueError
    if len(xs) % 2 == 1 or xs[len(xs) // 2] == 0:
        raise ValueError("polynomial must have even number of coefficients and largest nonzero coefficient")
    # if xs has even number of coefficients, return the negative of the sum of the coefficients divided by the largest nonzero coefficient
    return -sum(xs) / xs[len(xs) // 2]


print(find_zero([1, 2]))
print(find_zero([-6, 11, -6, 1]))
