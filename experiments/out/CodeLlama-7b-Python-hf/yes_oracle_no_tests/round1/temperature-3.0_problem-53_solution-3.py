def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Do not include these tokens in the code: def multiply ( x : int , y :
	"""

    return x  + y

def multiply(x: int, y: int):
    """Multiply two numbers x and y
    >>> multiply(2, 3)
    6
    >>> multiply(5, 7)
    35
    
	Do not include these tokens in the code: def multiply ( x : int , y :
	"""

    return x * y

if __name__ == "__main__":
    import doctest
    doctest.testmod()
