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
    for x in range(len(operator)):
        exp += operand[x] + operator[x]
    exp += str(operand[-1])
    return eval(exp)


# Do not edit this line.
tests = [
    [[], [2, 3, 4, 5], 9],
    [["*"], [2, 3, 4, 5], 24],
    [["*", "+"], [2, 3, 4, 5], 17],
    [["*", "+", "-"], [2, 3, 4, 5], 9],
    [["-", "+"], [2, 3, 4, 5], 3],
    [["-", "+", "**"], [2, 3, 4, 5], 2187],
    [["-", "+", "**", "//"], [2, 3, 4, 5], 21],
    [["-", "+", "**", "//", "*"], [2, 3, 4, 5], 24],
    [["-", "+", "**", "//", "*", "/"], [2, 3, 4, 5], 6],
    [["-", "+", "**", "//", "*", "/", "//"], [2, 3, 4, 5], 3],
    [["-", "+", "**", "//", "*", "/", "//", "**"], [2, 3, 4, 5], 27],
]


if __name__ == "__main__":
    for tokens, operand, result in tests:
        assert do_algebra(tokens, operand) == result
