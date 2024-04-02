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
	Do not include these tokens in the code: numer ator _
	"""
    def gcd(a,b):
        if a < b:
            a, b = b, a
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def simplify(x, n):
        x = x.split("/")
        n = n.split("/")
        if gcd(int(x[0]), int(n[1])) == 1:
            return True
        else:
            return False
    
    return simplify(x, n)


def simplify_2(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Include these tokens in the code: x 1
	Do not include these tokens in the code: numer ator _
	"""
    def gcd(a,b):
        if a < b:
            a, b = b, a
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def simplify(x, n):
        x = x.split("/")
        n = n.split("/")
        if int(n[1]) == 1:
            return True
        elif int(x[0]) * int(n[1]) == int(n[0]) * int(x[1]):
            return True
        elif gcd(int(x[0]), int(n[1])) == 1:
            return True
        else:
            return False
    
    return simplify