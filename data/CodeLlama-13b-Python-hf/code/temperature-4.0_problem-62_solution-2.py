def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    result = [];
    for a_index in range(1, len(xs)):
        result.append(xs[a_index]*a_index); #result.append(coefficient * index_power);

    if ((len(result)!=0)): #if 1d array, nothing will happen. But it's actually 1d zero array, not zero value in Python.

        result = result[len(result)-len(xs):]; #

        # if (result != 0 or result != [], this result is zero.)
    return result;