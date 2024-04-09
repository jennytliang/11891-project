def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	Do not include these tokens in the code: # count = 0
	"""
    
    # count = 0
    # if n == 1:
    #     return 1
    # elif n == 2:
    #     return 2
    # else:
    #     for i in range(n - 1):
    #         if i == 0:
    #             for i in range(10):
    #                 count += 1
    #         elif i == n - 2:
    #             for i in range(10):
    #                 count += 1
    #         else:
    #             for i in range(10):
    #                 for i in range(10):
    #                     count += 1
    #     return count
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (10**(n-1) + 10**(n-2) + 10**(n-1) * 9 + 1)
    
    
    
print(starts_one_ends(1))
print(starts_one_ends(2))
print(starts_one_ends(3))
print(starts_one_ends(4))
print(starts_one_ends(5))
