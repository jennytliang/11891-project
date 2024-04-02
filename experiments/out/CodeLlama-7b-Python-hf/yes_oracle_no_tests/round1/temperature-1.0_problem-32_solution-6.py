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
    if len(xs) % 2 == 1:
        print('Not even number of non-zero term in polynomial', xs)
        return None
    d = -xs[0]
    j = 1
    n = len(xs)
    xj = xs[j]
    xjold = xj
    while j < n:
        xjold += xj
        j += 1
        xj += xs[j]
    x0 = -xj / d
    xold = x0
    
    while abs(xold - x0) > 1e-10:
        oldcoeff = poly([xold, 1], xold) / xold
        xold = (poly(xs, xold) - oldcoeff) / d
        j = 1
        n = len(xs)
        xj = xs[j]
        xjold = xj
        while j < n:
            xjold += xj
            j += 1
            xj += xs[j]
        x0 -= xjold / (d + oldcoeff)
    return x0


def find_multiple_zeros(xs: list, numzeros: int):
    """ xs are coefficients of a polynomial and
    length of list xs is even.
    find_multiple_zero searches for numzeros zeros of polynomials.
    >>> find_multiple_zeros([-6, 11, -6, 1], 2)
    [-3.0, 1.0] """
    if len(xs) % 2 == 1:
        print('find_zeros takes even number of coefficients', xs)
        return None
    if numzeros not in range(1, len(xs) + 1):
        print('Too many zeros requested', numzeros, '>=', len(xs))
        return None
    result = []
    while len(result) < numzeros:
        x0 = find_zero(xs)
        coeff0 = poly(xs, x0) / x0
        dx = -coeff0
        result.append(x0)
