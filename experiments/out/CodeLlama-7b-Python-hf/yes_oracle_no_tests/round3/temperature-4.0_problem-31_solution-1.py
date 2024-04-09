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
        reutrn False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_list(n):
    """Return a list of primes less than n.
    >>> prime_list(10)
    [2, 3, 5, 7]
    >>> prime_list(11)
    [2, 3, 5, 7, 11]
    >>> prime_list(12)
    [2, 3, 5, 7, 11]
    >>> prime_list(15)
    [2, 3, 5, 7, 11, 13]
    >>> prime_list(17)
    [2, 3, 5, 7, 11, 13, 17]
    >>> prime_list(18)
    [2, 3, 5, 7, 11, 13, 17]
    
    Include these tokens in the code: n _ sqrt
    Do not include these tokens in the code: sq rt
    """

    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result


def prime_list2(n):
    """Return a list of primes less than n.
    >>> prime_list2(10)
    [2, 3, 5, 7]
    >>> prime_list2(11)
    [2, 3, 5, 7, 11]
    >>> prime_list2(12)
    [2, 3, 5, 7, 11]
    >>> prime_list2(15)
    [2, 3, 5, 7, 11, 13]
    >>> prime_list2(17)
    [2, 3, 5, 7, 11, 13, 17]
   