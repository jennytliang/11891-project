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

    
	Include these tokens in the code: exp = ""
	Do not include these tokens in the code: if len ( operator ) != len
	"""

    exp = ""
    if len(operator) != (len(operand) - 1):
        return "Invalid input"

    for i in range(len(operator)):
        if operator[i] == "+":
            exp = exp + str(operand[i]) + " + "
        elif operator[i] == "-":
            exp = exp + str(operand[i]) + " - "
        elif operator[i] == "*":
            exp = exp + str(operand[i]) + " * "
        elif operator[i] == "//":
            exp = exp + str(operand[i]) + " // "
        elif operator[i] == "**":
            exp = exp + str(operand[i]) + " ** "

    exp = exp[:-3]
    return eval(exp)


print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
print(do_algebra(['+', '*', '//', '**'], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
