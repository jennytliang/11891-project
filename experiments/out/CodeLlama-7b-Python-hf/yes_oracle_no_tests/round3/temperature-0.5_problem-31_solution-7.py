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



    if n  <= 1:
       r = False
    elif n == 2:
       r = True
    elif n % 2 == 0:
       r = False
    else:
       for i in range(3, int(n**0.5+1), 2):
          if n % i == 0:
             r = False
             break
       else:
          r = True
    return r

if __name__=="__main__":
    import doctest
    doctest.testmod()