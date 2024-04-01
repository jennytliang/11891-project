def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Do not include these tokens in the code:  " *** Y OUR CO DE H ERE ***
	"""

    factor = 2
    while n > 1:
        if n % factor == 0:
            n = n / factor
            while n % factor == 0:
                n = n / factor
            factor = factor + 1
        else:
            factor = factor + 1
    return factor - 1
