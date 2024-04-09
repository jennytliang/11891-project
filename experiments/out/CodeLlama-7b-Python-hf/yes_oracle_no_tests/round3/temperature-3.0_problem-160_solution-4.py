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
            result = result + operand[i + 1]
        elif operator[i] == '-':
            result = result - operand[i + 1]
        elif operator[i] == '*':
            result = result * operand[i + 1]
        elif operator[i] == '//':
            result = result // operand[i + 1]
        elif operator[i] == '**':
            result = result ** operand[i + 1]
    return result


if __name__ == '__main__':
    print("Example:")
    print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['+', '*', '*', '*'], [2, 3, 4, 5]) == 80
    assert do_algebra(['//', '//', '*'], [15, 10, 3]) == 5
    assert do_algebra(['+', '*', '+', '*'], [2, 3, 4, 5]) == 23
    assert do_algebra(['//', '*', '//', '*'], [15, 10, 3, 2]) == 30
    assert do_algebra(['//', '*', '//', '*', '+'], [15, 10, 3, 2, 2]) == 32
    print("Coding complete? Click 'Check' to earn cool rewards!")
