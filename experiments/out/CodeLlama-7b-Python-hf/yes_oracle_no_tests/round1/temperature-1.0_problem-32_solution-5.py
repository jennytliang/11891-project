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
    
	Include these tokens in the code: d xs = [ xs [ i ]
	Do not include these tokens in the code: return sum ([ co eff
	"""
    # your code here
    if len(xs) % 2 == 1 or max([coeff for coeff in xs if coeff != 0]) != xs[0]:
        raise ValueError("Not enough coefficients or zero coefficient not largest")
    a = xs[0]
    b = xs[1]
    c = xs[2]
    if b ** 2 - 4 * a * c < 0:
        raise ValueError("No real solutions")
    elif b ** 2 - 4 * a * c == 0:
        return -b / (2 * a)
    else:
        return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
