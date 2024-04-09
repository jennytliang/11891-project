def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r anger
	"""


    cnt = 0
    fo = 0
    for i in range(1,n):
        if (i%11 == 0 or i%13 == 0) and (str(i).count("7") > 0):
            cnt += 1
    return cnt
