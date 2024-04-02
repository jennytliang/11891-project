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
    # YOUR CODE GOES HERE
    # Use the following function to test your code
    # The function call should look something like:
    # do_algebra(operator, operand)
    #
    # operator = ['+', '*', '-']
    # operand = [2, 3, 4, 5]
    #
    # do_algebra(operator, operand)
    # => 9
    # 
    # operator = ['+', '*', '//', '**']
    # operand = [2, 3, 4, 5]
    #
    # do_algebra(operator, operand)
    # => 2
    #
    # operator = ['+', '*', '//', '**']
    # operand = [1, 2, 3, 4]
    #
    # do_algebra(operator, operand)
    # => 2
    #
    # operator = ['+', '*', '//', '**']
    # operand = [1, 2, 3, 4, 5]
    #
    # do_algebra(operator, operand)
    # => 2
    #
    # operator = ['+', '*', '//', '**']
    # operand = [1, 2, 3, 4, 5, 6, 7]
    #
    # do_algebra(operator, operand)
    # => 2
    #
    # operator = ['+', '*', '//', '**']
    # operand = [2, 3, 4, 5, 6, 7, 8]
    #
    # do_algebra(operator, operand)
    # => 2
    #
    # operator = ['+', '*', '//', '**']
    # operand = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #
    # do_algebra(operator, operand)
    # => 2


    # Write your code here
