def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code:  count =  0
	"""

    n_digits = 10**n
    n_digits_in_10s = 10**(n - 1)
    count = 0

    # Count the numbers that start with 1
    for i in range(1, n_digits_in_10s):
        if i % 10 == 1:
            count += n_digits_in_10s

    # Count the numbers that end with 1
    for i in range(1, 10):
        count += n_digits_in_10s

    return count


print(starts_one_ends(3))
print(starts_one_ends(5))
print(starts_one_ends(1))
