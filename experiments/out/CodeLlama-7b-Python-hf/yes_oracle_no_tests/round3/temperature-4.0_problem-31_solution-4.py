def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret =
	"""


    if n == 1 or n == 2:
        return True
    if n == 3 or n == 5:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    return False


def prime_factors(n):
    """Print out all the prime factors of a given number.
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(14)
    2
    7
    >>> prime_factors(17)
    17
    >>> prime_factors(25)
    5
    >>> prime_factors(27)
    3
    3
    >>> prime_factors(30)
    2
    3
    5
    """
    for i in range(1, n + 1):
        if is_prime(i):
            if n % i == 0:
                print(i)
                n = n / i
                i = 1


def prime_factors_mult(n):
    """Return a list of all the prime factors of a given number.
    >>> prime_factors_mult(10)
    [2, 5]
    >>> prime_factors_mult(14)
    [2, 7]
    >>> prime_factors_mult(17)
    [17]
    >>> prime_factors_mult(25)
    [5]
    >>> prime_factors_mult(27)
    [3, 3]
    >>> prime_factors_mult(30)
    [2, 3, 5]
    """
    factors = []
    for i in range(1, n + 1):
        if is_prime(i):
            if n % i == 0:
                factors.append(i)
                n = n / i
                i = 1
    return factors


def prime_list(n):
    """Return a list containing all the prime numbers up to a given number.
    >>> prime_list(5)
    [2, 3,