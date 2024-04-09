def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	Do not include these tokens in the code: assert >
	"""
    # for i in range(2, n + 1):
    #     if n % i == 0:
    #         while n % i == 0:
    #             n //= i
    #         if n == 1:
    #             return i
    # return n

    max_prime = 0
    for i in range(2, n + 1):
        if n % i == 0:
            max_prime = i
            while n % i == 0:
                n //= i
    return max_prime


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(largest_prime_factor(13195))
    print(largest_prime_factor(2048))