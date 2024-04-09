def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is
	Do not include these tokens in the code: " *** Y OUR CO DE H
	"""

    # Your code here
    p = 2
    while p * p < n:
        if n % p == 0:
            n //= p
        else:
            p += 1
    return n

if __name__ == "__main__":
    import doctest
    doctest.testmod()