def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""


    return x + y


def subtract(x: int, y: int):
    """Subtract two numbers x and y
    >>> subtract(2, 3)
    -1
    >>> subtract(5, 7)
    -2
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""


    return x - y


def multiply(x: int, y: int):
    """Multiply two numbers x and y
    >>> multiply(2, 3)
    6
    >>> multiply(5, 7)
    35
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""


    return x * y


def divide(x: int, y: int):
    """Divide two numbers x and y
    >>> divide(2, 3)
    0
    >>> divide(5, 7)
    0
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""


    return x / y


def is_leap_year(year: int):
    """Check if a year is a leap year
    >>> is_leap_year(2021)
    False
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(1900)
    False
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""


    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def to_leap_year(year: int):
    """Convert a year to a leap year
    >>> to_leap_year(2021)
    2024
    >>> to_leap_year(2020)
    2020
    >>> to_leap