def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # YOUR CODE HERE
    ones_start = 10
    ones_end = 10
    if n > 1:
        ones_start = 9
        ones_end = 1
    return ones_start + ones_end


print(starts_one_ends(1))
print(starts_one_ends(2))
print(starts_one_ends(3))
