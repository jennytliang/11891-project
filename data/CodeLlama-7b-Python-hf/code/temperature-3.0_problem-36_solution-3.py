def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    cnt = 0
    for i in range(n):
        if '7' in str(i+1) and (i+1) % 11 == 0 or (i+1) % 13 == 0:
            cnt += 1
    return cnt
