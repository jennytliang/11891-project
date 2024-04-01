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
    #operators = {"+", "-", "*", "//", "**"}
    #operands = {"2", "3", "4", "5"}
    #operators = {"+", "-", "*", "/", "^"}
    #operands = {"2", "3", "4", "5"}
    operators = operator
    operands = operand
    #print(operators, operands)
    def parse_operands(operands):
        #print(operands)
        if len(operands) == 1:
            return int(operands[0])
        else:
            return parse_operands(operands[1:])
    def parse_operators(operators):
        #print(operators)
        if len(operators) == 1:
            return operators[0]
        else:
            return parse_operators(operators[1:])
    def eval_exp(exp):
        #print(exp)
        if len(exp) == 1:
            return int(exp[0])
        else:
            op = parse_operators(exp[0])
            if op == "+":
                return eval_exp(exp[1:]) + eval_exp(exp[2:])
            elif op == "-":
                return eval_exp(exp[1:]) - eval_exp(exp[2:])
            elif op == "*":
                return eval_exp(exp[1:]) * eval_exp(exp[2:])
            elif op == "/":
                return eval_exp(exp[1:]) / eval_exp(exp[2:])
            elif op == "^":
                return eval_exp(exp[1:]) ** eval_exp(exp[2:])
            else:
                return "Error"
    #print(operands, operators)
    #print(eval_exp(operands))
    #print(eval_exp(operators))
    return eval_exp(operands)
