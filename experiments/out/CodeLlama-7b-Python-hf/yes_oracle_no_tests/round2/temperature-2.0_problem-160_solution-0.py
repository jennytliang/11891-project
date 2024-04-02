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

    
	Do not include these tokens in the code: # Oper and is a list of
	"""
    result = operand.pop(0)
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand.pop(0)
        elif operator[i] == '-':
            result -= operand.pop(0)
        elif operator[i] == '*':
            result *= operand.pop(0)
        elif operator[i] == '//':
            result //= operand.pop(0)
        elif operator[i] == '**':
            result **= operand.pop(0)
    return result


def test_function(test_case):
    operator = test_case[0]
    operand = test_case[1]
    solution = test_case[2]
    output = do_algebra(operator, operand)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


operator = ['+', '*', '*', '-', '//']
operand = [10, 6, 4, 20]
solution = 12
test_case = [operator, operand, solution]
test_function(test_case)

operator = ['+', '*', '*', '-', '//']
operand = [20, 15, 15, 18, 3]
solution = 147
test_case = [operator, operand, solution]
test_function(test_case)

operator = ['+', '*', '*', '-', '//']
operand = [10, 6, 4, 20, 10, 6, 4]
solution = 120
test_case = [operator, operand, solution]
test_function(test_case)
