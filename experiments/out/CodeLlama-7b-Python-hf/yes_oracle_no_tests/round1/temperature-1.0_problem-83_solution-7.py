def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: count = 0 for
	"""
    # set variables
    counter = 0
    for i in range (1,n):
        # count numbers starting with 1
        counter += i
        # count numbers ending with 1
        counter += 9 * i
    return counter
