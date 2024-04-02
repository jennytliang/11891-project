def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: result = 0 for
	"""
    result = 0
    # Write your code here
    for i in range(1, n):
        result += 2 * (10 ** i - 1)
    return result
