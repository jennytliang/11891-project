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
    exp = str(operand.pop(0))
    tokens_lookup = {'+': operator.index("+"), '-': operator.index("-"), '*': operator.index("*"), '/': operator.index("//"), '**': operator.index("**")}
    tokens = list(exp)
    for i, op in enumerate(operator):
        token_list = tokens[:tokens_lookup[op]+i] + [f'((op[i]),'] + tokens[tokens_lookup[op]+i+1:]
        tokens = token_list
        exp += f" {op} "
    exp += tokens[-1]
    try:
        return eval(exp)
    except SyntaxError:
        return SyntaxError