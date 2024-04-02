def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    starts_one = 0
    ends_one = 0
    if n == 1:
        return 1
    for i in range(10**(n-1), 10**n):
        if i % 10 == 1:
            starts_one += 1
        if i % 10 == 9:
            ends_one += 1
    return starts_one + ends_one
