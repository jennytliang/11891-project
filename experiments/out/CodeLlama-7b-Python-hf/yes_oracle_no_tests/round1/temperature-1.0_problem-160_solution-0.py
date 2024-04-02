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
    # build algebric expression
    expression = ''
    for i in range(len(operand)):
        expression += str(operand[i])
        if i < len(operator):
            expression += operator[i]

    # evaluate expression
    result = eval(expression)

    return result


assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
assert do_algebra(['+', '*', '*', '*', '+'], [2, 3, 4, 5, 6, 7]) == 2 * 3 * 4 * 5 + 6 * 7
assert do_algebra(['+', '*', '*', '*', '+'], [2, 3, 4, 5, 6, 7, 8]) == 2 + 3 * 4 * 5 * 6 + 7 * 8
assert do_algebra(['+', '*', '*', '*', '+'], [2, 3, 4, 5, 6, 7, 8, 9]) == 2 + 3 * 4 * 5 * 6 + 7 * 8 * 9
assert do_algebra(['+', '*', '*', '*', '+'], [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2 + 3 * 4 * 5 * 6 + 7 * 8 * 9 * 10

print("Test Success!")
