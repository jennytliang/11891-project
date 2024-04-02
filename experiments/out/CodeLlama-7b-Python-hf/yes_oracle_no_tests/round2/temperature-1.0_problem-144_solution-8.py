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
	Do not include these tokens in the code: import re class
	"""

    def simplefy(x, n):
        num1 = x.split('/')[0]
        den1 = x.split('/')[1]
        num2 = n.split('/')[0]
        den2 = n.split('/')[1] # num1*num2 is still a number so cancels the denominators
        whole = (int(num1) * int(num2)) / int(den2)
        whole = str(whole)
        numwhole = whole.split('/')[0]
        denwhole = whole.split('/')[1]
        if int(numwhole) == 1 and int(denwhole) != 1:
            return True
        else:
            return False
    return False # change this line
