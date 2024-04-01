def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Do not include these tokens in the code:  " *** Y OUR CO DE H ERE ***
	"""

    # Your code here
    if n <= 0:
        return None
    if n <= 2:
        return n
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n


if __name__ == "__main__":
    import doctest

    doctest.testmod()
