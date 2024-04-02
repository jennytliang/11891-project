def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""

    r = 0
    for i in string:
        r += 1
    return r


def sum(num1: int, num2: int) -> int:
    """ Return sum of given integers
    >>> sum(1,2)
    3
    >>> sum(0,-1)
    -1
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""

    r = num1 + num2
    return r


def average(num1: int, num2: int) -> float:
    """ Return average of given integers
    >>> average(1,2)
    1.5
    >>> average(-1,2)
    0.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""

    r = (num1 + num2) / 2
    return r


def max_num(num1: int, num2: int) -> int:
    """ Return maximum of given integers
    >>> max_num(1,2)
    2
    >>> max_num(-1,2)
    2
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""

    r = max(num1, num2)
    return r


def is_even(num: int) -> bool:
    """ Return whether given integer is even
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""

    if num % 2 == 0:
        r = True
    else:
        r = False
    return r


def is_odd(num: int) -> bool:
    """ Return whether given integer is odd
    >>> is_odd(2)
    False
    >>> is_odd(3)
    True
    
	Include these tokens in the code: return
	Do not include these tokens in the