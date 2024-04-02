import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    
	Include these tokens in the code: d xs = [ xs [ i ] * i
	"""
    # assert len(xs) % 2 == 0, "Invalid polynomial"
    # assert xs [ 0 ] != 0, "Invalid polynomial"
    # assert xs [ -1 ] != 0, "Invalid polynomial"
    # assert xs [ -1 ] > 0, "Invalid polynomial"

    # TODO: fill in the code here
    # use poly(x) == 0 to find the zero point
    # use poly(x) < 0 or poly(x) > 0 to find the zero point
    # use poly(x) < 0 and poly(x+delta) > 0 to find the zero point
    # return zero point

    # TODO: write a test for this function
    # assert find_zero([1, 2]) == -0.5
    # assert find_zero([-6, 11, -6, 1]) == 1.0
    # assert find_zero([1, 0, 0, 0]) == -1
    # assert find_zero([0, 0, 1]) == -1
    # assert find_zero([0, 1, 0]) == 1
    # assert find_zero([0, 1]) == 1
    # assert find_zero([0, 0, 1, 0]) == -1
    # assert find_zero([0, 1, 0, 0]) == 1
    # assert find_zero([-6, 11, -6, 1, 0, 0]) == 1.0
    # assert find_zero([0, 1, 0, 0, 0, 1]) == 1.0
    # assert find_zero([0, 1, 0, 0, -1, 0, 1]) == 1.0
    # assert find_zero([0, 1, 0, 0, 0, 1, 0, 1]) == 1.0
    # assert find_zero([0, 1, 0, 0, -1, 0, 1, 0, 1]) == 1.0
   