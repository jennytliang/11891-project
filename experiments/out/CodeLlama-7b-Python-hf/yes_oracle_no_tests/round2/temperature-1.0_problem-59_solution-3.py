def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    max_prime_factor = n
    i = 2
    while i * i <= n:
        if n//i == 0:
            i += 1
        while n//i > 1:
            if n % i == 0:
                max_prime_factor = i
                break 
            i += 1
    return max_prime_factor
