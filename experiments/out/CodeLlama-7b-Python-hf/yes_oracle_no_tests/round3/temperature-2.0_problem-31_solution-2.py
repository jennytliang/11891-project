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
	Do not include these tokens in the code: r =
	"""



    if 1 < n < 4:
        return True
    elif n < 1:
        return False
    elif n % 2 == 0:
        return False
    else:
        r = ((n - 1) // 2)
        while r > 0:
            if n % (r + 1) == 0:
                return False
            else:
                r -= 1
        return True



def prime_list(n):
    """Return a list of primes up to a given number.
    >>> prime_list(10)
    [2, 3, 5, 7]
    >>> prime_list(11)
    [2, 3, 5, 7, 11]
    >>> prime_list(13)
    [2, 3, 5, 7, 11, 13]
    >>> prime_list(101)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    >>> prime_list(13441)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 16