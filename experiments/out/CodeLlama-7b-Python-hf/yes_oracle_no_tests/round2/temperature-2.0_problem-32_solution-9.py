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
    # Your code here
    if len(xs) % 2 == 1 or max([abs(x) for x in xs]) == 0:
        raise ValueError("Invalid polynomial")
    mid = len(xs) // 2
    return -xs[mid] / xs[mid - 1]


def find_roots(xs: list):
    """
    find_roots returns all roots of polynomial with coefficients xs.
    """
    # Your code here
    if len(xs) % 2 == 1 or max([abs(x) for x in xs]) == 0:
        raise ValueError("Invalid polynomial")
    roots = []
    for i in range(0, len(xs), 2):
        roots.append(-xs[i] / xs[i + 1])
    return roots


def f(x: float):
    """
    Evaluates polynomial f at x.
    f(x) = 3 + 2x - 4x^2 + 3x^3
    """
    return 3 + 2 * x - 4 * math.pow(x, 2) + 3 * math.pow(x, 3)


def f_derivative(x: float):
    """
    Evaluates polynomial f derivative at x.
    f'(x) = 2 - 8x + 9x^2
    """
    return 2 - 8 * x + 9 * math.pow(x, 2)


def find_root(f: callable, f_derivative: callable, x: float):
    """
    find_root returns x such that f(x) = 0.
    find_root uses Newton's method and requires f and f_derivative.
    f_derivative is the derivative of f.
    >>> round(find_root(f, f_derivative, 0), 2)
    0.58
    """
    while abs(f(x)) > 0.01:
        x = x - f(x) / f_derivative(x)
    return