def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    
	Do not include these tokens in the code: if str ( i ). find (' 7
	"""


    cnt = 0
    for i in ran(1, n):
        if i%11 == 0 or i%13 == 0:
            cnt += i.count('7')
    return cnt


import random

def ran(a,b):
    """
    Return a random integer between a and b inclusive.
    """
    return random.randint(a,b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()