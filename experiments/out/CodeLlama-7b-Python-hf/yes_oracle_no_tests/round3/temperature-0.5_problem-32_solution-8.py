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
    return (-xs[1] / xs[2]) + (xs[3] / xs[2])


def is_prime(x: int):
    """
    >>> is_prime(5)
    True
    >>> is_prime(13)
    True
    >>> is_prime(15)
    False
    """
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def find_primes(n: int):
    """
    >>> find_primes(6)
    [2, 3, 5]
    >>> find_primes(11)
    [2, 3, 5, 7, 11]
    >>> find_primes(15)
    [2, 3, 5, 7, 11, 13]
    """
    primes = [2, 3]
    i = 4
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes


def find_min_max(xs: list):
    """
    >>> find_min_max([1, 2, 3, 4, 5])
    (1, 5)
    >>> find_min_max([3, 1, 2, 5, 4])
    (1, 5)
    >>> find_min_max([5, 4, 3, 2, 1])
    (1, 5)
    """
    return (min(xs), max(xs))


def find_mean(xs: list):
    """
    >>> find_mean([1, 2, 3, 4, 5])
    3.0
    >>> find_mean([3, 1, 2, 5, 4])
    3.0
    >>> find_mean([5, 4, 3, 2, 