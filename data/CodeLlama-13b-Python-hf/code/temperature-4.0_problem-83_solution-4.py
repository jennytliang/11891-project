def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if isinstance(n, int):
        raise TypeError
    if n < 1:
        raise ZeroDivisionError
    return 45**n