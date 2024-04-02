def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    
	Include these tokens in the code: i
	Do not include these tokens in the code: x
	"""

    exp = ""
  
    for i in range(len(operator)):
        exp += str(operand[i]) + operator[i]
    exp += str(operand[len(operand) - 1])

    return eval(exp)


# These are given to you, do not modify:

def test(operator, operand, expected):
    """
    Given an operator, operand, and expected result, this function tests do_algebra
    to ensure it is working properly.
    """
    result = do_algebra(operator, operand)

    if expected == result:
        print("PASSED test")
    else:
        print("FAILED test, expected", expected, "but got", result, "instead")


test(["+"], [2, 3], 5)
test(["+", "-"], [2, 3, 4], 5)
test(["+", "-", "*"], [2, 3, 4, 5], 5)
test(["-", "+", "*"], [2, 3, 4, 5], 5)
test(["-", "+", "*", "/"], [2, 3, 4, 5, 6], 5)
test(["-", "+", "*", "/", "//"], [2, 3, 4, 5, 6, 7], 5)
test(["-", "+", "*", "/", "//", "%"], [2, 3, 4, 5, 6, 7, 8], 5)
test(["-", "+", "*", "/", "//", "%", "**"], [2, 3, 4, 5, 6, 7, 8, 9], 5)
test(["-", "+", "*", "/", "//", "%", "**", "**"], [2, 3, 4, 5, 6, 7, 8, 9, 10], 5)


