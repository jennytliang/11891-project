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
	"""
    exp = ""
    for i in range(0, len(operator)):
        exp += str(operand[i]) + operator[i]
    exp += str(operand[len(operand) - 1])
    return eval(exp)


if __name__ == '__main__':
    print("Example:")
    print(do_algebra(["+", "-", "*"], [2, 4, 10, 12]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert do_algebra(["+", "-", "*"], [2, 4, 10, 12]) == 26, "Add and Sub"
    assert do_algebra(["+", "*"], [2, 4, 10, 12]) == 34, "Add and Mul"
    assert do_algebra(["*", "/"], [2, 4, 10, 12]) == 2, "Mul and FloorDiv"
    assert do_algebra(["+", "-", "/"], [2, 4, 10, 12]) == 1, "Add, Sub and FloorDiv"
    assert do_algebra(["*", "/"], [2, 4, 10, 12]) == 2, "Mul and Div"
    assert do_algebra(["*", "/", "+"], [2, 4, 10, 12]) == 18, "Mul, Div and Add"
    assert do_algebra(["*", "/", "-"], [2, 4, 10, 12]) == 14, "Mul, Div and Sub"
    assert do_algebra(["*", "/", "+", "-"], [2, 4, 10, 12]) == 10, "Mul, Div, Add and Sub"
    assert do_algebra(["*", "/", "+", "-", "**"], [2, 4, 10, 12]) == 10, "Mul, Div, Add, Sub and Pow"
    assert