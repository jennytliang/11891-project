def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Do not include these tokens in the code: def sub ( x : int , y : int
	"""


    return x + y


def sub(x: int, y: int):
    """Subtract two numbers x and y
    >>> sub(2, 3)
    -1
    >>> sub(5, 7)
    -2
    
	Do not include these tokens in the code: def sub ( x : int , y : int
	"""


    return x - y


def mult(x: int, y: int):
    """Multiply two numbers x and y
    >>> mult(2, 3)
    6
    >>> mult(5, 7)
    35
    
	Do not include these tokens in the code: def sub ( x : int , y : int
	"""


    return x * y


def div(x: int, y: int):
    """Divide two numbers x and y
    >>> div(2, 3)
    0
    >>> div(5, 7)
    0
    
	Do not include these tokens in the code: def sub ( x : int , y : int
	"""


    return x / y


def main():
    print("Welcome to the Interactive Calculator")
    print("Enter 'add', 'sub', 'mult', 'div' or 'quit'")
    while True:
        choice = input("What do you want to do? ")
        if choice == "add":
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print(add(x, y))
        elif choice == "sub":
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print(sub(x, y))
        elif choice == "mult":
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print(mult(x, y))
        elif choice == "div":
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print(