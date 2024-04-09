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
	Do not include these tokens in the code: _ n
	"""

    def fraction_to_float(fraction):
        return float(fraction.split('/')[0]) / float(fraction.split('/')[1])

    def float_to_fraction(float_num):
        return str(int(float_num * 100)) + '/100'

    return float_to_fraction(fraction_to_float(x) * fraction_to_float(n)) == float_to_fraction(int(fraction_to_float(x) * fraction_to_float(n)))


def simplify_brute_force(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: _ n
	"""

    def fraction_to_float(fraction):
        return float(fraction.split('/')[0]) / float(fraction.split('/')[1])

    def float_to_fraction(float_num):
        return str(int(float_num * 100)) + '/100'

    for i in range(1, 100):
        if float_to_fraction(fraction_to_float(x) * fraction_to_float(n)) == float_to_fraction(i):
            return True
    return False


print(simplify("1/5", "5/1"))
print(simplify("1/6", "2/1"))
print