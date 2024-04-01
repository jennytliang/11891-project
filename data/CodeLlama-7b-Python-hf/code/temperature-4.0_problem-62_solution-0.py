def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    result = []  # Create a new empty list of coefficients for the result, called results.
    xpowers = [list(x ** x for x in range(0, 5))]
    pow = 1  # Define a variable holding the power for which we are currently computing values of x
    y = xs.copy()  # Define another variable y, holding an array of the xs
    y0 = 0

    while ((pow < len(xpowers)):
