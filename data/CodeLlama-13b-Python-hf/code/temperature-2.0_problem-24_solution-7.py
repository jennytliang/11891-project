def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisor = n // 2
    while divisor > 0:
        if n % divisor == 0:
            return divisor
        divisor -= 1
    return 1
