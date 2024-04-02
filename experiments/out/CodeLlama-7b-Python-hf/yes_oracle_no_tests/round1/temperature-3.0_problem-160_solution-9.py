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
    result = int(operand[0])
    for i in range(len(operator)):
        if operator[i] == '+':
            result += int(operand[i+1])
        elif operator[i] == '-':
            result -= int(operand[i+1])
        elif operator[i] == '*':
            result *= int(operand[i+1])
        elif operator[i] == '//':
            result //= int(operand[i+1])
        elif operator[i] == '**':
            result **= int(operand[i+1])
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert do_algebra(["+", "-", "+"], [2, 4, 2, 4]) == 4, "Test 1"
    assert do_algebra(["*", "+", "-", "+", "**"], [2, 4, 3, 5, 2]) == 24, "Test 2"
    assert do_algebra(["*", "//", "+"], [1, 2, 4]) == 1, "Test 3"
    assert do_algebra(["*", "//", "+"], [1, 3, 5]) == 1, "Test 4"
    assert do_algebra(["*", "//", "+"], [1, 5, 2]) == 2, "Test 5"
    assert do_algebra(["*", "//", "+"], [1, 5, 3]) == 1, "Test 6"
    assert do_algebra(["*", "//", "+"], [1, 5, 5]) == 0, "Test 7"
