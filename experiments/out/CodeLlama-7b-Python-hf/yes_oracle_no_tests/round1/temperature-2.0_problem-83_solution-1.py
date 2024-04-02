def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	Do not include these tokens in the code: result = 0 for
	"""
    # YOUR CODE HERE
    result = 0
    for num in range(10**(n-1), 10**n):
        if num % 10 == 1 or num // 10**(n-1) == 1:
            result += 1
    return result


print(starts_one_ends(1))
print(starts_one_ends(2))
print(starts_one_ends(3))
print(starts_one_ends(4))
