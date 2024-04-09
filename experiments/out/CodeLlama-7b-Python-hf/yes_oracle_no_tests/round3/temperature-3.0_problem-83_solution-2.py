def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # TODO : Write your assert
	"""
    # assert n >= 1, "n must be greater than or equal to 1"
    # assert n <= 9, "n must be less than or equal to 9"
    
    # base cases
    if n == 1:
        return 1
    if n == 2:
        return 8
    
    # recursive case
    return starts_one_ends(n-1) + starts_one_ends(n-2)

# test cases
print(starts_one_ends(1))
print(starts_one_ends(2))
print(starts_one_ends(3))
print(starts_one_ends(4))
print(starts_one_ends(5))
print(starts_one_ends(6))
print(starts_one_ends(7))
print(starts_one_ends(8))
print(starts_one_ends(9))
print(starts_one_ends(10))

# edge cases
print(starts_one_ends(0))
print(starts_one_ends(-1))
