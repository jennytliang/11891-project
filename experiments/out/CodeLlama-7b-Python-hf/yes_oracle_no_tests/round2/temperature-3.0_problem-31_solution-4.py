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
    
	Include these tokens in the code: False n _ sqrt = 1
	Do not include these tokens in the code: F als
	"""


    if n <= 1: 
        return False
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

def prime_list(n):
    """
    >>> prime_list(10)
    [2, 3, 5, 7]
    >>> prime_list(15)
    [2, 3, 5, 7, 11, 13]
    >>> prime_list(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> prime_list(1)
    []
    >>> prime_list(0)
    []
    """

    num_list = []
    for x in range(2, n):
        if is_prime(x):
            num_list.append(x)
    return num_list



























































































































































































































































































