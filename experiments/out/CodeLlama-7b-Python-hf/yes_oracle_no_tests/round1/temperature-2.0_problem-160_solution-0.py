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
    # Operand is a list of of non-negative integers.
    # Operator list has at least one operator, and operand list has at least two operands.
    # The length of operator list is equal to the length of operand list minus one.
    exp = ""
    for i in range(len(operator)):
        exp += str(operand[i]) + " " + operator[i] + " "
    exp = exp[:-3]
    return eval(exp)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert do_algebra(["*", "+"], [1, 2, 3]) == 6, "Multiplication"
    assert do_algebra(["*", "+", "-"], [1, 2, 3, 4]) == 6, "Multiplication and Subtraction"
    assert do_algebra(["/", "//", "/"], [1, 2, 3, 4]) == 0, "Floor division"
    assert do_algebra(["//", "/", "*"], [1, 2, 3, 4]) == 0, "Floor division and Multiplication"
    assert do_algebra(["*", "//", "*"], [1, 2, 3, 4]) == 6, "Multiplication and Floor division"
    assert do_algebra(["*", "*", "*", "*", "/"], [1, 2, 3, 4, 5]) == 120, "Multiplication and exponentiation"
    assert do_algebra(["//", "*", "*", "*"], [1, 2, 3, 4]) == 0, "Floor division and Multiplication"
    assert do_algebra(["*", "/", "*", "*"], [1, 2, 3, 4]) == 24, "Multiplication, Floor division and Multiplication"
    assert do_algebra(["*", "*", "*", "*", "*"], [1, 2, 3, 4, 5]) == 