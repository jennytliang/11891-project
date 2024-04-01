def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest_dividend = 1
    n_copy = n

    while n_copy:
        if n % 2 == 0:
            largest_dividend = 2
            n /= largest_dividend
        else:

            if 2 * n < n_copy:
                return largest_dividend   

