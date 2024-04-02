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

    num1, num2 = x.split('/')
    num1 = int(num1)
    num2 = int(num2)

    num3, num4 = n.split('/')
    num3 = int(num3)
    num4 = int(num4)

    if (num1 * num4) % num4 == 0:
        if (num2 * num3) % num3 == 0:
            if (num1 * num4) % num3 == 0:
                return True
    return False


print(simplify("1/5", "5/1"))
print(simplify("1/6", "2/1"))
print(simplify("7/10", "10/2"))
