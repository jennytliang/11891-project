def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # Your code here
    # This is a very inefficient solution
    count = 0
    for i in range(10 ** (n - 1) + 1, 10 ** n):
        if i % 10 == 1 or i // 10 ** (n - 1) == 1:
            count += 1
    return count


assert starts_one_ends(1) == 8
assert starts_one_ends(2) == 24
assert starts_one_ends(3) == 40


def starts_one_ends2(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # Your code here
    # This is a more efficient solution
    count = 0
    for i in range(10 ** (n - 1) + 1, 10 ** n):
        if i % 10 == 1 or i // 10 ** (n - 1) == 1:
            count += 1
    return count


assert starts_one_ends2(1) == 8
assert starts_one_ends2(2) == 24
assert starts_one_ends2(3) == 40
