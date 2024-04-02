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
    >>> subtract(5, 3)
    2
    >>> subtract(10, 20)
    -10
    
    Do not include these tokens in the code: def subtract ( x : int , y :
    """


    return x - y


def multiply(x: int, y: int):
    """Multiply two numbers x and y
    >>> multiply(5, 3)
    15
    >>> multiply(10, 20)
    200
    
    Do not include these tokens in the code: def multiply ( x : int , y :
    """


    return x * y


def divide(x: int, y: int):
    """Divide two numbers x and y
    >>> divide(5, 3)
    1
    >>> divide(10, 20)
    0
    
    Do not include these tokens in the code: def divide ( x : int , y :
    """


    return x / y


def power(x: int, y: int):
    """Raise number x to the power y
    >>> power(2, 3)
    8
    >>> power(10, 2)
    100
    
    Do not include these tokens in the code: def power ( x : int , y :
    """


    return x ** y


def modulo(x: int, y: int):
    """Return the modulo of x and y
    >>> modulo(5, 3)
    2
    >>> modulo(10, 2)
    0
    
    Do not include these tokens in the code: def modulo ( x : int , y :
    """


    return x % y


def main():
    import doctest

    doctest.testmod()


if __name__ == '__main__':
    main()
