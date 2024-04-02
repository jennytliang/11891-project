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


def derivative_f(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative_f([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative_f([1, 2, 3])
    [2, 6]
    
	Include these tokens in the code: return [ xs [ i ] * i
	Do not include these tokens in the code: result = []
	"""
    return [xs[i] * i for i in range(len(xs))]


def derivative_g(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative_g([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative_g([1, 2, 3])
    [2, 6]
    
	Include these tokens in the code: return [ xs [ i ] * i
	Do not include these tokens in the code: result = []
	"""
    return [xs[i] * i for i in range(len(xs))]


def derivative_h(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative_h([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative_h([1, 2, 3])
    [2, 6]
    