def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:
        return [0]
    else:
        return [i * j for i, j in zip(range(1, len(xs)), xs[1:])]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
