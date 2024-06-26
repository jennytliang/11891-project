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
    exp = ""
    for i in range(len(operator)):
        exp += str(operand[i]) + operator[i]
    exp += str(operand[len(operand) - 1])
    return eval(exp)


def test_do_algebra():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['-', '*', '+'], [2, 3, 4, 5]) == -7
    assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 11
    assert do_algebra(['*', '*', '-'], [2, 3, 4, 5]) == 20
    assert do_algebra(['*', '*', '-'], [1, 2, 3, 4]) == -12
    assert do_algebra(['+', '*', '+', '*', '+', '-'], [2, 3, 4, 5, 6, 7]) == 16
    assert do_algebra(['-', '*', '+', '*', '+', '-'], [2, 3, 4, 5, 6, 7]) == -16
    assert do_algebra(['*', '*', '-', '*', '+', '+'], [2, 3, 4, 5, 6, 7]) == 48
    assert do_algebra(['*', '*', '-', '*', '+', '+'], [1, 2, 3, 4, 5, 6]) == -24
    assert do_algebra(['-', '*', '+', '*', '+', '-'], [1, 2, 3, 4, 5, 6]) == -26
    assert do_algebra(['*', '*', '-', '*', '+', '+'], [1, 2, 3, 4, 5, 6]) == 48
    assert do_algebra(['-', '*', '+',