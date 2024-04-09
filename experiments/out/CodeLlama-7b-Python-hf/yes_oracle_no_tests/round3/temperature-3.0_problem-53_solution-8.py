def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Include these tokens in the code: return x + y
	"""
    pass


def sub(x: int, y: int):
    """Subtract two numbers x and y
    >>> sub(2, 3)
    -1
    >>> sub(5, 7)
    -2
    
	Include these tokens in the code: return x - y
	"""
    pass


def mul(x: int, y: int):
    """Multiply two numbers x and y
    >>> mul(2, 3)
    6
    >>> mul(5, 7)
    35
    
	Include these tokens in the code: return x * y
	"""
    pass


def div(x: int, y: int):
    """Divide two numbers x and y
    >>> div(2, 3)
    0
    >>> div(5, 7)
    0
    
	Include these tokens in the code: return x / y
	"""
    pass


def main():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    main()
