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

    # Base case:
    if len(operator) == 0:
        return operand[-1]

    # Recursion case:
    else:
        # Add the first element of the operand list and call the function again
        if operator[0] == '+':
            return do_algebra(operator[1:], [operand[0] + operand[1]])

        # Subtract the first element of the operand list and call the function again
        elif operator[0] == '-':
            return do_algebra(operator[1:], [operand[0] - operand[1]])

        # Multiply the first element of the operand list and call the function again
        elif operator[0] == '*':
            return do_algebra(operator[1:], [operand[0] * operand[1]])

        # Divide the first element of the operand list and call the function again
        elif operator[0] == '//':
            return do_algebra(operator[1:], [operand[0] // operand[1]])

        # Exponentiate the first element of the operand list and call the function again
        elif operator[0] == '**':
            return do_algebra(operator[1:], [operand[0] ** operand[1]])































































































































































































