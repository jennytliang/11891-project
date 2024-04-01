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
    """
    n = len(xs)
    assert n % 2 == 0
    d = n // 2
    # y^2 - s * y + t = 0
    x0 = -xs[d - 1] / xs[d]
    x1 = -xs[d] / xs[d]

    # Newton-Raphson Method
    while True:
        y0 = poly(xs, x0)
        y1 = poly(xs, x1)
        if y0 == 0.0:
            return x0
        elif y1 == 0.0:
            return x1
        else:
            x0, x1 = x1 - y1 / (y1 - y0) * x1, x0 - y0 / (y1 - y0) * x0
    return x0