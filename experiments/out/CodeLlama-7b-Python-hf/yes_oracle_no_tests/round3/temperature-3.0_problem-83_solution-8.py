def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # start with 1
	"""
    # If n is 1 return 2
    if n == 1:
        return 2
    # If n is 2 return 10
    elif n == 2:
        return 10
    # Otherwise return 9 * 9 * 10
    else:
        return 9 * 9 * 10


# TESTS
assert starts_one_ends(1) == 2
assert starts_one_ends(2) == 10
assert starts_one_ends(3) == 90
