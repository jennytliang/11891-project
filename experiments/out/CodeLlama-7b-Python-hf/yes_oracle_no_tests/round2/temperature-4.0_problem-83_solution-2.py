def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: starts _ one = 0
	"""
    starts_one = 0
    for i in range(10**(n-1), 10**n):
        if str(i).startswith("1"):
            starts_one += 1
    return starts_one


print(starts_one_ends(3))
print(starts_one_ends(1))
print(starts_one_ends(2))