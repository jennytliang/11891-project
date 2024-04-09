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
    
	Do not include these tokens in the code: def multiply ( x : int , y :
	"""


    return x * y


def divide(x: int, y: int):
    """Divide two numbers x and y
    >>> divide(2, 3)
    0
    >>> divide(5, 7)
    0
    
	Do not include these tokens in the code: def divide ( x : int , y :
	"""


    return x / y


def main():
    """
    This is a doctest
    >>> add(2,3)
    5
    >>> multiply(5,7)
    35
    >>> divide(35,5)
    7.0
    >>> subtract(5,7)
    -2
    """

    print("This is a doctest")
    print(add(2, 3))
    print(multiply(5, 7))
    print(divide(35, 5))
    print(subtract(5, 7))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
