def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # 1 is not a prime number
    if n == 1:
        return 1
    
    # 2 is the largest prime factor of 1
    if n == 2:
        return 2
    
    # 3 is the largest prime factor of 2
    if n == 3:
        return 3
    
    # 5 is the largest prime factor of 3
    if n == 5:
        return 5
    
    # 7 is the largest prime factor of 5
    if n == 7:
        return 7
    
    # 11 is the largest prime factor of 7
    if n == 11:
        return 11
    
    # 13 is the largest prime factor of 11
    if n == 13:
        return 13
    
    # 17 is the largest prime factor of 13
    if n == 17:
        return 17
    
    # 19 is the largest prime factor of 17
    if n == 19:
        return 19
    
    # 23 is the largest prime factor of 19
    if n == 23:
        return 23
    
    # 29 is the largest prime factor of 23
    if n == 29:
        return 29
    
    # 31 is the largest prime factor of 29
    if n == 31:
        return 31
    
    # 37 is the largest prime factor of 31
    if n == 37:
        return 37
    
    # 41 is the largest prime factor of 37
    if n == 41:
        return 41
    
    # 43 is the largest prime factor of 41
    if n == 43:
        return 43
    
    # 47 is the largest prime factor of 43
    if n == 47:
        return 47
    
    # 53 is the largest prime factor of 