def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # TODO: Write a solution here
    # base cases
    if n == 1:
        return 1
    elif n == 2:
        return 8
    else:
        return 9 * 10**(n - 2) + 9
    


print(starts_one_ends(1))
print(starts_one_ends(2))
print(starts_one_ends(3))
print(starts_one_ends(4))
print(starts_one_ends(5))
print(starts_one_ends(6))
print(starts_one_ends(7))