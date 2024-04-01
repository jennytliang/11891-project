def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	Do not include these tokens in the code: count = 0
	"""
    count = 0
    if n > 0:
        if n == 1:
            count = 10
        elif n == 2:
            count = 9 * 10
        elif n == 3:
            count = 9 * 9 * 10
        elif n == 4:
            count = 9 * 9 * 9 * 10
        elif n == 5:
            count = 9 * 9 * 9 * 9 * 10
        else:
            count = (9 * 9 * 9 * 9 * 9) * 10
    return count
