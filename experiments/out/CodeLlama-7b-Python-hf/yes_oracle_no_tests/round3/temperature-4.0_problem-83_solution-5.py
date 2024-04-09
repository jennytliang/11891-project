def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 2
	"""


    if n == 1:
 	    return 9

    return 9 * 10 ** (n - 2)


def starts_two_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 2.
    
	Include these tokens in the code: 2
	Do not include these tokens in the code: 1
	"""


    if n == 1:
 	    return 8

    return 9 * 10 ** (n - 2)


def starts_one_ends_not_two(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1 but do not end with 2.
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 2
	"""


    if n == 1:
 	    return 8

    return 9 * 10 ** (n - 2) - 10 * 9 * 10 ** (n - 3)


def starts_two_ends_not_one(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 2 but do not end with 1.
    
	Include these tokens in the code: 2
	Do not include these tokens in the code: 1
	"""


    if n == 1:
 	    return 7

    return 9 * 10 ** (n - 2) - 9 * 10 ** (n - 3)


def starts_one_ends_not_two_not_three(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1 but do not end with 2 or 3.
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 2, 3
	"""
