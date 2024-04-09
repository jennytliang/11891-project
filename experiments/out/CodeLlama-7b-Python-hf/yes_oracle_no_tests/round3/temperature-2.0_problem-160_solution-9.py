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
	Do not include these tokens in the code: ex ps
	"""
    
    # your code here
    # print(operator, operand)
    # print(operator[0], operand[0], operator[1], operand[1])
    # print(operator[0], operand[0], operator[1], operand[1], operator[2], operand[2])
    # print(operator[0], operand[0], operator[1], operand[1], operator[2], operand[2], operator[3], operand[3])
    if len(operator) == 1:
        return eval(str(operand[0]) + operator[0] + str(operand[1]))
    elif len(operator) == 2:
        return eval(str(operand[0]) + operator[0] + str(operand[1]) + operator[1] + str(operand[2]))
    elif len(operator) == 3:
        return eval(str(operand[0]) + operator[0] + str(operand[1]) + operator[1] + str(operand[2]) + operator[2] + str(operand[3]))
    elif len(operator) == 4:
        return eval(str(operand[0]) + operator[0] + str(operand[1]) + operator[1] + str(operand[2]) + operator[2] + str(operand[3]) + operator[3] + str(operand[4]))
    else:
        return 'Invalid operator length'



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert do_algebra(["+", "+", "+", "+"], [1, 2, 3, 4]) == 10, "First"
    assert do_algebra(["-", "-", "-", "-"], [1, 2, 3, 4]) == -10, "Second"
    assert do_algebra(["*", "*", "*", "*"], [1, 2, 3, 4]) == 24, "Third"
    assert do_algebra(