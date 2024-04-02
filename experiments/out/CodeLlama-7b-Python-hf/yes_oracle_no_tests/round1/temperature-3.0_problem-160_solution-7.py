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
	Do not include these tokens in the code: result
	"""
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert do_algebra(["+", "**", "*"], [2, 3, 2, 5]) == 2 ** 2 * 2 * 5, "Add"
    assert do_algebra(["*", "--", "*"], [3, 2, 2, 5]) == 3 * (2 - 2) * 5, "Ooo"
    assert do_algebra(["-", "+"], [1, 2]) == -1 + 2, "Simple"
    assert do_algebra(["+", "-", "*"], [2, 2, 2, 5]) == 2 + 2 - 2 * 5, "Hard"
    assert do_algebra(["-", "-"], [1, 1, 2]) == -(1 - 1 - 2), "Triple minus"
    assert do_algebra(["+", "+", "+", "+", "-", "-"], [1, 2, 3, 4, 5, 6]) == 1 + 2 + 3 + 4 - 5 - 6, "Long"
