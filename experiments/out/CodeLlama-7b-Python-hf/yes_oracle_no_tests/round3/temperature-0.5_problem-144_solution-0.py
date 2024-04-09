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
	Do not include these tokens in the code: # Your code here num
	"""
    def make_int(x):
        return int(x.split('/')[0])

    def make_den(x):
        return int(x.split('/')[1])

    x_int = make_int(x)
    x_den = make_den(x)

    n_int = make_int(n)
    n_den = make_den(n)

    if (x_int * n_den) % n_int == 0:
        return True
    else:
        return False

print(simplify("1/5", "5/1"))
print(simplify("1/6", "2/1"))
print(simplify("7/10", "10/2"))
