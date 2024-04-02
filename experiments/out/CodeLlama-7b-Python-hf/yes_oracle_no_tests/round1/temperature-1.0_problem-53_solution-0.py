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
    """Minuses two numbers 
    >>> subtract(2, 4)
    -2
    >>> subtract(5, 8)
    -3
    """
    return x - y

def subtract3args(x: int, y: int, z: int):
    """Three integers"""
    return x - y - z -3

def addition_and_subtraction(x: int, y: int):
    """Addition and subtraction using 1 function"""
    return (x + y) * y / y - 3

def multiplication(x: int, y: int):
    """Multiply two numbers """
    return x * y

__test__ = {
    "add3arg":
    '>>> add(2, 3)\n5\n>>> add(5, 7) \n12\n',
    "subtract3args":
    '>>> subtract(2, 4)\n-2 \n>>> subtract(5, 8) \n-3 \n',
    "subtract": '>>> subtract(2, 4) \n-2 \n>>> subtract(5, 7)\n-2\n',
    "addition_and_subtraction":
    '>>> addition_and_subtraction(2, 4)\n1 \n>>> subtraction(3,6)\n-3\n',
    "multiplication": '>>> multiplication(4 ,4) \n16\n>>> multiply (2, 2)\n4\n',
}
