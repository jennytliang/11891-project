def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""

    return x  + y


def subtract(x: int, y: int):
    """
    >>> subtract(5, 3)
    2
    >>> subtract(10, 10)
    0
    """
    return x - y


def multiply(x: int, y: int):
    """
    >>> multiply(10, 10)
    100
    >>> multiply(3, 5)
    15
    """
    return x * y


def divide(x: int, y: int):
    """
    >>> divide(10, 2)
    5.0
    >>> divide(10, 10)
    1.0
    """
    return x / y


def power(x: int, y: int):
    """
    >>> power(2, 3)
    8
    >>> power(2, 2)
    4
    """
    return x ** y


def sum_of_digits(x: int):
    """
    >>> sum_of_digits(123)
    6
    >>> sum_of_digits(25)
    7
    """
    return sum(int(digit) for digit in str(x))


def is_leap_year(x: int):
    """
    >>> is_leap_year(1990)
    False
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(2000)
    True
    """
    if x % 400 == 0:
        return True
    elif x % 100 == 0:
        return False
    elif x % 4 == 0:
        return True
    else:
        return False


def sum_of_n_numbers(n: int):
    """
    >>> sum_of_n_numbers(10)
    55
    """
    return n * (n + 1) // 2


def sum_of_n_numbers_with_step(n: int,