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

    """
    # 1. Remove the first element in operand and assign it as result
    # 2. Check if the length of operator is zero
    # 3. If the length of operator is zero, finish the loop
    # 4. Assign one operator from operator list to one_operator
    # 5. If one_operator is **, calculate the result of this operation using 
            # 5a. result **= operand[0]
    # 6. Else one_operator is + - * //, calculate the result of this operation using 
            # 6a. result = result one_operator operand[0]
    # 7. Pop the first element in operand list
    # 8. Repeat step 4~7 until the length of operator is zero
    # 9. Return result
    result = operand.pop(0)

    if len(operator) == 0:
        return result
    else:
        one_operator = operator.pop(0)
        if one_operator == "**":
            result **= operand[0]
        else:
            result = result one_operator operand[0]
        operand.pop(0)

        return do_algebra(operator, operand)




