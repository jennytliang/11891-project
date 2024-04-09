def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Do not include these tokens in the code: #
	"""
    # Your code here
    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, n // 2 + 1, 2):
            if n % i == 0:
                return False
        return True

    for i in range(2, n // 2 + 1):
        if n % i == 0 and is_prime(i):
            return i
    return n


if __name__ == "__main__":
    import doctest

    doctest.testmod()
