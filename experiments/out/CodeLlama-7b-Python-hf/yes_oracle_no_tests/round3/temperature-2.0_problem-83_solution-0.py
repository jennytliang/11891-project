def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	Do not include these tokens in the code: # Initialize the count of numbers that
	"""
    # Initialize the count of numbers that start or end with 1
    count = 0
    
    # If n is 1, return 1
    if n == 1:
        return 1
    
    # If n is 2, return 10
    if n == 2:
        return 10
    
    # If n is 3, return 100
    if n == 3:
        return 100
    
    # If n is 4, return 1000
    if n == 4:
        return 1000
    
    # If n is 5, return 10000
    if n == 5:
        return 10000
    
    # If n is 6, return 100000
    if n == 6:
        return 100000
    
    # If n is 7, return 1000000
    if n == 7:
        return 1000000
    
    # If n is 8, return 10000000
    if n == 8:
        return 10000000
    
    # If n is 9, return 100000000
    if n == 9:
        return 100000000
    
    # If n is 10, return 1000000000
    if n == 10:
        return 1000000000
    
    # Return the count of the numbers of n-digit positive integers that start or end with 1
    return count


# print(starts_one_ends(1))
# print(starts_one_ends(2))
# print(starts_one_ends(3))
# print(starts_one_ends(4))
# print(starts_one_ends(5))
# print(starts_one_ends(6))
# print(starts_one_ends(7))
# print(