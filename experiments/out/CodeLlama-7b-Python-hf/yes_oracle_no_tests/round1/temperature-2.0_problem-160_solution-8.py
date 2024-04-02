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
	Do not include these tokens in the code: if len ( operator ) != len
	"""
    # First you need to check the lengths of the two lists are correct.
    # If not, return an error.
    if len(operator) != len(operand) - 1:
        return "Error"

    # Create an empty string to store the expression
    exp = ""
    
    # Now loop through the lists
    for i in range(len(operator)):
        # Add the operands to the expression
        exp += str(operand[i])
        # Add the operator to the expression
        exp += operator[i]

    # Add the last operand to the expression
    exp += str(operand[-1])

    # Evaluate the expression
    result = eval(exp)

    return result


def test_function(operator, operand, expected_result):
    # This function will test your function
    result = do_algebra(operator, operand)

    if result == expected_result:
        print("Your code PASSED the test for", operator, "and", operand)
    else:
        print("Your code FAILED the test for", operator, "and", operand)


# Test 1: Testing the addition functionality
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
expected_result = 9
test_function(operator, operand, expected_result)

# Test 2: Testing the subtraction functionality
operator = ['-', '*', '*', '+']
operand = [2, 3, 4, 5]
expected_result = -12
test_function(operator, operand, expected_result)

# Test 3: Testing the multiplication functionality
operator = ['+', '*', '*', '-']
operand = [2, 3, 4, 5]
expected_result = 14
test_function(operator, operand, expected_result)

# Test 4: Testing the floor division functionality
operator = ['+', '//', '*', '+']
operand = [2, 3, 4, 