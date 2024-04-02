def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    return 0

print(starts_one_ends(1))
print(starts_one_ends(2))
print(starts_one_ends(3))
print(starts_one_ends(4))
print(starts_one_ends(5))


# 0
# 2
# 5
# 8
# 12

# Rules:
# - if n == 1: return 0
# - if n == 2: return 10
# - if n == 3: return 91
# - if n == 4: return 901
# - if n == 5: return 9001
# - if n == 6: return 90001
# - if n == 7: return 900001
# - if n == 8: return 9000001
# - if n == 9: return 90000001
# - if n == 10: return 900000001
