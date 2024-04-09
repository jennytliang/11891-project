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
	Do not include these tokens in the code: e
	"""


    exp = ""
    for i in range(len(operator)):
        exp += str(operand[i]) + operator[i]
    exp += str(operand[-1])
    return eval(exp)


if __name__ == '__main__':
    # Test 1
    print('Test 1')
    print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))

    # Test 2
    print('Test 2')
    print(do_algebra(['+', '*', '+', '*', '*'], [2, 3, 4, 5, 6]))

    # Test 3
    print('Test 3')
    print(do_algebra(['*', '*', '*', '*', '*', '*', '*'], [2, 3, 4, 5, 6, 7, 8]))

    # Test 4
    print('Test 4')
    print(do_algebra(['+', '*', '+', '*', '*', '+', '*', '+', '*', '*'], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

    # Test 5
    print('Test 5')
    print(do_algebra(['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '*', '*', '*', '*', '*', '*', '*', '*', '*'], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]))

    # Test 6
    print('Test 6')
    print(do_algebra(['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*',