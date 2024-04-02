def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Do not include these tokens in the code: def g cd ( a ,
	"""

    num1, den1 = x.split("/")
    num2, den2 = n.split("/")

    num1, den1 = int(num1), int(den1)
    num2, den2 = int(num2), int(den2)

    return (num1 * num2) % den2 == 0 and (num2 * den1) % den2 == 0

    # return (num1 * num2) % den2 == 0 and (num2 * den1) % den2 == 0


if __name__ == '__main__':
    print(simplify("1/5", "5/1"))
    print(simplify("1/6", "2/1"))
    print(simplify("7/10", "10/2"))
