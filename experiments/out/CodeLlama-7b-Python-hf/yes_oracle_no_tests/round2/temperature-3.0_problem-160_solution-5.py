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
	Do not include these tokens in the code: # Do not edit the code below
	"""
    # Do not edit the code below
    exp = str(operand[0])

    for i in range(len(operator)):
        if operator[i] == '+':
            exp += " + " + str(operand[i+1])
        elif operator[i] == '-':
            exp += " - " + str(operand[i+1])
        elif operator[i] == '*':
            exp += " * " + str(operand[i+1])
        elif operator[i] == '//':
            exp += " // " + str(operand[i+1])
        elif operator[i] == '**':
            exp += " ** " + str(operand[i+1])
    return eval(exp)

if __name__ == '__main__':
    # Test your code
    # Do not edit the code below
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    print("Example:")
    print(do_algebra(operator, operand))

    # Do not remove the next line
    # grader.py: 2.1038888888888887
