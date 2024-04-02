def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: largest _ div or
	"""

    # Your code here
    prime_factors = []
    prime_factor = 2
    while prime_factor < n:
        if not n % prime_factor:
            prime_factors.append(prime_factor)
            n //= prime_factor
        else:
            prime_factor += 1
    return prime_factors[-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
