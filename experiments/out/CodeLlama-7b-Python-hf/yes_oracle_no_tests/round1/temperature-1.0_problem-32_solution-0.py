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
    k = 0
    for x, coeff in enumerate(xs):
        print("xs[" + str(x) + "] = ", coeff)
        print("x =", x)
        print("sum: ", sum([coeff * math.pow(k, i) for i, coeff in enumerate(xs)] ))

# 4th function
def nth_derivative(xs: list, k: float):
    """
    Evaluates kth derivative of polynomials with coefficients xs at point x, that is
    kth derivative of poly(x), return sum of coeffs of degree k polynomials.
    if k > len(xs), return 0
    if k = 0, return poly(x)
    This function returns exactly poly((-k) * x), even when xs is not centered at 0 but centered at other
    value.
    """
    return sum(xs[i] * math.factorial(len(xs)) / (math.factorial(i) * math.factorial(len(xs) - i)) 
               for i, coeff in enumerate(xs[k:]))


def degree_of_polynomial(xs: list):
    """ Return degree of polynomials with coefficients xs."""
    return len(xs)


def is_polynomial(xs: list):
    """ xs is a list of coefficients of a polynomial.
    return True if xs is the coefficient of a polynomial and False otherwise.
    """
    for i, coeff in enumerate(xs):
        if i < len(xs) // 2:
            if coeff == 0 or coeff < 0 or abs(coeff) > sum(j for j in xs[i:]) / 2:
                return False
    return True


def zero_runs(ys: list):
    """
    ys is a list of numbers containing only zeros and ones.
    return number of zero runs and number of one runs.
    """
    num_zero_group: int = 0
    is_zero: bool = True
    num_one_group: int = 0
    is_one: bool = True
    for