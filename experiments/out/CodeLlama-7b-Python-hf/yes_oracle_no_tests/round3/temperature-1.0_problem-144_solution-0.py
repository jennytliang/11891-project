def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: _ numer ator
	"""

    x_n, x_d = x.split("/")
    n_n, n_d = n.split("/")
    x_n = int(x_n)
    x_d = int(x_d)
    n_n = int(n_n)
    n_d = int(n_d)
    
    x_n = x_n * n_d
    x_d = x_d * n_n
    
    if x_d == 0:
        return False
    else:
        return x_n % x_d == 0