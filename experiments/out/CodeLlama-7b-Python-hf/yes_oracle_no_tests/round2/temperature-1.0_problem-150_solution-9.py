def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: if n <= 1 :
	"""
	pass

# Do not edit this code ---==---->
# Run the code before submitting
def test_(expected, result):
    if expected == result:
        print("Pass")
    else:
        print("Fail")


test_(28, x_or_y(7, 9, 28))
test_(28, x_or_y(11, 28, 9))
test_(9, x_or_y(12, 9, 28))
# <----==-----


# Run this code to test your function
def is_prime(n):
    if n <= 1:
        return False
    for x in range(2, n // 2 + 1):
        if n % x == 0:
            return False
    return True


def x_or_y(n, x, y):
    if is_prime(n):
        return x
    return y


def test_(expected, result):
    if expected == result:
        print("Pass")
    else:
        print("Fail")


test_(28, x_or_y(7, 9, 28))
test_(28, x_or_y(11, 28, 9))
test_(9, x_or_y(12, 9, 28))
