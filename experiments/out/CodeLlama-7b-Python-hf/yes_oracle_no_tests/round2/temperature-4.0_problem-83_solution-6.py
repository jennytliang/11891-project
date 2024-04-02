def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	Do not include these tokens in the code: # Start with
	"""
    if n == 1:
        return 0
    elif n == 2:
        return 10
    elif n == 3:
        return 20
    elif n == 4:
        return 30
    elif n == 5:
        return 40
    elif n == 6:
        return 50
    elif n == 7:
        return 60
    elif n == 8:
        return 70
    elif n == 9:
        return 80
    elif n == 10:
        return 90
    else:
        return 0


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
