def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # is_prime = [True] * (n + 1)
    # is_prime[0] = is_prime[1] = False
    # for i in range(2, int(n ** 0.5) + 1):
    #     if is_prime[i]:
    #         for j in range(i * i, n + 1, i):
    #             is_prime[j] = False

    # return next(i for i in range(n, 1, -1) if is_prime[i])

    # 1. Get the largest factor of n
    # 2. Check if the largest factor is a prime
    # 3. If the largest factor is not a prime, return the largest factor
    # 4. If the largest factor is a prime, return the largest factor
    largest_factor = 1
    while n % 2 == 0:
        largest_factor = 2
        n /= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n /= i
    if n > 2:
        largest_factor = n
    return largest_factor


if __name__ == "__main__":
    import doctest

    doctest.testmod()
