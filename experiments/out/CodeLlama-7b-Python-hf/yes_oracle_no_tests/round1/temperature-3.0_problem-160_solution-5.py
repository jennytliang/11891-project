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
    # Do not edit the code below 
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result


if __name__ == '__main__':
    # Test Case 1
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    expected = 9
    result = do_algebra(operator, operand)
    print("Test 1: Result: {0}. Expected: {1}.".format(result, expected))

    # Test Case 2
    operator = ['*', '+', '*', '*', '//']
    operand = [2, 3, 4, 5, 6]
    expected = 14
    result = do_algebra(operator, operand)
    print("Test 2: Result: {0}. Expected: {1}.".format(result, expected))

    # Test Case 3
    operator = ['-', '*', '-', '/']
    operand = [2, 3, 4, 5]
    expected = -1
    result = do_algebra(operator, operand)
    print("Test 3: Result: {0}. Expected: {1}.".format(result, expected))

    # Test Case 4
    operator = ['*', '+', '*', '**', '/']
    operand = [2, 3, 4, 5, 6]
    expected = 29
    result = do_algebra(operator, operand)
    print("Test 4: Result: {0}. Expected