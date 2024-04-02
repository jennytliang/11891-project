def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: if n == 1 :
	"""
    totalCount = 0
    
    for i in range(n):
        if (i == 0 or i == n-1): 
            totalCount += 2
        else: 
            totalCount += 1
    
    return totalCount
