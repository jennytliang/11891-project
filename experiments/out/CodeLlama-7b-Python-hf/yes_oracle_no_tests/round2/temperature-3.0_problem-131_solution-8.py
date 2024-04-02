def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    return 0




def test(did_pass):
    """  This function prints the result of a test.  """
    linenum = "."
    if did_pass:
        print(linenum, "PASSED")
    else:
        print(linenum, "FAILED")


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    # test case 1
    expected = 1
    actual = digits(1)
    test(expected == actual)
    # test case 2
    expected = 0
    actual = digits(4)
    test(expected == actual)
    # test case 3
    expected = 15
    actual = digits(235)
    test(expected == actual)
    # test case 4
    expected = 0
    actual = digits(0)
    test(expected == actual)
    # test case 5
    expected = 120
    actual = digits(120)
    test(expected == actual)
    # test case 6
    expected = 144
    actual = digits(144)
    test(expected == actual)


test_suite()  # Here is the call to run the tests
