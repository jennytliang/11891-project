def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # your code here count
	"""
    # count the number of n-digit positive integers that start or end with 1
    # return count
    count = 0
    for i in range(10**(n-1), 10**n):
        if str(i).startswith('1') or str(i).endswith('1'):
            count += 1
    return count