def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        return 4 * 10 ** (n - 2)