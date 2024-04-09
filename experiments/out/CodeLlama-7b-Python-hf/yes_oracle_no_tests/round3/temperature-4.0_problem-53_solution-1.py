def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret =
	"""
    return x + y


def subtract(x: int, y: int):
    """Subtract two numbers x and y
    >>> subtract(2, 3)
    -1
    >>> subtract(5, 7)
    -2
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret =
	"""
    return x - y


def multiply(x: int, y: int):
    """Multiply two numbers x and y
    >>> multiply(2, 3)
    6
    >>> multiply(5, 7)
    35
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret =
	"""
    return x * y


def divide(x: int, y: int):
    """Divide two numbers x and y
    >>> divide(2, 3)
    0
    >>> divide(5, 7)
    0
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret =
	"""
    return x / y


def main():
    print("Testing math operations")
    assert add(2, 3) == 5
    assert subtract(5, 7) == -2
    assert multiply(2, 3) == 6
    assert divide(5, 7) == 0
    print("Math operations are tested successfully!")


if __name__ == "__main__":
    main()
