def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret =
	"""
    return [xs[i] * (i + 1) for i in range(len(xs) - 1)]


def derivative2(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret =
    """
    return [xs[i] * (i + 1) for i in range(len(xs) - 1)]


def main():
    import doctest
    doctest.testmod()
    xs = [3, 1, 2, 4, 5]
    xs2 = [1, 2, 3]
    print(derivative(xs))
    print(derivative2(xs2))


if __name__ == "__main__":
    main()
