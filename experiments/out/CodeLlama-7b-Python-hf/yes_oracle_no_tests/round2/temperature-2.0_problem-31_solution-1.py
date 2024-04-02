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

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


    # if n <= 1:
    #     return False
    # if n == 2 or n == 3:
    #     return True
    # if n % 2 == 0 or n % 3 == 0:
    #     return False
    # i = 5
    # while i ** 2 <= n:
    #     if n % i == 0 or n % (i + 2) == 0:
    #         return False
    #     i += 6
    # return True




def prime_factors(n):
    """Return a list of the prime factors of n, in ascending order.
    >>> prime_factors(8)
    [2, 2, 2]
    >>> prime_factors(101)
    [101]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(97)
    [97]
    >>> prime_factors(12345)
    [2, 3, 5, 7]
    >>> prime_factors(639957)
    [3, 199, 1093]
    >>> prime_factors(10000000)
    [2, 5, 7, 11, 13, 23, 29, 31, 37, 41]
    >>> prime_factors(1234567890)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 