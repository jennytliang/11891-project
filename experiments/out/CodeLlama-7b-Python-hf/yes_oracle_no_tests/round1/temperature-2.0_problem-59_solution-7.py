def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    if n == 1:
        return 1
    else:
        for i in range(2, n):
            if n % i == 0:
                n = n / i
                if is_prime(i):
                    return i


def is_prime(n: int):
    """Returns True if n is prime, otherwise False
    >>> is_prime(3)
    True
    >>> is_prime(20)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(13195)
    False
    >>> is_prime(2048)
    True
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
