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

    
	Do not include these tokens in the code: # First you need to check the
	"""
    # First you need to check the length of operator list is equal to the length of operand list minus one.
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator list length is not equal to operand list length minus one.")

    # Second, you need to check the operand is a list of non-negative integers.
    for num in operand:
        if num < 0:
            raise ValueError("Operand list must be a list of non-negative integers.")

    # Third, you need to check the length of operator list is not zero.
    if len(operator) == 0:
        raise ValueError("Operator list length is zero.")

    # Finally, you need to check the first element of operator list is '+'.
    if operator[0] != '+':
        raise ValueError("The first element of operator list must be '+'.")

    # Fourth, you need to check the last element of operand list is an integer.
    if type(operand[-1]) != int:
        raise ValueError("The last element of operand list must be an integer.")

    # Finally, you need to check the operator list has the same number of '+' and '-' tokens.
    if operator.count('+') != operator.count('-'):
        raise ValueError("The operator list must have the same number of '+' and '-' tokens.")

    # Finally, you need to check the operator list has the same number of '*' and '//' tokens.
    if operator.count('*') != operator.count('//'):
        raise ValueError("The operator list must have the same number of '*' and '//' tokens.")

    # Finally, you need to check the operator list has the same number of '**' tokens.
    if operator.count('**') != 1:
        raise ValueError("The operator list must have the same number of '**' tokens.")

    # Finally, you need to check the operator list has the same number of '*' and '//' tokens.
    if operator.count('**') != 1:
        raise ValueError("The operator list must have the