def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Include these tokens in the code: x 1 , x 2
	Do not include these tokens in the code: numer ator
	"""
    num1, den1 = x.split('/')
    num2, den2 = n.split('/')
    num1, den1 = int(num1), int(den1)
    num2, den2 = int(num2), int(den2)
    return (num1 * den2) % den1 == 0 and (num2 * den1) % den2 == 0


def test_simplify():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/6", "1/6") == True
    assert simplify("7/10", "1/2") == False
    assert simplify("7/10", "7/10") == True
    assert simplify("7/10", "1/10") == True
    assert simplify("7/10", "5/10") == True


if __name__ == '__main__':
    test_simplify()
