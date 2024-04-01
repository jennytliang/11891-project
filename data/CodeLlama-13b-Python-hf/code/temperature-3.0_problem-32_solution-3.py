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
    assert len(xs) % 2 == 0

    # Find a point with one of the coefficient is 0, such as f(1) = 0.
    for idx in range(1, len(xs)):
        if xs[idx] == 0:
            return idx

    # This is the Newton method.
    x: float = xs[1] / xs[0]
    while abs(poly(xs, x)) > 0.0001:
        dx: float = (poly(xs, x) - 0) / (poly(xs[:idx], x) - poly(xs[:idx - 1], x))
        x = x + dx

    return x


if __name__ == "__main__":
    import doctest
    doctest.testmod()