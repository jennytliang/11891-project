def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n <= 0:
        raise ValueError("n must be greater than 0")
    if n <= 50:
        return 0
    if n > 50:
        number_7s = [7]
        for num in range(51, n):
            for dig in number_7s:
                if str(dig) in str(num) and (num % 11 == 0 or num % 13 == 0):
                    number_7s.append(num)
        return len(number_7s)-1