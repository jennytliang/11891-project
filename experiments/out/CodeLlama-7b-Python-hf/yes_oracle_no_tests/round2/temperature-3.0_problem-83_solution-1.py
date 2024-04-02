def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # start with 1 and end with 1
    # start with 1 and end with 2
    # start with 1 and end with 3
    # start with 1 and end with 4
    # start with 1 and end with 5
    # start with 1 and end with 6
    # start with 1 and end with 7
    # start with 1 and end with 8
    # start with 1 and end with 9
    # start with 1 and end with 0
    # start with 2 and end with 1
    # start with 3 and end with 1
    # start with 4 and end with 1
    # start with 5 and end with 1
    # start with 6 and end with 1
    # start with 7 and end with 1
    # start with 8 and end with 1
    # start with 9 and end with 1
    # start with 0 and end with 1
    
    count = 0
    for i in range(1, n + 1):
        count += (i * 10)
    return count
