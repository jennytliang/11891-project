def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    
    # Base cases
    if n == 1:
        return 1
    elif n == 2:
        return 8
    
    # Recursive case
    return 9 * starts_one_ends(n-1)


print(starts_one_ends(1))
print(starts_one_ends(2))
print(starts_one_ends(3))

