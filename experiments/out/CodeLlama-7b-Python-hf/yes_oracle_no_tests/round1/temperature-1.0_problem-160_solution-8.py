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
    def get_operator(expr):
        return list(map(int, expr.split()))
    def do_algebra(operator, operand):
        assert len(operator) == len(operand)-1, 'Operator count {} not matches operand {}'.format(len(operator),len(operand)-1)
        my_exp = operand[0]
        for i in range(len(operator)):
            curr_operator = operator[i]
            curr_item = operand[i+1]
            #print(i , curr_operator , curr_item)
            if curr_operator == 1:
                my_exp = my_exp + curr_item
            if curr_operator == 2:
                my_exp = my_exp * curr_item
            if curr_operator == 3:
                my_exp = my_exp - curr_item
            if curr_operator == 4:
                my_exp = my_exp / curr_item
            if curr_operator == 5:
                my_exp = my_exp / curr_item
        return my_exp
    return do_algebra(get_operator(operator), operand)

#######################

    
operator = ['+', '-', '$', '*', '+', '-', '+']
operand = [1, 2, 3]




print('\noperator = ',operator)
print('operand = ',operand)
print('result = {}'.format(do_algebra(operator, operand)))