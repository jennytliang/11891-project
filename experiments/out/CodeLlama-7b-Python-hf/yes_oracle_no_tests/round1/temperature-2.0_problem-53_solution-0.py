def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Do not include these tokens in the code: def sub ( x : int , y :
	"""

    return x  + y

def sub(x: int, y: int):
    """Subtract two numbers x and y
    >>> sub(2, 3)
    5
    >>> sub(5, 7)
    12
    
	Do not include these tokens in the code: def sub ( x : int , y :
	"""

    return x  - y

def mul(x: int, y: int):
    """Multiply two numbers x and y
    >>> mul(2, 3)
    5
    >>> mul(5, 7)
    12
    
	Do not include these tokens in the code: def sub ( x : int , y :
	"""

    return x  * y

def div(x: int, y: int):
    """Divide two numbers x and y
    >>> div(2, 3)
    5
    >>> div(5, 7)
    12
    
	Do not include these tokens in the code: def sub ( x : int , y :
	"""

    return x  / y

def main():
    print("Addition: ", add(5, 7))
    print("Subtraction: ", sub(5, 7))
    print("Multiplication: ", mul(5, 7))
    print("Division: ", div(5, 7))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
