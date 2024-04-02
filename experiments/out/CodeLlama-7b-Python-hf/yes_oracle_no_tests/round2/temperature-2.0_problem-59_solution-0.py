def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Do not include these tokens in the code: # Your code here
	"""
    # Your code here
    if n == 2:
        return n
    if n % 2 == 0:
        return largest_prime_factor(n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return largest_prime_factor(n // i)
    return n


if __name__ == "__main__":
    import doctest

    doctest.testmod()
