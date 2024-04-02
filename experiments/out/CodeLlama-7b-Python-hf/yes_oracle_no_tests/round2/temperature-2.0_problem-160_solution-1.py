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

    
	Include these tokens in the code: str ( oper
	"""

    exp = ""
    for i in range(len(operator)):
        e = operand[i]
        for j in range(len(operator)):
            if i == j:
                continue
            if operator[j] == '+':
                e += " + "
            elif operator[j] == '-':
                e += " - "
            elif operator[j] == '*':
                e += " * "
            elif operator[j] == '//':
                e += " // "
            elif operator[j] == '**':
                e += " ** "
        exp += str(e)
    return eval(exp)


print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))
print(do_algebra(['**', '*', '/', '+'], [2, 3, 4, 5]))
print(do_algebra(['+', '*', '*', '+', '/', '**'], [2, 3, 4, 5, 6, 7]))
