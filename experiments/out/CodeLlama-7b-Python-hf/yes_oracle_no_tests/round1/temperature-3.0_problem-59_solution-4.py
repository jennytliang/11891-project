def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    prime_factors = []
    k = 2
    while k * k <= n:
        while n % k == 0:
            prime_factors.append(k)
            n //= k
        k += 1
    if n > 1:
        prime_factors.append(n)
    return max(prime_factors)


if __name__ == "__main__":
    import doctest
    doctest.testmod()