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
	Do not include these tokens in the code: num _
	"""

    # x, n = (1, 5), (5, 1)
    # x, n = (1, 6), (2, 1)
    # x, n = (7, 10), (10, 2)

    # x, n = (1, 3), (3, 1)
    # x, n = (1, 3), (5, 3)
    # x, n = (1, 3), (5, 6)

    # x, n = (1, 1), (1, 1)

    # x, n = (1, 2), (2, 1)
    # x, n = (1, 2), (2, 2)
    # x, n = (1, 2), (3, 2)

    # x, n = (1, 3), (3, 1)
    # x, n = (1, 3), (5, 3)
    # x, n = (1, 3), (5, 6)

    # x, n = (1, 3), (3, 1)
    # x, n = (1, 3), (5, 3)
    # x, n = (1, 3), (5, 6)

    # x, n = (1, 5), (5, 1)
    # x, n = (1, 6), (2, 1)
    # x, n = (7, 10), (10, 2)
    
    # x, n = (1, 3), (1, 3)
    # x, n = (1, 3), (2, 3)
    # x, n = (1, 3), (3, 3)
    
    # x, n = (1, 3), (2, 3)
    # x, n = (1, 3), (3, 3)
    # x, n = (1, 3), (4, 3)
    
    # x, n = (1