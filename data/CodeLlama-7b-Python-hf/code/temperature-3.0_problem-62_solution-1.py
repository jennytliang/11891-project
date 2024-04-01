def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [n * xs[i] for i, n in enumerate(xs[:-1])]


def derivative_(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative_([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative_([1, 2, 3])
    [2, 6]
    """

    result = []
    if len(xs) < 2:
        return result

    i = 1
    while i + 1 <= len(xs) - 1:
        result.append(xs[i] * (i + 1))
        i += 1
    return result
