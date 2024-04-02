def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # TODO: implement this
    # for i in range(2, n):
    #     if n % i == 0:
    #         n = n // i
    #         break
    # return n

    # This is much faster than the above solution
    # because it is a prime factorization
    for i in range(2, n):
        if i * i > n:
            break
        if n % i == 0:
            while n % i == 0:
                n //= i
    return n


if __name__ == "__main__":
    import doctest

    doctest.testmod()
