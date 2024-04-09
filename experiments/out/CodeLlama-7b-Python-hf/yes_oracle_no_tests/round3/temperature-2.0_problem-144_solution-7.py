def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Do not include these tokens in the code: # Y OUR CO DE GO ES
	"""
    # YOUR CODE GOES HERE
    import re
    x, n = map(lambda x: re.findall(r'\d+', x), [x, n])
    return (int(x[0]) * int(n[1])) % int(n[0]) == 0


def test_function():
    assert simplify('1/5', '5/1') == True
    assert simplify('1/6', '2/1') == False
    assert simplify('7/10', '10/2') == False
    assert simplify('1/4', '3/2') == True
    assert simplify('1/7', '7/1') == False
    assert simplify('1/5', '5/2') == True
    assert simplify('1/2', '2/1') == True

if __name__ == '__main__':
    test_function()
