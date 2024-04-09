def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	Do not include these tokens in the code: starts _ one = 0
	"""
    # Your code here
    if 1 <= n <= 10:
        return 1
    return (10**(n-1))*2































































