def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Include these tokens in the code: 1 , x 2
	Do not include these tokens in the code: _
	"""

    # x and n are strings. split them into numerator and denominator
    # numerator and denominator are strings
    # return True if x * n is a whole number
    
    x_numerator, x_denominator = x.split('/')
    n_numerator, n_denominator = n.split('/')

    x_numerator = int(x_numerator)
    x_denominator = int(x_denominator)
    n_numerator = int(n_numerator)
    n_denominator = int(n_denominator)

    if (x_numerator * n_denominator) % n_numerator == 0 and (x_denominator * n_numerator) % n_denominator == 0:
        return True
    else:
        return False


print(simplify('1/5', '5/1'))
print(simplify('1/6', '2/1'))
print(simplify('7/10', '10/2'))