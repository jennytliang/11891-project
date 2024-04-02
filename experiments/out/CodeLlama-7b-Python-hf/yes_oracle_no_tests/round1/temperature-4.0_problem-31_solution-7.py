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
    
	Include these tokens in the code: if n <=
	"""
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def find_primes(n):
    """Return a list of prime numbers less than n.
    >>> find_primes(6)
    [2, 3, 5]
    >>> find_primes(13)
    [2, 3, 5, 7, 11, 13]
    >>> find_primes(101)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes


def find_primes_for_loop(n):
    """Return a list of prime numbers less than n.
    >>> find_primes_for_loop(6)
    [2, 3, 5]
    >>> find_primes_for_loop(13)
    [2, 3, 5, 7, 11, 13]
    >>> find_primes_for_loop(101)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    primes = []
    for i in range(2, n):
        is_prime