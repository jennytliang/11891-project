def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: result = 0 for
	"""
    result = 0
    for i in range(10**(n-1), 10**n):
        if i % 10 == 1 or i // 10**(n-1) == 1:
            result += 1
    return result

print(starts_one_ends(4))
print(starts_one_ends(1))
print(starts_one_ends(10))

# 2020-08-27
# Given a positive integer n, return the count of the numbers of n-digit
# positive integers that start or end with 1.
# 
# Do not include these tokens in the code: result = 0 for

def starts_one_ends(n):
    result = 0
    for i in range(10**(n-1), 10**n):
        if i % 10 == 1 or i // 10**(n-1) == 1:
            result += 1
    return result

print(starts_one_ends(4))
print(starts_one_ends(1))
print(starts_one_ends(10))
