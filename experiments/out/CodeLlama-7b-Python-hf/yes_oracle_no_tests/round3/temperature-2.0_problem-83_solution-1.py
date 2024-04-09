def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: else :
	"""

    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return 3 * starts_one_ends(n - 1)
