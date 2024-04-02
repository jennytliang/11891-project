def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if
	Do not include these tokens in the code: count = 0 for
	"""
    n = int(n)
    if n <= 0:
        return 0
    else:
        # count = 0
        # for i in range(10**(n-1), 10**n):
        #     if i[0] == 1 or i[-1] == 1:
        #         count += 1
        # return count
        return sum([1 for i in range(10**(n-1), 10**n) if i[0] == 1 or i[-1] == 1])
