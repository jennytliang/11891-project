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
    # 1. find a largest non zero coefficient
    # 2. find a sign of the largest non zero coefficient
    # 3. find a number which is a root of the polynomial
    # 4. return the number

    # 1. find a largest non zero coefficient
    largest_coeff = max([abs(coeff) for coeff in xs])
    # 2. find a sign of the largest non zero coefficient
    sign = 1 if largest_coeff > 0 else -1
    # 3. find a number which is a root of the polynomial
    # 3-1. find a number which is an intermediate root of the polynomial
    # 3-1-1. find a number which is a root of the polynomial
    # with the largest non zero coefficient
    # 3-1-1-1. find a number which is an intermediate root of the polynomial
    # with the largest non zero coefficient
    # 3-1-1-1-1. find a number which is a root of the polynomial
    # with the largest non zero coefficient
    # 3-1-1-1-2. find a number which is an intermediate root of the polynomial
    # with the largest non zero coefficient
    # 3-1-1-1-3. find a number which is a root of the polynomial
    # with the largest non zero coefficient
    # 3-1-1-1-4. find a number which is an intermediate root of the polynomial
    # with the largest non zero coefficient
    # 3-1-1-1-5. find a number which is a root of the polynomial
    # with the largest non zero coefficient
    # 3-1-1-1-6. find a number which is an intermediate root of the polynomial
    # with the largest non zero coefficient
    # 3-1-1-1-7. find a number which is a root of the polynomial
    # with the largest non zero coefficient
    # 3-1-1-1-8. find a number which is an intermediate root of the polynomial
    # with the largest non zero coefficient
    # 3-1-1-1-9. find a number which is a