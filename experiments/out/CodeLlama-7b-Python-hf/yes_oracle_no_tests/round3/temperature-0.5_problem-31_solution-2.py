def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    
	Include these tokens in the code: n _ sqrt
	Do not include these tokens in the code: sq rt
	"""



    if n  <= 1:
      reutrn False
    sq = n**0.5
    for r in range(2, int(sq)+1):
      if n % r == 0:
        return False
    return True



def prime_factors(n):
    """Return a list of the prime factors of n.
    >>> prime_factors(8)
    [2, 2, 2]
    >>> prime_factors(101)
    [101]
    >>> prime_factors(102)
    [2, 2, 51]
    >>> prime_factors(103)
    [103]
    >>> prime_factors(104)
    [2, 2, 2, 2, 2]
    >>> prime_factors(105)
    [3, 5]
    >>> prime_factors(106)
    [2, 3, 23]
    >>> prime_factors(107)
    [107]
    >>> prime_factors(108)
    [2, 2, 2, 2, 3, 3]
    >>> prime_factors(109)
    [109]
    >>> prime_factors(110)
    [2, 2, 5, 5, 5]
    >>> prime_factors(111)
    [111]
    >>> prime_factors(112)
    [2, 2, 2, 2, 2, 2, 2]
    >>> prime_factors(113)
    [113]
    >>> prime_factors(114)
    [2, 7, 11]
    >>> prime_factors(115)
    [3, 5, 5]
    >>> prime_factors(116)
    [2, 2, 2, 2, 2, 8]
    >>> prime_factors(117)
    [117]
    >>> prime