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
    # your code
    exp_str = "exp = "
    for ind, opt in enumerate(operator):
        opt_str = ""
        opt_str += "exp" if ind == 0 else "exp "
        opt_str += f"{operator[ind]} {operand[ind+1]} " if len(operator)-ind > 1 else opt
        eval(f"exp {opt}={operand[ind+1]} if len(operand)-ind > 1 else exp")
    return eval(exp)



operator = ["+", "-"]
operand = [1, 2, 3, 4, 5]
print(do_algebra(operator, operand))