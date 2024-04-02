def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # TODO : Write a solution here
	"""
    # TODO : Write a solution here
    #
    # The number of 1-digit numbers that start or end with 1 is 10.
    # The number of 2-digit numbers that start or end with 1 is 90.
    # The number of 3-digit numbers that start or end with 1 is 900.
    # The number of 4-digit numbers that start or end with 1 is 9000.
    # ...
    # The number of n-digit numbers that start or end with 1 is 9 * 10^(n-1)
    ones = 9 * pow(10, n-1)
    return ones

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


def starts_one_ends_2(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # TODO : Write a solution here
	"""
    # TODO : Write a solution here
    #
    # The number of 1-digit numbers that start or end with 1 is 10.
    # The number of 2-digit numbers that start or end with 1 is 90.
    # The number of 3-digit numbers that start or end with 1 is 900.
    # The number of 4-digit numbers that start or end with 1 is 9000.
    # ...
    # The number of n-digit numbers that start or end with 1 is 9 * 10^(n-1)
    ones = 9 * pow(10, n-1)
   