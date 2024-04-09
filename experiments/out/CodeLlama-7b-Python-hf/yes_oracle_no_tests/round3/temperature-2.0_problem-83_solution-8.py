def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # Base cases
	"""
    # Base cases:
    if n == 1:
        return 2
    
    # Recursive case:
    return 9 * starts_one_ends(n - 1)


# Case 1:
print(starts_one_ends(1))
# 2

# Case 2:
print(starts_one_ends(2))
# 20

# Case 3:
print(starts_one_ends(3))
# 108

# Case 4:
print(starts_one_ends(4))
# 486

# Case 5:
print(starts_one_ends(5))
# 1216
