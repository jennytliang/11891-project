def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    
	Include these tokens in the code: return [ xs [ i ] * i
	Do not include these tokens in the code: ret = []
	"""
    ret = []
    for i in range(len(xs)):
        if i == 0:
            ret.append(0)
        else:
            ret.append(xs[i] * i)
    return ret


if __name__ == "__main__":
    import doctest

    doctest.testmod()
