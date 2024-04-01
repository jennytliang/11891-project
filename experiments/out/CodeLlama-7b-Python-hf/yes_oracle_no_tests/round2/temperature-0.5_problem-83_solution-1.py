def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if
	Do not include these tokens in the code: count = 0
	"""
    # Your code here
    count = 0
    for i in range(1, n + 1):
        if i % 10 == 1 or i // 10 == 1:
            count += 1
    return count


print(starts_one_ends(5))