def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: n = int ( n )
	"""
    # WRITE YOUR CODE HERE
    # count = 0
    # for i in range(1, 10**n):
    #     if i[0] == 1 or i[-1] == 1:
    #         count += 1
    # return count

    # return sum([k for k in range(1, 10 ** n) if str(k).startswith('1') or str(k).endswith('1')])

    return sum([k for k in range(1, 10 ** n) if k % 10 == 1 or k // 10**(n - 1) == 1])
