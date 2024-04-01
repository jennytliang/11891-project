def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for d in range(1, n + 1):
        start = int('1' + '0' * (d - 1))
        end = int('1' + '0' * (d - 2))
        count += start + end + 2
    return count        