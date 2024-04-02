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

    
	Include these tokens in the code: exp
	Do not include these tokens in the code: result
	"""
    # do not modify this variable
    # exp = []
    exp = []
    for i in range(len(operator)):
        exp.append(operand[i])
        exp.append(operator[i])
    exp.append(operand[-1])
    return eval(str(exp).replace("'", ""))


def test_function(test_case):
    test_input, test_operator, test_operand = test_case
    if do_algebra(test_operator, test_operand) == test_input:
        print("Pass")
    else:
        print("Fail")


test_function((4, ['+', '*', '+'], [2, 3, 4]))
test_function((15, ['+', '*', '+', '*'], [2, 3, 4, 5]))
test_function((15, ['+', '*', '+', '*'], [2, 3, 4, 5]))
test_function((9, ['-', '*', '*', '+'], [2, 3, 4, 5]))
test_function((16, ['*', '+', '*', '+'], [2, 3, 4, 5]))
test_function((32, ['*', '+', '*', '*'], [2, 3, 4, 5]))
test_function((32, ['*', '+', '*', '*'], [2, 3, 4, 5]))
test_function((4, ['+', '+', '+', '+'], [2, 3, 4, 5]))
test_function((4, ['+', '+', '+', '+'], [2, 3, 4, 5]))
test_function((4, ['+', '+', '+', '+'], [2, 3, 4, 5]))
test_function((4, ['+', '+', '+', '+'], [2, 3, 4, 5]))
test_function((25, ['*', '*', '