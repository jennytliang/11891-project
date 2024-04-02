def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    for i in range(2, n):
        if n % i == 0:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
            if is_prime:
                return i


def smallest_prime_factor(n: int):
    """Return the smallest prime factor of n. Assume n > 1 and is not a prime.
    >>> smallest_prime_factor(13195)
    19
    >>> smallest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    for i in range(2, n):
        if n % i == 0:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
            if is_prime:
                return i


def sum_of_divisors(n: int):
    """Sum of all divisors of n.
    >>> sum_of_divisors(100)
    200
    >>> sum_of_divisors(0)
    0
    >>> sum_of_divisors(1)
    1
    >>> sum_of_divisors(10)
    16
    >>> sum_of_divisors(17)
    17
    >>> sum_of_divisors(18)
    36
    >>> sum_of_divisors(20)
    48
    >>> sum_of_divisors(24)
    48
    >>> sum_of_divisors(1000)
    23279200
    >>> sum_of_divisors(2000)
    28800000
    >>> sum_of_divisors(10000)
    2880