def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""

    assert n > 1, "only works for n > 1"
    assert not is_prime(n), "only works for n not prime"

    largest = 1
    for i in range(2, n+1):
        if n % i == 0:
            largest = i
            while n % i == 0:
                n = n // i

    return largest


def is_prime(n: int):
    """Return True if n is prime."""
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
