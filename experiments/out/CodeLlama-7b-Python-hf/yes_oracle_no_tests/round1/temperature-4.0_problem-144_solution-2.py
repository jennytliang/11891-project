def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Include these tokens in the code: x 1 , x 2
	Do not include these tokens in the code: numer ator
	"""
    numerator_x, denominator_x = x.split("/")
    numerator_n, denominator_n = n.split("/")

    # Multiply numerator x by numerator n
    numerator_product = int(numerator_x) * int(numerator_n)
    # Multiply denominator x by denominator n
    denominator_product = int(denominator_x) * int(denominator_n)

    # Simplify
    gcd = gcd_euclid(numerator_product, denominator_product)

    # Check if the product is a whole number
    if (numerator_product // gcd) == (denominator_product // gcd):
        return True
    else:
        return False

def gcd_euclid(a, b):
    """Euclid's Algorithm for Greatest Common Divisor
    """
    while a != 0:
        a, b = b % a, a
    return b
