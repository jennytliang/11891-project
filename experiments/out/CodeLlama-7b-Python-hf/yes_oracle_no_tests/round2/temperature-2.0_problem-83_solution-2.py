def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # Your code here result
	"""
    # Your code here
    result = 0
    for i in range(10**(n-1), 10**n):
        if i[0] == 1 or i[-1] == 1:
            result += 1
    return result


# TESTS
assert starts_one_ends(3) == 16
