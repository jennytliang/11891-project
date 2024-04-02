def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Do not include these tokens in the code: print ( add ( 3 , 4 ))
	"""


    return x + y


def subtract(x: int, y: int):
    """Subtract two numbers x and y
    >>> subtract(20, 3)
    17
    >>> subtract(5, 7)
    -2
    
	Do not include these tokens in the code: print ( subtract ( 3 , 4 ))
	"""


    return x - y


def multiply(x: int, y: int):
    """Multiply two numbers x and y
    >>> multiply(20, 3)
    60
    >>> multiply(5, 10)
    50
    
	Do not include these tokens in the code: print ( multiply ( 3 , 4 ))
	"""


    return x * y


def divide(x: float, y: float):
    """Divide two numbers x and y
    >>> divide(20, 3)
    6.666666666666666
    >>> divide(5, 3)
    1.6666666666666667
    
	Do not include these tokens in the code: print ( divide ( 3 , 4 ))
	"""


    return x / y


def power(x: int, y: int):
    """ Raises x to the power of y
    >>> power(2,3)
    8
    >>> power(2,4)
    16
    
	Do not include these tokens in the code: print ( power ( 3 , 4 ))
	"""


    return x ** y

# Do not delete the lines below.
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)