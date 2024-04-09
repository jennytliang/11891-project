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
	Do not include these tokens in the code: a
	"""
    num1, den1 = x.split('/')
    num2, den2 = n.split('/')
    return (int(num1) * int(den2) == int(num2) * int(den1))


def simplify_solution(x, n):
    """
    My solution.
    """
    a, b = x.split('/')
    c, d = n.split('/')
    return int(a) * int(d) == int(b) * int(c)


def test(expect, *pargs):
    """
    Test the function using a variety of inputs and output the
    results.
    """
    print('EXPECTED: %s' % (expect,))
    print('ACTUAL: %s = %s' % (pargs, simplify(*pargs)))


if __name__ == '__main__':
    # test(True, '1/5', '5/1')
    # test(False, '1/6', '2/1')
    # test(False, '7/10', '10/2')
    # test(True, '1/1', '1/1')
    # test(False, '1/10', '10/1')
    # test(True, '1/2', '5/10')
    # test(True, '1/1', '5/5')
    # test(True, '1/5', '5/10')
    test(False, '1/6', '2/1')
    test(True, '1/6', '3/2')
    test(True, '1/6', '1/2')
