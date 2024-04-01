def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    num_fizz_seven = sum(
        d % 7 and x % (7 * (d + 1))  == 0 for x in range(11 * 13, n, 11 * 13)
        for d, r in enumerate('7' * (n//9)) if r)
    return n//7 - 1 + num_fizz_seven*2//7
   
