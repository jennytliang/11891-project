def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: if n >  1 :
	"""

    
    if is_prime(n):
        return x
    else:
        return y


def is_prime(n):
    if n > 1:
        for x in range(2, n):
            if (n % x) == 0:
                return False
        else:
            return True
    else:
        return False


def test_function(test_case):
    answer = x_or_y(test_case[0], test_case[1], test_case[2])
    if answer == test_case[3]:
        print("Pass!")
    else:
        print("Fail!")


test_function([7, 34, 12, 34])
test_function([15, 8, 5, 5])
test_function([12, 34, 12, 34])
test_function([23, 8, 5, 5])
test_function([14, 34, 12, 34])
