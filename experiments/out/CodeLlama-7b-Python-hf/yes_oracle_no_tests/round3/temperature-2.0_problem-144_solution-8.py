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
	"""

    x_num, x_denom = x.split('/')
    n_num, n_denom = n.split('/')
    x_num = int(x_num)
    x_denom = int(x_denom)
    n_num = int(n_num)
    n_denom = int(n_denom)

    if (x_num * n_num) % n_denom == 0 and (x_denom * n_denom) % n_num == 0:
        return True
    else:
        return False


def test_simplify():
    assert simplify('1/5', '5/1') == True
    assert simplify('1/6', '2/1') == False
    assert simplify('7/10', '10/2') == False
    assert simplify('1/2', '1/1') == True
    assert simplify('1/2', '1/2') == False
    assert simplify('1/2', '2/1') == True
    assert simplify('1/2', '2/2') == True
    assert simplify('2/20', '1/2') == True
    assert simplify('2/20', '1/1') == False
    assert simplify('2/20', '2/2') == False
    assert simplify('2/20', '20/2') == False
    assert simplify('2/20', '2/1') == False
    assert simplify('1/4', '1/4') == True
    assert simplify('1/4', '1/2') == True
    assert simplify('1/4', '2/1') == False
    assert simplify('1/4', '2/2') == False
    assert simplify('1/4', '4/2') == True
    assert simplify('1/4', '4/1') == False
    assert simplify('1/4', '8/2') == False
    assert simplify('10/4', '10/2') == True
    assert simplify('10/4', '20/1') == False
    assert simplify('1