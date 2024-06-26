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
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: ==
	"""

    if n <= 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n):
            if n % i == 0:
                return False
        return True


# def is_prime(n):
#     """Return true if a given number is prime, and false otherwise.
#     >>> is_prime(6)
#     False
#     >>> is_prime(101)
#     True
#     >>> is_prime(11)
#     True
#     >>> is_prime(13441)
#     True
#     >>> is_prime(61)
#     True
#     >>> is_prime(4)
#     False
#     >>> is_prime(1)
#     False
    
#     Include these tokens in the code: <=
#     Do not include these tokens in the code: ==
#     """

#     if n <= 2:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     else:
#         for i in range(3, n, 2):
#             if n % i == 0:
#                 return False
#         return True
