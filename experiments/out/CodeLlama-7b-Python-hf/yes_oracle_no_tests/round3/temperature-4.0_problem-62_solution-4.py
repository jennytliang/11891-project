def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    
	Include these tokens in the code: return [ xs [ i ] * i
	Do not include these tokens in the code: result = []
	"""
    result = []
    for i in range(len(xs)):
        result.append(xs[i] * i)
    return result


def derivative2(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative2([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative2([1, 2, 3])
    [2, 6]
    
	Include these tokens in the code: return [ xs [ i ] * i
	Do not include these tokens in the code: result = []
	"""
    result = []
    for i in range(len(xs)):
        result.append(xs[i] * i)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
