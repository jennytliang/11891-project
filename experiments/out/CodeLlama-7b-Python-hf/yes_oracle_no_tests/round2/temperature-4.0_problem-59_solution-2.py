def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # Your code here
    largest_prime_factor = 1
    for i in range(2, n + 1):
        while n % i == 0:
            n = n // i
            largest_prime_factor = i
    return largest_prime_factor


if __name__ == "__main__":
    import doctest

    doctest.testmod()
