def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    return int(round((n / 2) - 1)) if n % 4 else int(round(n / 2))


