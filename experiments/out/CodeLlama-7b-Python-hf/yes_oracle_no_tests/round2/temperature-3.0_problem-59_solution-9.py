def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(2, n // i + 1):
                is_prime[i * j] = False
    for i in range(n, 0, -1):
        if is_prime[i]:
            return i


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(largest_prime_factor(600851475143))
