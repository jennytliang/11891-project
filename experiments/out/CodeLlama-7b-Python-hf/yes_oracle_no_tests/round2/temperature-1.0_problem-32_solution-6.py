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
    assert (len(xs) % 2 == 0)
    assert (max(filter(lambda x: x != 0, xs[1::2])) == xs[0])
    y = -xs[0]
    for n, c in enumerate(xs[1:]):
        n = int(n / 2 + 1)
        y = y + c * math.pow(n, 2)
    return y


def newton_raphson(f: list, x: float, eps: float):
    """
    Newton Raphson method: x[i+1] = x[i] - f(x[i]) / f'_(x[i])
    """
    f_ = lambda x: f[0] + x * f[1]
    f_prime_ = lambda x: f[1]
    while (abs(f_(x)) > eps):
        x = x - f_(x) / f_prime_(x)
    return x


def regula_falsi(f: list, xl: float, xr: float, eps: float):
    """
    Regua falsi has 4 steps:
    step a. Choose interval
    step b-c Choose starting points where f(l) * f(r) < 0
    step d. Solve f(x) = 0 by halving width of interval [l, r]
    step e. Return solution with steps l and r.
    """
    f_ = lambda x: f[0] + x * f[1]
    f_prime_ = lambda x: f[1]
    assert (f_(xl) * f_(xr) < 0)
    # step d
    while True:
        x = (xl + xr) / 2
        if abs(f_(x)) <= eps:
            break
        else:
            fxl = f_(xl)
            fx = f_(x)
            fyr = f_(xr)

            if fxl * fx < 0:
                # f(xl) * fx < 0
                xr = x
