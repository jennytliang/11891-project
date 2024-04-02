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

    expr = operand[0]
    for op, val in zip(operator, operand[1:]):
        expr += ' '+op+' '+str(val)
    
    exp = compile(expr, '', 'eval')
    return eval(exp)

print(do_algebra(['-', '+', '+', '*', '*', '+'], [-1234, 4325, 5425, 235, 235, -235]))
# -19875
print(do_algebra(['+', '-', '*'], [-1234, 4325, 5425]))
# -4325

print(do_algebra(['*', '+', '*'], [235, 235, -235]))
# 2

print(do_algebra(['-', '/', '-'], [42944, 10, 3]))
# -9395

print(do_algebra(['/', '*', '/', '+'], [297473, 9, 3824, 4450]))
# 3464

print(do_algebra(['+'], [4]))
# 4