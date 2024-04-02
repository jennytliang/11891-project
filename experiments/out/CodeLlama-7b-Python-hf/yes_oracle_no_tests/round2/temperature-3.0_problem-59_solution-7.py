def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    #
    # Your code here
    #
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            n //= i
            i = 2
        else:
            i += 1
    return n


if __name__ == "__main__":
    import doctest
    doctest.testmod()