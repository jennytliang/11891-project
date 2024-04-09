def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: ret = [] for
	"""
    ret = []
    for i in range(len(xs) - 1):
        ret.append(xs[i] * (i + 1))
    return ret


def derivative_recur(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative_recur([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative_recur([1, 2, 3])
    [2, 6]
    
	Include these tokens in the code: def
	"""
    if len(xs) == 1:
        return []
    return [xs[0] * len(xs)] + derivative_recur(xs[1:])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
