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
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(1))
print(is_prime(2))
print(is_prime(101))
print(is_prime(51))
print(is_prime(11))
print(is_prime(13441))
print(is_prime(61))
print(is_prime(4))
print(is_prime(1))


