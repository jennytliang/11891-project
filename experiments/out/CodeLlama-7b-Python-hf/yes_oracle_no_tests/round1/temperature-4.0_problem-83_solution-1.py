def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # Your code here
    # Base Case
    if n == 0:
        return 0
    # Recursive Case
    if n == 1:
        return 2
    else:
        return 2 * starts_one_ends(n - 1)


print(starts_one_ends(3))
print(starts_one_ends(1))
print(starts_one_ends(0))
