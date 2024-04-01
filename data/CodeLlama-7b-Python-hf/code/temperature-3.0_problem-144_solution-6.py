def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    x_numerator, x_denominator = x.split('/')
    n_numerator, n_denominator = n.split('/')

    #print(n_denominator)
    
    if (int(n_denominator) % int(x_denominator) == 0):
        x_factor = int(n_denominator) / int(x_denominator)
        y = int(x_numerator) * x_factor
        if (int(y) % int(n_numerator) == 0):
            return True
    
    return False

