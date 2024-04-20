def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    
	Include these tokens in the code: range
	Do not include these tokens in the code: rang
	"""



    cnt = 0
    fizzbuzz = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            fizzbuzz += i
            if 7 in str(fizzbuzz):
                cnt += 1
    return cnt













































































































































































































































































































































































































































