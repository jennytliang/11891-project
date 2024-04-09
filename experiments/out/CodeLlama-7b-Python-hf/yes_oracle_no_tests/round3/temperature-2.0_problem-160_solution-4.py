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

    
	Include these tokens in the code: exp +=
	Do not include these tokens in the code: e =
	"""


    exp = ""
    for i in range(len(operator)):
 
        if i == 0:
            exp += str(operand[i]) + operator[i] + str(operand[i+1])
        else:
            exp += operator[i] + str(operand[i+1])
    return eval(exp)



def test_function(operator, operand, expected_result):
    result = do_algebra(operator, operand)
    if expected_result == result:
        print("Pass")
    else:
        print("Fail")


operator = ["+", "*", "-"]
operand = [2, 3, 4, 5]
expected_result = 9
test_function(operator, operand, expected_result)

operator = ["-", "*", "+"]
operand = [2, 3, 4, 5]
expected_result = 15
test_function(operator, operand, expected_result)

operator = ["*", "+", "+", "*"]
operand = [2, 3, 4, 5]
expected_result = 44
test_function(operator, operand, expected_result)

operator = ["+", "-", "*", "/"]
operand = [2, 3, 4, 5]
expected_result = 1
test_function(operator, operand, expected_result)

operator = ["*", "*", "*", "*", "*", "*"]
operand = [2, 3, 4, 5, 6, 7]
expected_result = 701408
test_function(operator, operand, expected_result)

operator = ["*", "*", "*", "*", "*", "*", "+"]
operand = [2, 3, 4, 5, 6, 7, 8]
expected_result = 701409
test_function(operator, operand, expected_result)

operator = ["*", "*", "*", "*", "*", "*", "*", "*", "*", "+"]
operand = [2, 3, 4, 5, 6, 7,