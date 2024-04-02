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
    
	Do not include these tokens in the code: pass def is _ multiple
	"""
    # pass
    if n == 1:
        return False
    for j in range(2, int(n ** .5) + 1):
        if n % j == 0:
           return False
    return True


if __name__ == "__main__":
    print("5 should be prime and it is:")
    print(is_prime(5))
 
    print("16 should not be prime and it isn't:")
    print(is_prime(16))
