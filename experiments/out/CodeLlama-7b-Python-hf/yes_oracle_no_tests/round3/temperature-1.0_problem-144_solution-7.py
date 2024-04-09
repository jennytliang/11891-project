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
    num, den = x.split("/")
    num, den = int(num), int(den)

    num2, den2 = n.split("/")
    num2, den2 = int(num2), int(den2)

    # Check if the product of the x and n is a whole number
    if (num * num2) % den == 0 and (num * num2) % den2 == 0:
        return True
    else:
        return False


# Tests
def test_simplify():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/10", "1/10") == True
    assert simplify("1/10", "2/5") == False


if __name__ == "__main__":
    test_simplify()
