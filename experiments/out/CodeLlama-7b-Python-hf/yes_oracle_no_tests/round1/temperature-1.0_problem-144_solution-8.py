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

    import re

    class Fraction:
        numerator = 0
        denominator = 0
        
        def __init__(self, numStr):
            n, d = map(numStr.split("/"))
            self.numerator = int(n);  self.denominator = int(d)
            assert self.denominator > 0, "Invalid denominator!"
            
        def __multiply__(self, scalar):
            return Fraction(str(int(self.numerator * scalar)/ self.denominator))
        
        def __repr__(self):
            return numStr
        
    numStr = re.sub("[ ]+", "/", str(Fraction(x)))
    return numStr in fractionsIn("*" + str(int(n)))

def fractionsIn(operation):
    return set(fraction for x in fractionsIn("(" + operation + ")") for fraction in x.split("/")
             if operation not in ("", "1") and not any([char.isdigit() for char in operation])) 

import unittest
class TeststringMethods(unittest.TestCase):    
    def test_simplify(self):
        self.assertEqual(simplify("1/5", "5/1"), True)
        self.assertEqual(simplify("1/6", "2/1"), False)
        self.assertEqual(simplify("7/10", "10/2"), False)

if __name__=="__main__":
    unittest.main(exit=False)
