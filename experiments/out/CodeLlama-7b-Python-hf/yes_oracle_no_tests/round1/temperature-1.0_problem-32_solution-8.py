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
    a = xs[0]
    b = xs[1]
    c = xs[2]
    d = xs[3]
    if a == 0:
        raise ValueError("The coefficient of the highest degree term is zero")
    if b == 0:
        return -c / a
    else:
        return -b / (2 * a)


def derivative(xs: list):
    """
    xs are coefficients of a polynomial.
    derivative returns a list of coefficients of a polynomial's
    derivative.
    >>> derivative ([ 1, 2, 3, 4 ])
    [2, 4, 6]
    """
    return [xs[i] * (i + 1) for i in range(len(xs) - 1)]


def find_root(xs: list, x0: float, eps: float):
    """
    xs are coefficients of a polynomial.
    find_root returns a root of the polynomial.
    find_root uses Newton's method to find a root.
    The return value is a pair (x, k, err), where x is the estimated
    root, k is the number of iterations performed, and err is the estimated
    rounding error in x.
    >>> find_root ([ 1, -2, 1 ], 0, 1e-6)
    (0.5, 2, 0.0)
    """
    x = x0
    for k in range(1, 100):
        f = poly(xs, x)
        if f < 0:
            dx = -0.5
        else:
            dx = 0.5
        x = x + dx
        if abs(dx) < eps:
            break
    return x, k, abs(dx)


def f(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow