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


    if n <= 1:
        
 
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        sq = n ** 0.5
        sq = int(sq)
        for r in range(3, sq + 1, 2):
            if n % r == 0:
                return False
        return True








def prime_factors(n):
    """Return a list of the prime factors of a number.
    >>> prime_factors(8)
    [2, 2, 2]
    >>> prime_factors(20)
    [2, 5]
    >>> prime_factors(11)
    [11]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(90)
    [2, 3, 5]
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(101)
    [101]
    >>> prime_factors(123456)
    [2, 3, 5, 7, 11, 13]
    >>> prime_factors(999)
    [3, 3, 3, 3, 3, 3, 3]
    >>> a = prime_factors(123456)
    >>> a
    [2, 3, 5, 7, 11, 13]
    >>> a == prime_factors(123456)
    True
    """

    factors = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                factors.append(i)
                n = n / i
                break
    return factors





def first_n_prime_factors(n):
    """Return a list of the first n prime factors of a number.
    >>>