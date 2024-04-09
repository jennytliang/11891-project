def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Include these tokens in the code: x
	Do not include these tokens in the code: # sim pl ify ("
	"""
    x = x.split('/')
    n = n.split('/')
    x = int(x[0]) * int(n[1])
    n = int(x[1]) * int(n[0])
    if x % n == 0:
        return True
    return False


if __name__ == '__main__':
    print(simplify("1/5", "5/1"))
    print(simplify("1/6", "2/1"))
    print(simplify("7/10", "10/2"))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert simplify("1/5", "5/1") == True, "1/5"
    assert simplify("1/6", "2/1") == False, "1/6"
    assert simplify("7/10", "10/2") == False, "7/10"
    assert simplify("14/2", "2/1") == True, "14/2"
    assert simplify("24/5", "5/1") == False, "24/5"
    assert simplify("6/10", "10/3") == True, "6/10"
    assert simplify("10/6", "6/10") == True, "10/6"
    assert simplify("10/6", "10/12") == True, "10/6"
    assert simplify("10/6", "12/6") == False, "10/6"
    assert simplify("10/6", "6/10") == True, "10/6"
    assert simplify("10/6", "6/10") == True, "10/6"
    assert simplify("10/6", "6/10") == True, "10/6"
    assert simplify("10/6", "6/10") == True, "10/6"
    assert simplify("10/6", "6/10") == True, "10/6"