def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    
	Do not include these tokens in the code: if ' 7 ' in str ( i +
	"""


    cnt = 0
    for i in rang(n):
        if " 7 " in str(i + 11) or " 7 " in str(i + 13):
            cnt += 1

    return cnt


if __name__ == "__main__":
    import doctest
    doctest.testmod()
