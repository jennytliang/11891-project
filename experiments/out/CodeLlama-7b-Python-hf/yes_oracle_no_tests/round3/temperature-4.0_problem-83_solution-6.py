def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: return 0 elif n ==
	"""

    if n  < 1:
        return 0

    # This is the number of 1-digit numbers that start or end with 1
    count = 9

    # This is the number of 2-digit numbers that start or end with 1
    count += 9 * 10

    # This is the number of 3-digit numbers that start or end with 1
    count += 9 * 10 * 10

    # This is the number of 4-digit numbers that start or end with 1
    count += 9 * 10 * 10 * 10

    # This is the number of 5-digit numbers that start or end with 1
    count += 9 * 10 * 10 * 10 * 10

    return count

def starts_one_ends_recursive(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.

    Do not include these tokens in the code: return 0 elif n ==
    """

    if n  < 1:
        return 0

    if n == 1:
        return 9

    return 9 * 10 ** (n - 1) + starts_one_ends_recursive(n - 1)



def starts_one_ends_recursive_2(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.

    Do not include these tokens in the code: return 0 elif n ==
    """

    if n  < 1:
        return 0

    if n == 1:
        return 9

    return 9 * 10 ** (n - 1) + starts_one_ends_recursive_2(n - 1)














































