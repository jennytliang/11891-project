def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # 1 digit numbers that start
	"""
    return 9 * (n - 1) ** 2


def starts_one_ends_two(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # 1 digit numbers that start
	"""
    return 9 ** (n - 1) * (10 - 9) ** (n - 1)


def starts_one_ends_three(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # 1 digit numbers that start
	"""
    return 9 ** (n - 1) * (10 - 9) ** (n - 1) + 10 ** (n - 1)


def starts_one_ends_four(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # 1 digit numbers that start
	"""
    return (10 - 9) ** (n - 1) * 10 ** (n - 1) * 2


def starts_one_ends_five(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # 1 digit numbers that start
	"""
    return (10 - 9) ** (n - 1) * 10 ** (n - 1) * 2 + 10 ** (n - 1)
