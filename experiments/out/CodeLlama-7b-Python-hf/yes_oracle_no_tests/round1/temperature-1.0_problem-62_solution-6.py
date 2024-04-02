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

    x = len(xs)
    return [xs[i+1]*i for i in range(x-1)]
    # return list(zip(*(t for t in enumerate(xs) if t[0] != 0)))[1]
    # return list(zip(*[t for t in enumerate(xs) if t[0] != 0]))[1]



def test():
    for method in [derivative]:
        for xs in [[1], [3, 1], [3, 1, 2], [3, 5, 1, 2], [3, 5, 1,
                                                                 2, 4]]:
            assert type(method(xs)) is type(xs)
            print(method(xs))

if __name__ == '__main__':
    test()
