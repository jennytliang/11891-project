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
    "*** YOUR CODE HERE ***"
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_factors(n):
    """Print the prime factors of n.
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(12)
    2
    2
    3
    """
    "*** YOUR CODE HERE ***"
    if is_prime(n):
        print(n)
    else:
        while n % 2 == 0:
            print(2)
            n = n // 2
        while n % 3 == 0:
            print(3)
            n = n // 3
        i = 5
        while n != 1:
            while n % i == 0:
                print(i)
                n = n // i
            i += 6



def prime_factors2(n):
    """Compute the prime factors of n.
    Return a list of tuples (prime, exponent).
    >>> prime_factors2(10)
    [(2, 1), (5, 1)]
    >>> prime_factors2(11)
    [(11, 1)]
    >>> prime_factors2(12)
    [(2, 2)]
    >>> prime_factors2(13441)
    [(17, 1), (19, 2), (23, 1)]
    >>> prime_factors2(123)
    [(11, 1), (13, 1)]
    """
    "*** YOUR CODE HERE ***"
    factors = []