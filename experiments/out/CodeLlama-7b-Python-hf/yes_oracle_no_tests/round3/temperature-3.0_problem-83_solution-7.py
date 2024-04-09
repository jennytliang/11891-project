def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    ones = 0
    for i in range(1, 10):
        for j in range(10 ** (n - 1)):
            ones += (i == 1 or i == 9) and (j == 0 or j == 9)
    return ones


def starts_one_ends_2(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    ones = 0
    for i in range(1, 10):
        ones += (i == 1 or i == 9) * (10 ** (n - 1) - 1)
    return ones
