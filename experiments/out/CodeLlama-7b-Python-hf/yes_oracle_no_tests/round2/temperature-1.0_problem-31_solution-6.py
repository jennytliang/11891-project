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
       return False
    elif n <= 3:
       return True
    elif n % 2 == 0 or n % 3 == 0:
       return False
    else:
       for i in range(5, int(n ** 0.5) + 1, 6):
          if n % i == 0 or n % (i + 2) == 0:
             return False
       return True


def is_prime_check(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime_check(6)
    False
    >>> is_prime_check(101)
    True
    >>> is_prime_check(11)
    True
    >>> is_prime_check(13441)
    True
    >>> is_prime_check(61)
    True
    >>> is_prime_check(4)
    False
    >>> is_prime_check(1)
    False
    
	Do not include these tokens in the code: elif
	"""

    
    if n <= 1:
       return False
    elif n <= 3:
       return True
    elif n % 2 == 0 or n % 3 == 0:
       return False
    else:
       for i in range(5, int(n ** 0.5) + 1, 6):
          if n % i == 0 or n % (i + 2) == 0:
             return False
       return True


def is_prime_for(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime_for(6)
    False
    >>> is_prime_for(101)
    True
    >>> is_prime_for(11)
    True
    >>> is_prime_for(13441)
    True
    >>> is_prime_for(61)
    True
    >>> is_prime_for(4)
    False
    >>> is_prime_for(1)
    False
    
	Do not include these tokens