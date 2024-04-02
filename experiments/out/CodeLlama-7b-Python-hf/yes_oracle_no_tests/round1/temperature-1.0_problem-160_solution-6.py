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
    # your code here

    def build_expression(operator, operand):
        if len(operator) == 1:
            return "[%s] * %s [exp]" % (operator, operand[0])
            #return "[%d] * %s [exp]" % (operator, operand[0])
        else:
            return "[%s] * %s [%s] * %s [exp]" % (
                operator[0],
                operand[0],
                operator[1],
                operand[1],
            )

    return eval(build_expression(operator, operand))

