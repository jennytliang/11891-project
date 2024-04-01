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

    
	Do not include these tokens in the code: # Write your code here
	"""
    if len(operator) != len(operand) - 1:
        raise ValueError('Invalid input')

    def eval_expression(operator, operand):
        if len(operator) == 0:
            return operand
        else:
            return eval_expression(operator[1:], [eval(f'{operand[0]} {operator[0]} {operand[1]}')])

    return eval_expression(operator, operand)


if __name__ == '__main__':
    do_algebra(['*', '+'], [3, 4, 5])
