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

    
	Do not include these tokens in the code: if len ( operator ) != ( len
	"""


    exps = list(zip(operator, operand))
    for exp in exps:
        if exp[0] == '+':
            operand[operand.index(exp[1])] = exp[1] + exp[1]
        elif exp[0] == '-':
            operand[operand.index(exp[1])] = exp[1] - exp[1]
        elif exp[0] == '*':
            operand[operand.index(exp[1])] = exp[1] * exp[1]
        elif exp[0] == '//':
            operand[operand.index(exp[1])] = exp[1] // exp[1]
        elif exp[0] == '**':
            operand[operand.index(exp[1])] = exp[1] ** exp[1]
    
    return sum(operand)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert do_algebra(["+", "+", "*"], [1, 2, 3]) == 7, "First"
    assert do_algebra(["+", "*", "+"], [1, 2, 3]) == 9, "Second"
    assert do_algebra(["-", "*", "-"], [4, 2, 2]) == 4, "Third"
    assert do_algebra(["*", "*", "*"], [1, 2, 3]) == 6, "Fourth"
    assert do_algebra(["*", "*", "*"], [1, 2, 1]) == 2, "Fifth"
    assert do_algebra(["-", "-", "*"], [4, 2, 2]) == 0, "Sixth"
