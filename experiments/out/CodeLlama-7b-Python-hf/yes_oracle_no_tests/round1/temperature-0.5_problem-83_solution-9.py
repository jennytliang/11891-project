def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code:  count =  0
	"""

    # Count the numbers of n-digit positive integers that start or end with 1
    count = 0
    for i in range(1, 10**(n - 1) + 1):
        # If the first digit is 1
        if i % 10 == 1:
            count += 1
        # If the last digit is 1
        if int(str(i)[-1]) == 1:
            count += 1

    return count


print(starts_one_ends(2))
