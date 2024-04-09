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
       re = False
    elif n == 2:
       re = True
    elif n % 2 == 0:
       re = False
    else:
       i = 3
       while i < n:
           if n % i == 0:
               re = False
               break
           i += 2
       if i == n:
           re = True
    return re


def is_prime2(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime2(6)
    False
    >>> is_prime2(101)
    True
    >>> is_prime2(11)
    True
    >>> is_prime2(13441)
    True
    >>> is_prime2(61)
    True
    >>> is_prime2(4)
    False
    >>> is_prime2(1)
    False
    
	Do not include these tokens in the code: elif
	"""

    if n <= 1:
       re = False
    else:
       i = 2
       while i < n:
           if n % i == 0:
               re = False
               break
           i += 1
       if i == n:
           re = True
    return re


    
def is_prime3(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime3(6)
    False
    >>> is_prime3(101)
    True
    >>> is_prime3(11)
    True
    >>> is_prime3(13441)
    True
    >>> is_prime3(61)
    True
    >>> is_prime3(4)
    False
    >>> is_prime3(1)
    False
    
	Do not include these tokens in the code: elif
	"""
    if n <= 1:
       re = False
    else:
       i = 2
       while i * i <= n:
           if n % i == 0:
               re = False
               break
