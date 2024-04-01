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
    assert not xs[-1] == 0, "Coefficient must have finite non-zero leading coefficient"
    low = -10 ** 5
    high = 10 ** 5
    diff_min = high
    for x in xs:
        assert x < 10 ** 5 and x > -10 ** 5,\
            "X must lie in finite region. Too large coefficient {x}".format(x=x)
        diff = math.fabs(xs[0] - poly(xs[:-1], x))
        assert diff < (10 ** -3),\
            "Loss of resolution for {xs} in {x} is too big to guarantee the zero point exists: diff={y}".\
            format(xs=xs, x=str(x), y=diff)
        if x > low and x <= high:
            if diff < diff_min:
                diff_min, low = diff, x
            else:
                high = x
