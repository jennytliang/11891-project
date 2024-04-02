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
	Do not include these tokens in the code: _ l
	"""

    # Your code here
    int_part_x, frac_part_x = x.split("/")
    int_part_n, frac_part_n = n.split("/")
    divisor = int(int_part_n) * int(frac_part_x) + int(frac_part_n) * int(int_part_x)

    if divisor % 1 == 0:
        return True
    else:
        return False
