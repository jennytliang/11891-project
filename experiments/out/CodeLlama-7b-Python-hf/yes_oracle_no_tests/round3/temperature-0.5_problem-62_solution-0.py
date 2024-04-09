def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    
	Include these tokens in the code: xs
	Do not include these tokens in the code: x
	"""



    return [xs[i] * i for i in range(1, len(xs))]




def integral(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return integral of this polynomial in the same form.
    >>> integral([3, 1, 2, 4, 5])
    [3, 1, 2, 4, 5]
    >>> integral([1, 2, 3])
    [0, 1, 3, 6]
    
	Include these tokens in the code: xs
	Do not include these tokens in the code: x
	"""



    return [xs[i] * i for i in range(0, len(xs))]




def eval(xs: list, x: int):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return value of this polynomial at x.
    >>> eval([3, 1, 2, 4, 5], 0)
    3
    >>> eval([1, 2, 3], 1)
    7
    
	Include these tokens in the code: xs, x
	Do not include these tokens in the code:
	"""



    return sum([xs[i] * x ** i for i in range(0, len(xs))])




def roots(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return list of roots of this polynomial.
    >>> roots([3, 1, 2, 4, 5])
    [1, 2]
    >>> roots([1, 2, 3])
    []
    
	Include these tokens in the code: xs
	Do not include these tokens in the code:
	"""



    return []




def print_polynomial(xs: list):
    """ xs represent coefficients of a polynomial.
   