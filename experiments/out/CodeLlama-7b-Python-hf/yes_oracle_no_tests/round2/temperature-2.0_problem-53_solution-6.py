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
    5
    >>> subtract(5, 7)
    12
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""


    return x - y


def multiply(x: int, y: int):
    """Multiply two numbers x and y
    >>> multiply(2, 3)
    5
    >>> multiply(5, 7)
    12
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""


    return x * y


def divide(x: int, y: int):
    """Divide two numbers x and y
    >>> divide(2, 3)
    5
    >>> divide(5, 7)
    12
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""


    return x / y


if __name__ == "__main__":
    import doctest
    doctest.testmod()
