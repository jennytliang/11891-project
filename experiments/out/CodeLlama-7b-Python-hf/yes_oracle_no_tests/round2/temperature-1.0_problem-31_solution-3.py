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
    #is_prime
    "*** YOUR CODE HERE ***"


def prime_factors(m):
    """Return a tuple of the prime factors of m.

    >>> prime_factors(100) # (2, 2, 5, 5)
    (2, 2, 5, 5)
    >>> prime_factors(8388608)
    (2, 3, 5, 7, 13, 29)
    >>> prime_factors(4)
    (2, 2)
    >>> prime_factors(6)
    (2, 3)
    >>> prime_factors(45) # Not prime
    (3, 3, 5)
    >>> prime_factors(0)
    ()
    
	Include these tokens in the code: while m %
    """
    #prime_factors
    "*** YOUR CODE HERE ***"



def accumulate_primes(n):
    """Return a tuple of all the prime numbers that occur before n.

    >>> accumulate_primes(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    >>> accumulate_primes(100)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97)
    """
    #accumulate_primes
    "*** YOUR CODE HERE ***"


def prime_sum(n):
    """Return the sum of all the primes that occur before n.
    
    >>> prime_sum(