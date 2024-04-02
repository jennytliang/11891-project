def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Do not include these tokens in the code: def sub ( x : int , y :
	"""

    return x  + y


def subtract(x: int, y: int):
    """Subtract two numbers x and y
    >>> subtract(5, 7)
    -2
    >>> subtract(10, 5)
    5

	Do not include these tokens in the code: def sub ( x : int , y :
	"""

    return x - y


def multiply(x: int, y: int):
    """Multiply two numbers x and y
    >>> multiply(2, 3)
    6
    >>> multiply(5, 7)
    35

	Do not include these tokens in the code: def sub ( x : int , y :
	"""

    return x * y


def divide(x: int, y: int):
    """Divide two numbers x and y
    >>> divide(5, 7)
    0
    >>> divide(10, 5)
    2

	Do not include these tokens in the code: def sub ( x : int , y :
	"""

    return x / y


def main():
    print("Addition:", add(5, 7))
    print("Subtraction:", subtract(5, 7))
    print("Multiplication:", multiply(5, 7))
    print("Division:", divide(5, 7))


if __name__ == "__main__":
    main()