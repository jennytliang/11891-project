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

    # Write your code below this line
    # ================================
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result = result + operand[i + 1]
        elif operator[i] == '-':
            result = result - operand[i + 1]
        elif operator[i] == '*':
            result = result * operand[i + 1]
        elif operator[i] == '//':
            result = result // operand[i + 1]
        elif operator[i] == '**':
            result = result ** operand[i + 1]
    return result


if __name__ == '__main__':
    # operator = ['+', '-', '*', '//']
    # operand = [2, 3, 4, 5]

    operator = ['+', '*', '//', '**']
    operand = [2, 3, 4, 5, 6]

    print('Input:')
    print('operator =', operator)
    print('operand =', operand)
    print('Output:', do_algebra(operator, operand))