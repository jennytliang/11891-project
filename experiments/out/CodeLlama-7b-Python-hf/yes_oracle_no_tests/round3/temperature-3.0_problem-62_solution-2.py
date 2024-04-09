def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    
	Include these tokens in the code: 1 , len
	"""

    return [xs[i] * i for i in r]


def derivative2(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative2([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative2([1, 2, 3])
    [2, 6]
    
	Include these tokens in the code: 1 , len
	"""
    return [i * xs[i] for i in range(1, len(xs))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
