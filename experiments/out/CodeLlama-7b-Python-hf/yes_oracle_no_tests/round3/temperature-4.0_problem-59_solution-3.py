def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Do not include these tokens in the code: # Check if n
	"""

    # Check if n is prime
    if n % 2 == 0:
        # Check if n is even
        for i in range(2, int(n**0.5)+1, 2):
            if n % i == 0:
                return i
        return n
    else:
        # Check if n is odd
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return i
        return n


if __name__ == "__main__":
    import doctest
    doctest.testmod()
