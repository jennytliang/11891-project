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
    assert len(xs) % 2 == 0
    assert max([abs(x) for x in xs[1::2]]) == xs[0]
    return -xs[1] / (xs[0] + 2 * xs[2])


def gcd(a: int, b: int):
    """
    return greatest common divisor of a and b
    """
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a: int, b: int):
    """
    return least common multiple of a and b
    """
    return abs(a * b) // gcd(a, b)


def gcd_list(xs: list):
    """
    return greatest common divisor of list xs
    """
    return math.prod(xs) // math.gcd.reduce(xs)


def lcm_list(xs: list):
    """
    return least common multiple of list xs
    """
    return math.prod(xs) // math.gcd.reduce([math.gcd.reduce(xs), math.prod(xs)])


def find_zero_of_polynomial(xs: list):
    """
    find_zero_of_polynomial returns a list of zero points
    of polynomial with coefficients xs
    """
    assert len(xs) % 2 == 0
    assert max([abs(x) for x in xs[1::2]]) == xs[0]
    if xs[0] == 0:
        return []
    # first, find a zero point x_0 such that x_0 is integer
    x_0 = -xs[1] / (xs[0] + 2 * xs[2])
    # if x_0 is not integer, find smallest integer n such that
    # n * x_0 is integer
    if not x_0.is_integer():
        n = math.floor(x_0)
        x_0 = n * x_0
    # now, find zero points recursively
    if xs[0] > 0:
        return [x_