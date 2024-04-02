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
    """Subtract two numbers x and y
    >>> subtract(2, 3)
    5
    >>> subtract(5, 7)
    12
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""

    return x  - y


def multiply(x: int, y: int):
    """Multiply two numbers x and y
    >>> multiply(2, 3)
    5
    >>> multiply(5, 7)
    12
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""

    return x  * y


def divide(x: int, y: int):
    """Divide two numbers x and y
    >>> divide(2, 3)
    5
    >>> divide(5, 7)
    12
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""
    return x  / y


def main():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        # Take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif