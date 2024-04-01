def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Base case
    if n == 1:
        return 1
    for i in reversed(range(2, n // 2 + 1)):
        # print("Largest_divisor: i {}, n {}".format(i, n))
        if n % i == 0:
            return i
    if n == 1:
        return 1
