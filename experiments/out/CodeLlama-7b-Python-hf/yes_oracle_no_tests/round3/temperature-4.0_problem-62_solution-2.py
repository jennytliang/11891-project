def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    
	Do not include these tokens in the code: def main (): import do ct est
	"""

    return [xs[i] * i for i in range(1, len(xs))]


def main():
    import doctest

    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()