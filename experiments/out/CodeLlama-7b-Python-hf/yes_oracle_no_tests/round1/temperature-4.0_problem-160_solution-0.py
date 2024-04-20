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

    
	Include these tokens in the code: exp = "" for i in range (
	"""
    # Your code goes here
    exp = ""
    for i in range (len(operator)):
        exp += " " + str(operand[i]) + operator[i]
    exp += " " + str(operand[len(operand) - 1])
    return eval(exp)


if __name__ == '__main__':
    operator = ["+", "*", "-"]
    operand = [2, 3, 4, 5]
    print(do_algebra(operator, operand))