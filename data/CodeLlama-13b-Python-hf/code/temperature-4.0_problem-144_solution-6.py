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
    def get_frac_pair(f):
        return f.split('/')

    n_int, n_den = get_frac_pair(n)
    # x_frac1 = fractions.Fraction(int(x_int)//int(den1), int(n_den // int(n_den)));
    x_int, denominator1 = float(x) ,float(x_den)
    # return (den1 * n_den) in (x_int*n_Int)



    return False # return answer

# solution
def simplify(x, n):
    return float(x) * float(n) % 1 == 0