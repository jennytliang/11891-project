def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # Your code here result
	"""

    # Your code here
    num_ones = 0
    for i in range(10**(n-1), 10**n):
        if i % 10 == 1 or i // 10**(n-1) == 1:
            num_ones += 1
    return num_ones


# print(starts_one_ends(3))
print(starts_one_ends(10))
