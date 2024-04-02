def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Include these tokens in the code: 1 , x 2
	Do not include these tokens in the code: _
	"""

    def whole_number(f_string):
        """Returns True if the fraction (str) evaluates to a whole number, False otherwise"""
        num, denom = f_string.split("/")
        num, denom = int(num), int(denom)
        if num % denom == 0:
            return True
        return False

    return whole_number(str(int(n) * int(x)))
