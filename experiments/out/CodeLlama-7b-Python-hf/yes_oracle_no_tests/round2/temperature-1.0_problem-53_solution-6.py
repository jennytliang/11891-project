def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""


    return x + y

def multiply(x: int, y: int):
    """Multiply two numbers x and y.
	
	>>> multiply(2, 3)
	6
	>>> multiply(5, 7)
	35
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""


    # YOUR CODE HERE
    return x * y

def subtract(x: int, y: int):
    """Return the difference of two numbers x and y.
	
	>>> subtract(2, 3)
	-1
	>>> subtract(5, 10)
	-5
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""




def avg(values):
    """Return the average of an array of numbers.
	
	>>> avg([2, 5, 12, 98])
	33.25
	Do not include these tokens in the code: def subtract ( x : int , y :
	"""



    # YOUR CODE HERE
    return sum(values) / len(values)

def factorial(x: int):
    """Return the factorial of x (i.e. x!). 
	
	>>> factorial(7)
	5040
    
    Do not include these tokens in the code: def factorial ( x : int )
	"""



	
    # YOUR CODE HERE
    return 1 if x == 0 else x * factorial(x - 1)
    
    
# 2
def add(x: int, y: int):
    """Return the sum of 2 numbers. Both arguments must be integers from 0 to 100.
	The addition is done safely, so overflows are handled: 99 + 1 = 1.
	
	>>> add(10, 99)
	10
	>>> add(50, 50)
	0
	>>> add(1, 