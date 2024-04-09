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
    
	Include these tokens in the code: return
	Do not include these tokens in the code: re =
	"""



    if 0 or 1 or -1 or 2 or -2 or 3 or -3 or 4 or -4 or 5 or -5 or 6 or -6 or 7 or -7 or 8 or -8 or 9 or -9:
        return False
    else:
        return True




def prime_factors(n):
    """Return a list of the prime factors of a given number.
    >>> prime_factors(1)
    []
    >>> prime_factors(2)
    [2]
    >>> prime_factors(3)
    [3]
    >>> prime_factors(4)
    [2, 2]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(26)
    [2, 13]
    >>> prime_factors(97)
    [97]
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(7 ** 10) # 7^10 is 1048576
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
    
    """
    factors = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                factors.append(i)
                break
    return factors




def longest_prime_factor_chain(n):
    """Return the number whose prime factors have the longest chain of prime factors.
    >>> longest_prime_factor_chain(10)
    9
    >>> longest_prime_factor_chain(17)
    17
    >>> longest_prime_factor_chain(101)
    101
    >>> longest_prime_factor_chain(201)
    101
    >>> longest_prime_factor_chain(2001)
    201
    >>> longest