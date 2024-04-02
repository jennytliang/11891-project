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
    return eval(f"{operand[0]} {operator[0]} {operand[1]}")


if __name__ == '__main__':
    test_cases = [
        (['+', '*', '-'], [2, 3, 4, 5], 9),
        (['+', '*', '-'], [1, 2, 3, 4, 5], 12),
        (['+', '*', '-'], [1, 2, 3, 4, 5, 6], 18),
        (['+', '*', '-'], [1, 2, 3, 4, 5, 6, 7], 25),
        (['+', '*', '-'], [1, 2, 3, 4, 5, 6, 7, 8], 36),
        (['+', '*', '-'], [1, 2, 3, 4, 5, 6, 7, 8, 9], 49),
    ]

    for operator, operand, expected in test_cases:
        result = do_algebra(operator, operand)
        assert result == expected, f'Expected {expected}, got {result}'

    print('OK!')
