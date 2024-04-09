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

    
	Do not include these tokens in the code: if len ( oper and ) ==
	"""
    operator = operator
    operand = operand
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == "+":
            result = result + operand[i + 1]
        elif operator[i] == "-":
            result = result - operand[i + 1]
        elif operator[i] == "*":
            result = result * operand[i + 1]
        elif operator[i] == "//":
            result = result // operand[i + 1]
        elif operator[i] == "**":
            result = result ** operand[i + 1]

    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert do_algebra(["+", "+", "*"], [1, 2, 2, 2]) == 6, "First"
    assert do_algebra(["*", "*", "*"], [2, 2, 2, 2]) == 16, "Second"
    assert do_algebra(["*", "*", "*", "*"], [2, 2, 2, 2, 2]) == 32, "Third"
    assert do_algebra(["*", "/", "*", "/"], [1, 2, 2, 2, 2]) == 1, "Fourth"
    assert do_algebra(["+", "*", "*", "*", "+"], [1, 2, 2, 2, 2]) == 9, "Fifth"
    assert do_algebra(["+", "*", "*", "*", "+", "+"], [1, 2, 2, 2, 2, 2]) == 12, "Sixth"
    assert do_algebra(["+", "/", "*", "*", "+", "/"], [1, 2, 2, 2, 2, 2]) == 1, "Seventh"
    assert do_algebra(["+", "/", "*", "*", "+", "/", "*"], [