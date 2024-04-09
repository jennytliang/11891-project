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
	Do not include these tokens in the code: else : sq rt
	"""



    if n <= 1: 
         return False
    for sq in range(2, int(n**0.5)+1):
        if n % sq == 0:
            return False
    return True



def prime_factors(n):
    """Return a list of the prime factors of n.
    >>> prime_factors(8)
    [2, 2, 2]
    >>> prime_factors(101)
    [101]
    >>> prime_factors(27)
    [3, 3, 3]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(25)
    [5, 5]
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(101)
    [101]
    >>> prime_factors(111)
    [111]
    >>> prime_factors(151)
    [151]
    >>> prime_factors(121)
    [11, 11]
    >>> prime_factors(19)
    [19]
    >>> prime_factors(102)
    [2, 2, 5, 5, 11]
    >>> prime_factors(1001)
    [7, 11, 13, 19, 31, 37, 71, 73, 79, 97]
    >>> prime_factors(1000)
    [2, 2, 2, 5, 5, 5, 5, 5, 7, 11, 13, 17, 19, 31, 37, 71, 73, 79, 97]
    >>> prime_factors(1011)
    [1011]
    >>> prime_factors(1012)
    [2, 2, 2,