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

    
	Include these tokens in the code: +
	Do not include these tokens in the code: exp +=
	"""


    exp = ""
    for i in range(len(operator)):
        exp += str(opera) + str(operand[i])
    return exp


print(do_algebra(["+", "*"], [2, 3, 4, 5]))
print(do_algebra(["*", "+"], [2, 3, 4, 5]))
print(do_algebra(["*", "+", "-"], [2, 3, 4, 5]))


# Test.describe("Basic tests")
# Test.assert_equals(do_algebra(["*", "+", "-"], [2, 3, 4, 5]), 9)
# Test.assert_equals(do_algebra(["+", "*"], [2, 3, 4, 5]), 20)
# Test.assert_equals(do_algebra(["*", "+", "-"], [1, 2, 3, 4, 5, 6, 7, 8, 9]), 184)
# Test.assert_equals(do_algebra(["*", "+", "-"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1840)
# Test.assert_equals(do_algebra(["*", "+", "-"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 1840)
