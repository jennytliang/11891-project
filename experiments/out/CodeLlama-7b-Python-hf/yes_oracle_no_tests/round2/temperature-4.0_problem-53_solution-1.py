def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret =
	"""
    ret = x + y
    return ret

def subtract(x: int, y: int):
    """Subtract two numbers x and y
    >>> subtract(2, 3)
    -1
    >>> subtract(5, 7)
    -2
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret =
	"""
    ret = x - y
    return ret

def multiply(x: int, y: int):
    """Multiply two numbers x and y
    >>> multiply(2, 3)
    6
    >>> multiply(5, 7)
    35
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret =
	"""
    ret = x * y
    return ret

def divide(x: int, y: int):
    """Divide two numbers x and y
    >>> divide(2, 3)
    0
    >>> divide(5, 7)
    0
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret =
	"""
    ret = x / y
    return ret

def power(x: int, y: int):
    """Raise x to the power of y
    >>> power(2, 3)
    8
    >>> power(5, 7)
    16807
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret =
	"""
    ret = x ** y
    return ret

def factorial(n: int):
    """Factorial of a number n
    >>> factorial(2)
    2
    >>> factorial(5)
    120
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret =
	"""
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

def is_even(n: int):
    """Check if a number is even
