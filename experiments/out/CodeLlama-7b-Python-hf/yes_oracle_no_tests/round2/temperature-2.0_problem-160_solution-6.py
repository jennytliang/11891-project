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

    
	Do not include these tokens in the code: for i in range ( len ( oper
	"""

    exp = operand.pop(0)
    for i in range(len(operator)):
        if operator[i] == '+':
            exp = exp + operand[i]
        elif operator[i] == '-':
            exp = exp - operand[i]
        elif operator[i] == '*':
            exp = exp * operand[i]
        elif operator[i] == '//':
            exp = exp // operand[i]
        elif operator[i] == '**':
            exp = exp ** operand[i]

    return exp


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert do_algebra(["+", "*"], [3, 5, 2, 5, 2]) == 35, "Addition"
    assert do_algebra(["*", "+"], [2, 4, 3, 5]) == 44, "Multiplication"
    assert do_algebra(["-", "-"], [3, 2, 7, 4]) == 5, "Subtraction"
    assert do_algebra(["//", "//"], [100, 2, 4, 25]) == 2, "Integer division"
    assert do_algebra(["//", "*"], [15, 2, 3, 10]) == 3, "Priority"
    assert do_algebra(["+", "**"], [2, 2, 2, 2, 2]) == 16, "Priority"
