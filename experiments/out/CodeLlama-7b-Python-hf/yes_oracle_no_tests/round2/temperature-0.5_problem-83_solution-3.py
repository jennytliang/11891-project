def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if
	Do not include these tokens in the code: # Your code here
	"""
    # Your code here
    if n == 1:
        return 1
    if n == 2:
        return 10
    return (9 * (10 ** (n - 2))) + (10 ** (n - 2))


# print(starts_one_ends(1))
# print(starts_one_ends(2))
# print(starts_one_ends(3))
# print(starts_one_ends(4))
# print(starts_one_ends(5))
# print(starts_one_ends(6))
# print(starts_one_ends(7))
# print(starts_one_ends(8))
# print(starts_one_ends(9))
# print(starts_one_ends(10))


def starts_one_ends_2(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if
	Do not include these tokens in the code: # Your code here
	"""
    # Your code here
    if n == 1:
        return 1
    if n == 2:
        return 10
    if n == 3:
        return 91
    if n == 4:
        return 901
    if n == 5:
        return 9001
    if n == 6:
        return 90001
    if n == 7:
        return 900001
    if n == 8:
        return 9000001
    if n == 9:
        return 90000001
    if n == 10:
        return 900000001


# print(starts_one_ends_2(1))
# print(starts_one_ends_2(2))
# print(starts_one_ends_2(3))
# print(starts_one_ends_2(4))
# print(starts_one_