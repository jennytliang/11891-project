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
    >>> sub(5, 7)
    -2
    >>> sub(5, 3)
    2
	Do not include these tokens in the code: def sub ( x : int , y :
	"""
    return x - y

def mul(x: int, y: int):
    """Multiply two numbers x and y
    >>> mul(2, 3)
    6
    >>> mul(5, 7)
    35
	Do not include these tokens in the code: def sub ( x : int , y :
	"""
    return x * y

def div(x: int, y: int):
    """Divide two numbers x and y
    >>> div(5, 7)
    0
    >>> div(5, 3)
    1
	Do not include these tokens in the code: def sub ( x : int , y :
	"""
    return x // y

def main():
    print("The add function adds two numbers")
    print("The sub function subtracts two numbers")
    print("The mul function multiplies two numbers")
    print("The div function divides two numbers")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()