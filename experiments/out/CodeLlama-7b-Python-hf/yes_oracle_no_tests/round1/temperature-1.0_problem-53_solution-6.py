def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""

    return x  + y


def subtract(x: int, y: int):
    """
    >>> subtract(2, 3)
    -1
    >>> subtract(5, 7)
    -2
    """
    return x - y


def multiply(x: int, y: int):
    """
    >>> multiply(2, 3)
    6
    >>> multiply(5, 7)
    35
    """
    return x * y


def divide(x: int, y: int):
    """
    >>> divide(2, 3)
    0
    >>> divide(5, 7)
    0
    """
    return x / y


def main():
    print("Addition")
    print(add(10, 5))
    print(add(10, 3))

    print("Subtraction")
    print(subtract(10, 5))
    print(subtract(10, 3))

    print("Multiplication")
    print(multiply(10, 5))
    print(multiply(10, 3))

    print("Division")
    print(divide(10, 5))
    print(divide(10, 3))


if __name__ == "__main__":
    main()
