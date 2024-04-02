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

    # Split into numerator / denominator (each numerator and denominator are string representations of whole numbers)
    xN, xD = x.split("/")
    nN, nD = n.split("/")
    assert(xN.isdigit() and xD.isdigit() and nN.isdigit() and nD.isdigit())
    xNum = int(xN) / int(xD)
    nNum = int(nN) / int(nD)

    # Evaluate X * N
    xn = round(xNum * nNum, 10)
    return xn - round(xn) < .00000000001
