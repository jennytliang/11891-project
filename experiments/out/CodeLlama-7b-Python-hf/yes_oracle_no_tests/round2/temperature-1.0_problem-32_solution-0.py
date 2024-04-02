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
    
	Include these tokens in the code: d
	Do not include these tokens in the code: return sum ([ co eff * math
	"""
    # math.pow is not expected in answer.
    # Use '**' instead of math.pow in the code.
    #
    # math.poly is not expected in answer.
    # Use poly function instead of it.
    #
    # Find the code that calls find_zero and edit. 
    # Change input from list to dictionary 'coefficients'.
    # Set 'coefficients' key to be coefficients of polynomial instead of an index.
    coefficients = {'coefficients': xs}
    
    # Edit here
    # Find the code that calls find_zero and edit
    # Change input parameter from x to root
    if len(xs) % 2 == 1 or xs[0] != 0 and len(xs[::2]) == len(xs) // 2:
        return TypeError('number of coefficients should be even, the largest non zero coefficient should be zero')
    sgn = [xs[i] / xs[0] for i in range(len(xs))]
    x_min = (-xs[1] / xs[2]) ** (1 / 2)
    x_max = (-xs[1] / xs[2] - max(sgn)) ** (1 / 2)

    def f(root):
        if root == 0:
            return max(sgn)
        return poly(xs, root)

    def bisection(x_min, x_max):
        while abs(poly(xs, x_max) - poly(xs, x_min)) >= 10 ** -10:
            x_mid = (x_min + x_max) / 2
            if (f(x_min) * f(x_mid) <= 0):
                x_max = x_mid
            else:
                x_min = x_mid
        return x_min, x_max

    def fixed_point():
        diff = 1
        while True:
            x_mid = (x_max + x_min) / 2
            diff = f(x_max) * f(x_min)
            if diff < 0:
                x_min, x