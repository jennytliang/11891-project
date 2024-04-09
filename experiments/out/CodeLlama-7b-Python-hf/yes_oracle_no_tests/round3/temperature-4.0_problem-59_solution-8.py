def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    # if n % 2 == 0:
    #     return 2
    # for i in range(3, n, 2):
    #     if n % i == 0:
    #         return i
    # return n
    # return max(i for i in range(2, n) if n % i == 0)
    # from math import sqrt
    # from math import ceil
    # sqrt_n = ceil(sqrt(n))
    # for i in range(2, sqrt_n + 1):
    #     if n % i == 0:
    #         return i
    # return n
    # if n % 2 == 0:
    #     return 2
    # i = 3
    # while i * i <= n:
    #     if n % i == 0:
    #         return i
    #     i += 2
    # return n
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(largest_prime_factor(600851475143))
