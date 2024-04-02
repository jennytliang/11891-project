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
    # Your code goes here
    
    l = len(operand)
    final_exp = do_algo(operator, operand, l, '')
    
    return eval(final_exp)


def do_algo(operator, operand, l, exp):
    start = 0
    end = l

    if l == 1:
        return str(operand[0])
    
    for op in operator:
        for i in range(start, end):
            if op == "+" and end != 1:
                exp = do_algo(operator[start:i+1], operand[start:i+1], l-start, exp) + operate(operand[i], operand[i+1], op)
                return do_algo(operator[i+1:], operand[i+1:], l-i-1, exp)
            
            elif op == "-" and end != 1:
                exp = do_algo(operator[start:i+1], operand[start:i+1], l-start, exp) - operate(operand[i], operand[i+1], op)
                return do_algo(operator[i+1:], operand[i+1:], l-i-1, exp)
            
            elif op == "*" and end != 1:
                exp = do_algo(operator[start:i+1], operand[start:i+1], l-start, exp) * operate(operand[i], operand[i+1], op)
                return do_algo(operator[i+1:], operand[i+1:], l-i-1, exp)

            elif op == "//" and end != 1:
                exp = do_algo(operator[start:i+1], operand[start:i+1], l-start, exp) // operate(operand[i], operand[i+1], op)
                return do_algo(operator[i+1:], operand[i+1:], l-i-1, exp)

            elif op == "