def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # Initialize the list of primes.
    # Assume n > 1 and is not a prime.
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False

    # Loop through all the numbers from 2 to n.
    for i in range(2, n + 1):
        # If the number is prime, mark all its multiples as non-prime.
        if primes[i]:
            for j in range(i, n + 1, i):
                primes[j] = False
    # We have now marked all the non-primes,
    # so all that remains is to find the largest prime.
    for i in range(n, 1, -1):
        if primes[i]:
            return i


def prime_factors(n: int):
    """Return a list of the prime factors of n. Assume n > 1 and is not a prime.
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(7)
    [7]
    """
    # Initialize the list of primes.
    # Assume n > 1 and is not a prime.
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False

    # Loop through all the numbers from 2 to n.
    for i in range(2, n + 1):
        # If the number is prime, mark all its multiples as non-prime.
        if primes[i]:
            for j in range(i, n + 1, i):
                primes[j] = False
    # We have now marked all the non-primes,
    # so all that remains is to find the prime factors.
    factors = []
    for i in range(n, 1, -1):
        if primes[i]:
            factors.append(i)
    return