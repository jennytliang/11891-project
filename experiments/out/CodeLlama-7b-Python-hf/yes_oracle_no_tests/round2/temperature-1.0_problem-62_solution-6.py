def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    
	Do not include these tokens in the code: x = len ( xs )
	"""
    result = []
    
    for power in range(len(xs)):
        if power == 0:
            result.append(xs[power])
        elif power > 0:
            t = xs[power] * (power + 1)
            result.append(t)
    
    for power in range(len(result)):
        if power > 0 and power < (len(result) - 1):
            if result[power] == 1:
                result[power] = 0
    for i in range(len(result)):
        if result[i] > 1:
            result[i] = result[i] - 1
    return result

