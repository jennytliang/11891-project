def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Include these tokens in the code: x
	Do not include these tokens in the code: num
	"""
    import re

    # split the fractions into numerators and denominators
    x_numerator, x_denominator = x.split('/')
    n_numerator, n_denominator = n.split('/')

    # convert fractions to integers
    x_numerator = int(x_numerator)
    x_denominator = int(x_denominator)
    n_numerator = int(n_numerator)
    n_denominator = int(n_denominator)

    # compute the product of the fractions
    x_n = x_numerator * n_numerator
    x_d = x_denominator * n_denominator

    # check if the product is an integer
    if x_n % x_d == 0:
        return True
    else:
        return False


simplify('1/5', '5/1')
