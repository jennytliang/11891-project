def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    one_end_digits = set(str((i * 10 ** (n-1)) + ((i + 1) * 10 ** (n-1))))
    count = 0
    for i in range(10 ** n):
        if str(i).startswith('1') or str(i).endswith('1'):
            count += 1
        if i in one_end_digits:
            count += 1
    return count