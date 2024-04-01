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

    numerator = int(x.split("/", 2)[0])*int(n.split("/", 2)[1])  # numerator for x * n is multiplying top of x's num/denom and top of n's num/deno
    #denominator x's top is bottom of n bottom multiply n's denom by bottom denom of x = new denom

    if (numerator % int(n.split("/", 2)[1])) == 0: return True

    return False


print simplify('9/7', '1/200')