def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    #is prime = [ True ] * ( n + 1)
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    largest_prime = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            largest_prime = i
            for j in range(i, n + 1, i):
                is_prime[j] = False
    return largest_prime


if __name__ == "__main__":
    import doctest
    doctest.testmod()
