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
    
	Include these tokens in the code: n _ sqrt
	Do not include these tokens in the code: sq rt
	"""


    if n <= 1:
        reurn False
    for i in range(2,int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True


# 10 points
def factors(n):
    """Return a list of the factors of a given number.
    >>> factors(20)
    [1, 2, 4, 5, 10, 20]
    >>> factors(25)
    [1, 5, 25]
    >>> factors(24)
    [1, 2, 3, 4, 6, 8, 12, 24]
    >>> factors(210)
    [1, 2, 3, 5, 6, 10, 15, 30, 35, 75, 105, 210]
    >>> factors(210)
    [1, 2, 3, 5, 6, 10, 15, 30, 35, 75, 105, 210]
    >>> factors(5040)
    [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 32, 48, 72, 144, 288, 576, 1152, 2304, 4608, 5040]
    >>> factors(2000)
    [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 200, 250, 500, 1000, 2000]
    
	Include these tokens in the code: n _ sqrt
	Do not include these tokens in the code: sq rt
	"""


    factor_list = []
    for i in range(1, int(n+