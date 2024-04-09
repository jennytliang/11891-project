def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: first _ digit = 1
	"""
    if n == 1:
        return 1
    if n == 2:
        return 10
    return 10*(10**(n-2)) + 10 + 9*(10**(n-2))
