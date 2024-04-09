def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	Do not include these tokens in the code: # start with
	"""
    # start with 1
    start_one = 9 * 10 ** (n - 1)
    # end with 1
    end_one = 10 ** n - 10 ** (n - 1)
    # total
    total = start_one + end_one
    return total


# print(starts_one_ends(1))
# print(starts_one_ends(2))
# print(starts_one_ends(3))
# print(starts_one_ends(4))

# 3rd option
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	Do not include these tokens in the code: # start with
	"""
    # start with 1
    start_one = 9 * 10 ** (n - 1)
    # end with 1
    end_one = 10 ** n - 10 ** (n - 1)
    # total
    total = start_one + end_one
    return total


# print(starts_one_ends(1))
# print(starts_one_ends(2))
# print(starts_one_ends(3))
# print(starts_one_ends(4))
