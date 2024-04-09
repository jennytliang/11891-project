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
    # Your code here
    #print(operator, operand)
    #print(len(operator), len(operand))
    exp = str(operand.pop(0))
    for i in range(len(operator)):
        exp += operator[i] + str(operand[i])
    return eval(exp)


def test_function(operator, operand, expected_result):
    result = do_algebra(operator, operand)
    if result == expected_result:
        print("Pass")
    else:
        print("Fail")


operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
expected_result = 9
test_function(operator, operand, expected_result)

operator = ['*', '*', '+']
operand = [2, 3, 4, 5]
expected_result = 44
test_function(operator, operand, expected_result)

operator = ['*', '*', '*', '+']
operand = [2, 3, 4, 5]
expected_result = 120
test_function(operator, operand, expected_result)

operator = ['*', '*', '*', '*', '+']
operand = [2, 3, 4, 5]
expected_result = 360
test_function(operator, operand, expected_result)

operator = ['*', '*', '*', '*', '*', '+']
operand = [2, 3, 4, 5]
expected_result = 720
test_function(operator, operand, expected_result)

operator = ['+', '*', '*', '*', '*', '+']
operand = [2, 3, 4, 5]
expected_result = 25
test_function(operator, operand, expected_result)

operator = ['+', '*', '*', '*', '*', '+', '*']
operand = [2, 3