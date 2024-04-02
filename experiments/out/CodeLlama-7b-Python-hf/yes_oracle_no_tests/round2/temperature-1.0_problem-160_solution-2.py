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

    
	Do not include these tokens in the code: # do not modify this variable
	"""
    def build_tree(operator, operand):
        if len(operator) == 0:
            return operand[0]
        else:
            return [operator[0], build_tree(operator[1:], operand[:-1]), build_tree(operator[1:], operand[-1:])]
    return eval(str(build_tree(operator, operand)))


print(do_algebra(["+", "*", "-"], [2, 3, 4, 5]))
print(do_algebra(["+", "*", "-", "/"], [2, 3, 4, 5]))
print(do_algebra(["+", "*", "-", "/", "**"], [2, 3, 4, 5]))