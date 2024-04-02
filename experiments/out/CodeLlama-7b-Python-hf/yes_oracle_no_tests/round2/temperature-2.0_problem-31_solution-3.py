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
    
	Include these tokens in the code: n _ sqrt = 1
	"""


    if n <= 1:
       return False
    elif n <= 3:
       return True
    elif n % 2 == 0 or n % 3 == 0:
       return False
    sqrt = int(n**0.5) + 1
    for i in range(5, sqrt, 6):
       if n % i == 0 or n % (i + 2) == 0:
          return False
    return True
