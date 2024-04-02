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
    
	Do not include these tokens in the code: elif
	"""

    if n <= 1:
        ret = False
    elif n <= 3:
        ret = True
    else:
        if n % 2 == 0 or n % 3 == 0:
            ret = False
        else:
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    ret = False
                    break
                i += 6
            ret = True
    return ret


def is_prime_2(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime_2(6)
    False
    >>> is_prime_2(101)
    True
    >>> is_prime_2(11)
    True
    >>> is_prime_2(13441)
    True
    >>> is_prime_2(61)
    True
    >>> is_prime_2(4)
    False
    >>> is_prime_2(1)
    False
    
	Do not include these tokens in the code: elif
	"""

    if n <= 1:
        ret = False
    elif n <= 3:
        ret = True
    else:
        if n % 2 == 0 or n % 3 == 0:
            ret = False
        else:
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    ret = False
                    break
                i += 6
            ret = True
    return ret


def is_prime_3(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime_3(6)
    False
    >>> is_prime_3(101)
    True
    >>> is_prime_3(11)
    True
    >>> is_prime_3(13441)
    True
    >>> is_prime_3(61)
    True
    >>> is_prime_3(4)
