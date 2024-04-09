def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # Initialize the list of prime factors.
    prime_factors = [True] * (n + 1)
    # Set the first and second prime factors.
    prime_factors[0] = prime_factors[1] = False
    # Start with the smallest prime number.
    current_prime = 2
    # Keep going until we find a prime factor.
    while n > 1:
        # If the number is divisible by the current prime, it is not a prime.
        if n % current_prime == 0:
            # Set the corresponding element of the list to false.
            prime_factors[current_prime] = False
            # Divide the number by the current prime.
            n = n // current_prime
        # If the number is not divisible by the current prime, increment the
        # current prime by 1.
        else:
            current_prime += 1
    # Return the last prime.
    return current_prime - 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(largest_prime_factor(13195))
    print(largest_prime_factor(2048))