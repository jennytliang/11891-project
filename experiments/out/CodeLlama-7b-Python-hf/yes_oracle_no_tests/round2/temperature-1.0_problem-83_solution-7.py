def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    n1 = 0
    n2 = 0
    for i in range(10**(n - 1), 10**n):
        if str(i)[:1] == '1' or str(i)[-1:] == '1':
            n1 += 1
        else:
            n2 += 1
    return n1 + n2


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
# print(starts_one_ends(11))
# print(starts_one_ends(12))
# print(starts_one_ends(13))
# print(starts_one_ends(14))
# print(starts_one_ends(15))
# print(starts_one_ends(16))
# print(starts_one_ends(17))
# print(starts_one_ends(18))
# print(starts_one_ends(19))
