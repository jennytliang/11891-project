def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Do not include these tokens in the code: def sub ( x : int , y :
	"""

    return x  + y


def sub(x: int, y: int):
    """Subtract two numbers x and y
    >>> sub(2, 3)
    -1
    >>> sub(5, 7)
    -2
    
	Do not include these tokens in the code: def sub ( x : int , y :
	"""

    return x - y


def mul(x: int, y: int):
    """Multiply two numbers x and y
    >>> mul(2, 3)
    6
    >>> mul(5, 7)
    35
    
	Do not include these tokens in the code: def sub ( x : int , y :
	"""

    return x * y


def div(x: int, y: int):
    """Divide two numbers x and y
    >>> div(2, 3)
    0
    >>> div(5, 7)
    0
    
	Do not include these tokens in the code: def sub ( x : int , y :
	"""

    return x / y


def main():
    print("Welcome to the Python Calculator")
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
                break
            elif choice == '2':
                print(f"{num1} - {num2} = {sub(num1, num2)}")
                break
            elif choice == '3':
                print(f"{num1} * {num2} = {mul(num1, num2)}")
