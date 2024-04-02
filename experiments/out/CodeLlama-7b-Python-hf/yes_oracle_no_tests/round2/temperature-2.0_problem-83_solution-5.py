def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # initialize count
    count = 0
    
    # iterate through 10 to n-1
    for i in range(1, n):
        
        # get all possible permutations of i-digit numbers
        # and count the ones that start or end with 1
        count += len([j for j in range(10**(i-1), 10**i) if j % 10 == 1 or j // 10**(i-1) == 1])
        
    return count


# test
print(starts_one_ends(5))
