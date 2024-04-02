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

    def gcd(a, b):
        """
        Returns the greatest common divisor of a and b
        """
        while b:
            a, b = b, a % b
        return a

    def simplify(x, n):
        """
        Simplifies the expression x * n
        """
        num1, denom1 = x.split('/')
        num2, denom2 = n.split('/')
        num = int(num1) * int(num2)
        denom = int(denom1) * int(denom2)
        if gcd(num, denom) != 1:
            return False
        else:
            return True

    return simplify(x, n)
