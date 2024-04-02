def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # Initialize count
    count = 0
    # If n is 1, return 0
    if n == 1:
        return 0
    # Otherwise, for loop over 10 to the power n
    for i in range(10**(n-1), 10**n):
        # If the last digit is 1, add to count
        if i % 10 == 1:
            count += 1
        # If the first digit is 1, add to count
        if i // 10**(n-1) == 1:
            count += 1
    # Return count
    return count
    
# Check with input n = 1
print(starts_one_ends(1))
# Check with input n = 2
print(starts_one_ends(2))
# Check with input n = 3
print(starts_one_ends(3))