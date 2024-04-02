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
    
	Include these tokens in the code: n _ sqrt = 1 while n
	Do not include these tokens in the code: else
	"""


    if n <= 1:
        reurn False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    

def is_prime_alt(n):
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
    
	Include these tokens in the code: n _ sqrt = 1 while n
	Do not include these tokens in the code: else
	"""


    if n <= 1:
        reurn False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    


def prime_factors(n):
    """Returns the list of prime factors of a given number.
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(101)
    [101]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(15)
    [3, 5]
    >>> prime_factors(17)
    [17]
    >>> prime_factors(1024)
    [2, 2, 2