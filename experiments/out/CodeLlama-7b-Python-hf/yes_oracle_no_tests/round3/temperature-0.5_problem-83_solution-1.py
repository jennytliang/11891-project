def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if
	Do not include these tokens in the code: # Your code here count
	"""
    # Your code here
    s = str(n)
    if s[0] == '1':
        if s[-1] == '1':
            return n
        else:
            return n-1
    else:
        if s[-1] == '1':
            return n-1
        else:
            return n-2


print(starts_one_ends(100))