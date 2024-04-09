def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""



    return 0


def subtract(x: int, y: int):
    """Subtract two numbers x and y
    >>> subtract(2, 3)
    -1
    >>> subtract(5, 7)
    -2
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""



    return 0


def multiply(x: int, y: int):
    """Multiply two numbers x and y
    >>> multiply(2, 3)
    6
    >>> multiply(5, 7)
    35
    
	Do not include these tokens in the code: def multiply ( x : int , y :
	"""



    return 0


def divide(x: int, y: int):
    """Divide two numbers x and y
    >>> divide(2, 3)
    0
    >>> divide(5, 7)
    0
    
	Do not include these tokens in the code: def divide ( x : int , y :
	"""



    return 0


def main():
    """Main function of the program
	Do not include these tokens in the code: def main ():
	"""
    print("Welcome to my calculator")
    print("Please select the operation")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    while True:
        try:
            choice = int(input("Enter choice (1/2/3/4/5): "))
        except ValueError:
            print("Invalid input")
            continue

        if choice == 1:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print("Result is: ", add(x, y))
        elif choice == 2:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print("Result is: ",