def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""

    for factor in xrange(n, 1, -2):
        candidate = n / factor
        if candidate * factor == n:
            return candidate

# 17
def smallest_divisor(n, upper_bound):
    """If n is an odd integer, some integer a divides n, 
    where 0<a<upper_bound. A key observation is that a must also be odd,
    otherwise n would have another divisor other than a. 
    Thus we need to look for odd divisors.

    >>> smallest_divisor(8, 20) # Should return 3
    3
    >>> smallest_divisor(9, 20) # Should return 3
    3
    >>> smallest_divisor(12, 20) # Should return 2
    2
    >>> smallest_divisor(24, 35) # Should return 3
    3
    >>> smallest_divisor(45, 50) # Should return 5
    5
    >>> smallest_divisor(36, 50) # Should return 5
    Traceback (most recent call last):
    ...
    ValueError: n<12
    
    https://stackoverflow.com/questions/51212/the-smallest-divisor-of-a-number 
    """