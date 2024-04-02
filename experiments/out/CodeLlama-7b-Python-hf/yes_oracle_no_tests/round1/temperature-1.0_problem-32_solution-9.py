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
    if not xs:
        return "Error! no coefficients for polynomial."
    elif len(xs) % 2 != 0:
        return "Error! odd number of coefficients."
    elif any(n == 0 for n in xs):
        n = max(i for i, n in enumerate(xs) if n == 0)
        del xs[n]
    d = xs[1]
    dx = xs[0]
    x0 = dx / d
    dx = dx / d
    if not dx:
        return x0
    else:
        return find_root_newton(d, dx, -dx * x0, x0)


def find_roots(xs: list):
    """ xs are coefficients of a polynomial.
    find_root calculates roots of the polynomal.
    This function only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution. return values are sorted in descending order of absolute values.
    >>> find_roots([1, 2]) # f(x) = 1 + 2x
    []
    >>> find_roots([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    ['1.0', '-0.5']
    """

    def f(x): return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)]) - 0
    def df(x): return sum([i * coeff * math.pow(x, i-1) for i, coeff in enumerate(xs)])

    def newton_root_find(df, f, x0, k):
        xn = x0 - f(x0) / df(x0)
        if abs(xn-x0) < 10**(-k): return xn
        else:
            x0 = xn
            return newton_root_find(df, f, x0, k)

