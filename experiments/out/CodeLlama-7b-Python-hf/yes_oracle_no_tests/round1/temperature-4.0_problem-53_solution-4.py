def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Do not include these tokens in the code: def subtract ( x : int , y : int
	"""

    return x  + y


def subtract(x: int, y: int):
    """Subtract two numbers x and y
    >>> subtract(5, 3)
    2
    >>> subtract(5, 7)
    -2
    
	Do not include these tokens in the code: def subtract ( x : int , y : int
	"""

    return x - y


def multiply(x: int, y: int):
    """Multiply two numbers x and y
    >>> multiply(5, 3)
    15
    >>> multiply(5, 7)
    35
    
	Do not include these tokens in the code: def multiply ( x : int , y : int
	"""

    return x * y


def divide(x: int, y: int):
    """Divide two numbers x and y
    >>> divide(5, 3)
    1
    >>> divide(5, 7)
    0
    
	Do not include these tokens in the code: def divide ( x : int , y : int
	"""

    return x / y


def power(x: int, y: int):
    """Raise x to the power of y
    >>> power(5, 3)
    125
    >>> power(5, 7)
    78125
    
	Do not include these tokens in the code: def power ( x : int , y : int
	"""

    return x ** y


def modulo(x: int, y: int):
    """Return the remainder of x divided by y
    >>> modulo(5, 3)
    2
    >>> modulo(5, 7)
    5
    
	Do not include these tokens in the code: def modulo ( x : int , y : int
	"""

    return x % y


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
