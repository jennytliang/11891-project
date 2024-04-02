def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    if n == 1:
        return 1
    if n % 2 == 0:
        for i in range(3, n + 1, 2):
            if i >= n:
                return n
            if i**2 > n:
                return n % i
            i += 2
    else:
        i = 3
        while i <= n:
            if n % i == 0:
                break
            i += 2
        else:
            return n
        for i in range(i, n + 1, 2 * i):
            if i >= n:
                return n
            if i**2 > n:
                return n % i
            i += 2
        return n % i
