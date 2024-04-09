def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # Make sure n is an int
    n = int(n)

    # Make sure n is greater than 1
    if n < 2:
        return None

    # Make sure n is not a prime
    if n in [2, 3, 5, 7]:
        return n

    # If we have not found a prime factor yet,
    # then the largest prime factor is n itself.
    largest_prime_factor = n

    # We will divide n by primes, starting at 2.
    # If n is prime, we will return n.
    divisor = 2

    # Loop while n is greater than 1.
    while n > 1:
        # If n is evenly divisible by divisor,
        # then n is not prime and we divide n by the divisor.
        # Otherwise the divisor is prime and we increase the divisor by 1.
        if n % divisor == 0:
            n = n / divisor
        else:
            divisor += 1

        # If the divisor is greater than the largest prime factor,
        # then the divisor is the largest prime factor.
        if divisor > largest_prime_factor:
            largest_prime_factor = divisor

    # Return the largest prime factor
    return int(largest_prime_factor)
