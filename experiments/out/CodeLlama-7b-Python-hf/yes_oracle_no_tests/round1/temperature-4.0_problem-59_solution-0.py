def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: largest _ div or
	"""
    prime_factor = n
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            prime_factor = i
            n = n / i
            while n % i == 0:
                n = n / i
        i += 1
    return prime_factor


if __name__ == "__main__":
    import doctest
    doctest.testmod()