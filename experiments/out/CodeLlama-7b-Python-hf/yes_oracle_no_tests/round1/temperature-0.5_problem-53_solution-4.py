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


def main():
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"subtract(5, 7) = {subtract(5, 7)}")
    print(f"multiply(2, 3) = {multiply(2, 3)}")
    print(f"divide(5, 7) = {divide(5, 7)}")


if __name__ == "__main__":
    main()