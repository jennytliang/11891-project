def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Include these tokens in the code: x 1
	Do not include these tokens in the code: a
	"""
    numerator = int(x.split('/')[0])
    denominator = int(x.split('/')[1])
    
    numerator2 = int(n.split('/')[0])
    denominator2 = int(n.split('/')[1])
    
    if (numerator * denominator2) % denominator == 0 and (numerator2 * denominator) % denominator2 == 0:
        return True
    else:
        return False













