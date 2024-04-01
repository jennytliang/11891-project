def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return [xs[i] * i for i in range(1, len(xs))]


i = 0


def derivative_v2(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative_v2([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative_v2([1, 2, 3])
    [2, 6]
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""
    global i
    i = 1
    return [xs[i] * i for i in range(1, len(xs))]


def derivative_v3(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative_v3([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative_v3([1, 2, 3])
    [2, 6]
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""
    i = 1
    a = 1
    xs[0] = 0
    for x in xs:
        xs[i - 1] = a * i * x
        i += 1
        a += 1
    return xs


if __name__ == "__main__":
    import doctest

    doctest.testmod()
