def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	Do not include these tokens in the code: result = 0 for
	"""
    result = 0
    for i in range(1,10**n):
        if str(i)[:1] == "1" or str(i)[-1] == "1":
            result += 1
    return result
