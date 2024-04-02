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



import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match


def check(candidate):
    inputs = [[['**', '*', '+'], [2, 3, 4, 5]], [['+', '*', '-'], [2, 3, 4, 5]], [['//', '*'], [7, 3, 4]], [['+', '-', '*', '//'], [5, 2, 3, 4, 7]], [['**', '-', '//'], [9, 2, 5, 3]], [['*', '-', '*', '//'], [3, 6, 2, 4, 2]], [['-', '//', '+', '*'], [10, 2, 4, 3, 6]], [['+', '-', '*', '**'], [2, 3, 4, 5, 2]], [['*', '+', '-'], [1, 2, 3, 4]], [['-', '+', '*', '**'], [5, 4, 3, 2, 1]], [['*', '//', '-'], [10, 5, 3, 2]], [['**', '+', '-'], [3, 2, 1, 4]], [['*', '+', '//'], [2, 5, 3, 8]], [['-', '+', '*', '**'], [5, 3, 3, 2, 1]], [['*', '-', '*'], [10, 5, 3, 2]], [['-', '//', '-'], [10, 5, 3, 2]], [['*', '*', '-'], [10, 5, 3, 2]], [['-', '+', '*', '**'], [5, 3, 3, 2, 2]], [['*', '*', '-'], [9, 10, 3, 2]], [['*', '-', '*', '//'], [2, 6, 2, 4, 2]], [['+', '-', '*', '*'], [2, 3, 4, 5, 2]], [['*', '+', '//'], [2, 3, 8, 5]], [['-', '//', '+', '*'], [9, 2, 4, 3, 6]], [['*', '+', '//'], [2, 5, 4, 8]], [['*', '-', '**'], [10, 5, 3, 2]], [['-', '+', '*', '**'], [5, 3, 2, 2, 2]], [['-', '//', '+'], [10, 2, 4, 3]], [['*', '//', '//'], [2, 5, 8, 5]], [['-', '//', '-'], [10, 2, 3, 2]], [['*', '//'], [2, 5, 5]], [['-', '+', '**', '**'], [5, 3, 3, 2, 2]], [['**', '**', '//'], [9, 2, 5, 3]], [['*', '-', '*', '//'], [2, 6, 2, 3, 2]], [['*', '//', '+'], [2, 5, 8, 5]], [['-', '+', '*', '**'], [5, 4, 3, 2, 2]], [['//', '//', '+'], [2, 4, 3, 4]], [['+', '//', '//'], [2, 5, 4, 8]], [['**', '//', '//'], [2, 5, 4, 8]], [['**', '+', '//'], [2, 5, 4, 8]], [['*', '//', '//'], [2, 3, 8, 5]], [['-', '//', '+', '*', '*'], [10, 2, 4, 2, 6, 2]], [['*', '-', '*', '*'], [10, 5, 3, 2, 5]], [['**', '+', '-'], [3, 2, 0, 4]], [['-', '+', '*', '**'], [5, 5, 3, 2, 2]], [['-', '//', '+', '*', '*'], [10, 2, 4, 2, 5, 2]], [['**', '**', '//'], [9, 2, 5, 4]], [['-', '-', '+', '*', '*'], [10, 2, 4, 2, 5, 2]], [['*', '*', '-'], [10, 4, 3, 2]], [['-', '+', '*', '**'], [8, 4, 2, 2, 2]], [['+', '//', '*', '**'], [2, 3, 4, 5, 2]], [['//', '+', '//'], [2, 4, 3, 4]], [['-', '+', '-', '**'], [5, 4, 3, 2, 1]], [['-', '+', '**', '**'], [5, 5, 3, 2, 2]], [['-', '+', '**'], [5, 3, 3, 2]], [['+', '-', '*', '**'], [8, 3, 4, 5, 2]], [['+', '//', '*', '**'], [2, 3, 3, 5, 2]], [['-', '+', '-', '**', '**'], [5, 4, 3, 2, 1, 5]], [['-', '//', '+', '*', '*'], [10, 2, 4, 3, 5, 2]], [['-', '+', '*', '**', '*'], [5, 3, 2, 2, 2, 2]], [['**', '**', '//'], [9, 2, 6, 4]], [['//', '+', '//'], [1, 4, 3, 4]], [['+', '-', '*', '**', '+'], [2, 2, 3, 4, 5, 2]], [['*', '*', '-'], [10, 5, 10, 2]], [['-', '//', '-'], [2, 3, 6, 2]], [['-', '+', '**', '**'], [5, 3, 3, 2, 1]], [['+', '+', '//'], [6, 4, 3, 8]], [['//', '+', '//'], [8, 4, 3, 4]], [['**', '//'], [9, 5, 4]], [['**', '+', '-'], [4, 2, 0, 4]], [['*', '-', '**'], [10, 5, 2, 6]], [['-', '+', '**'], [10, 3, 3, 2]], [['**', '+', '//'], [8, 5, 4, 8]], [['**', '+', '-'], [2, 2, 2, 4]], [['*', '**', '//', '-'], [10, 5, 3, 3, 2]], [['-', '//', '+', '//', '*', '*'], [10, 2, 4, 3, 5, 2, 4]], [['**', '+', '-'], [0, 2, 1, 4]], [['-', '//', '-'], [1, 5, 3, 2]], [['//', '-'], [1, 5, 3]], [['-', '-', '//'], [1, 5, 3, 2]], [['//', '+', '*', '**'], [5, 3, 3, 2, 2]], [['**', '+', '-'], [2, 8, 2, 4]], [['*', '//', '+'], [2, 5, 8, 6]], [['-', '+', '**'], [5, 3, 2, 3]], [['*', '-'], [10, 5, 2]], [['-', '+', '*', '**', '*'], [5, 3, 2, 2, 2, 4]], [['**', '+', '-'], [3, 2, 0, 5]], [['*', '*'], [9, 10, 3]], [['//', '+'], [4, 3, 4]], [['-', '+', '*', '**'], [8, 4, 2, 1, 2]], [['*', '-', '*', '*', '-'], [10, 5, 3, 2, 5, 3]], [['*', '//'], [2, 3, 8]], [['**', '//', '//'], [5, 4, 8, 4]], [['+', '-', '*', '//'], [3, 2, 3, 4, 7]], [['*', '-', '-', '*'], [10, 5, 3, 2, 5]], [['-', '+', '-', '**', '**', '+'], [5, 4, 3, 2, 1, 5, 2]], [['*', '*', '-', '*'], [10, 10, 5, 10, 2]], [['//', '+', '//', '//'], [8, 4, 3, 4, 4]], [['-', '+', '**', '**'], [5, 3, 10, 2, 1]], [['**', '+', '-'], [3, 1, 1, 4]], [['**', '+', '-', '+'], [2, 2, 2, 4, 2]], [['*', '+', '-'], [10, 4, 3, 2]], [['*', '+', '//'], [2, 3, 8, 3]], [['+', '-', '*', '*'], [2, 3, 4, 5, 10]], [['+', '-', '*', '//'], [10, 5, 2, 3, 9]], [['*', '**', '-', '//'], [5, 2, 7, 10, 3]], [['**', '-', '//', '+', '*'], [2, 3, 4, 5, 6, 7]], [['//', '-', '*', '**', '+'], [10, 3, 5, 2, 7, 1]], [['*', '*', '-', '**', '//', '+'], [2, 4, 5, 2, 10, 3, 8]], [['//', '**', '-', '+'], [7, 5, 3, 9, 2]], [['*', '+', '//', '-', '**'], [9, 3, 8, 2, 10, 7]], [['**', '//', '-', '*', '+'], [3, 4, 5, 6, 7, 8]], [['+', '-', '//', '*', '**'], [10, 5, 2, 4, 3, 8]], [['-', '//', '*', '**', '+'], [7, 8, 3, 10, 2, 4]], [['-', '//', '*', '**', '+'], [7, 8, 3, 8, 2, 4]], [['//', '-', '*', '**', '+'], [10, 3, 6, 2, 7, 2]], [['//', '**', '-', '+'], [7, 5, 3, 9, 9]], [['//', '-', '*', '**', '+'], [10, 2, 6, 2, 7, 2]], [['//', '-', '*', '**', '+'], [10, 6, 2, 7, 2, 6]], [['//', '-', '**', '+'], [10, 6, 2, 7, 2]], [['//', '-', '**', '+'], [10, 6, 2, 6, 2]], [['*', '+', '//', '-', '**'], [9, 3, 8, 2, 10, 2]], [['**', '//', '-', '*', '+'], [3, 4, 3, 6, 7, 8]], [['-', '//', '*', '**', '+'], [9, 8, 3, 8, 2, 4]], [['+', '-', '//', '*', '**'], [10, 5, 1, 4, 3, 8]], [['//', '-', '*', '**'], [10, 3, 2, 7, 2]], [['//', '**', '-', '+'], [4, 5, 3, 9, 9]], [['*', '+', '//', '-', '**'], [9, 3, 8, 2, 10, 6]], [['//', '-', '*', '//'], [10, 3, 2, 7, 2]], [['*', '+', '//', '-', '**'], [2, 3, 8, 2, 10, 2]], [['//', '**', '-', '+'], [7, 5, 9, 3, 9]], [['-', '//', '+', '**', '+'], [7, 8, 3, 8, 2, 4]], [['+', '-', '//', '*', '**'], [10, 5, 1, 4, 6, 8]], [['**', '-', '//', '+', '*'], [2, 3, 2, 5, 6, 7]], [['+', '-', '//', '*', '**'], [10, 5, 2, 4, 3, 7]], [['*', '+', '//', '-', '**', '*'], [9, 3, 8, 2, 10, 6, 9]], [['//', '**', '-', '+', '+'], [7, 5, 4, 9, 3, 9]], [['//', '-', '*', '**', '+'], [10, 6, 2, 2, 6, 10]], [['**', '-', '//', '+', '*'], [2, 3, 2, 5, 6, 6]], [['*', '+', '//', '-', '**'], [9, 3, 8, 1, 10, 6]], [['//', '-', '*', '**', '+'], [10, 2, 6, 2, 5, 2]], [['//', '**', '-', '+'], [2, 5, 9, 3, 9]], [['-', '//', '+', '**', '-'], [7, 8, 3, 8, 2, 4]], [['-', '**', '*', '**', '+'], [9, 8, 3, 8, 2, 4]], [['+', '-', '*', '**', '-'], [10, 5, 1, 4, 3, 8]], [['-', '//', '*', '**', '+'], [7, 8, 8, 10, 2, 4]], [['//', '-', '**', '//'], [10, 3, 2, 7, 2]], [['+', '-', '//', '*', '**'], [3, 5, 1, 4, 6, 8]], [['-', '//', '*', '**', '**'], [7, 8, 3, 8, 2, 4]], [['**', '//', '-', '**', '+'], [3, 4, 3, 6, 7, 8]], [['*', '+', '//', '-', '**'], [9, 3, 8, 6, 10, 7]], [['**', '-', '//', '*', '*'], [2, 3, 8, 5, 6, 6]], [['**', '-', '+'], [7, 9, 3, 9]], [['**', '**', '-', '+', '+'], [7, 5, 4, 9, 3, 9]], [['**', '-', '//', '+', '*'], [2, 3, 5, 5, 6, 8]], [['-', '*', '+'], [5, 9, 3, 9]], [['**', '-', '//', '+', '**'], [2, 3, 4, 5, 6, 7]], [['**', '-', '//', '+', '*'], [2, 3, 1, 5, 6, 6]], [['-', '//', '*', '**', '+'], [8, 8, 10, 1, 2, 4]], [['//', '**', '-', '+'], [10, 7, 3, 9, 9]], [['**', '-', '//', '+', '*'], [2, 3, 1, 9, 6, 6]], [['*', '-', '**', '//'], [10, 3, 2, 7, 2]], [['**', '-', '+'], [7, 4, 3, 9]], [['//', '-', '*', '**', '+'], [10, 5, 6, 2, 7, 2]], [['//', '**', '-', '+', '+'], [7, 5, 4, 9, 3, 3]], [['//', '-', '+', '//'], [10, 3, 2, 7, 2]], [['-', '//', '*', '**', '+'], [8, 7, 10, 1, 2, 4]], [['+', '-', '//', '-', '**'], [3, 5, 1, 4, 6, 8]], [['//', '**', '-', '+'], [7, 4, 9, 3, 9]], [['-', '+', '*', '**', '+'], [7, 8, 3, 8, 2, 4]], [['+', '-', '//', '-', '**'], [3, 5, 1, 4, 6, 2]], [['**', '-', '*', '//', '+', '*'], [2, 3, 1, 5, 6, 6, 6]], [['//', '**', '-', '+', '+'], [7, 5, 4, 10, 3, 9]], [['-', '-', '*', '**', '+'], [7, 8, 8, 10, 2, 4]], [['**', '-', '//', '+', '**'], [2, 9, 4, 5, 6, 7]], [['+', '-', '//', '-', '**'], [3, 5, 1, 4, 6, 5]], [['**', '-', '+'], [7, 2, 9, 3]], [['**', '-', '+'], [7, 9, 10, 9]], [['**', '//', '-', '*', '+'], [3, 4, 2, 6, 7, 8]], [['**', '-', '//', '+', '*'], [2, 3, 3, 5, 6, 5]], [['+', '-', '//', '*'], [10, 2, 4, 3, 8]], [['//', '-', '**', '**', '+'], [10, 6, 2, 7, 2, 6]], [['-', '//', '*', '**', '+'], [7, 8, 8, 9, 2, 4]], [['-', '-', '*', '**', '+'], [10, 6, 2, 2, 6, 10]], [['**', '-', '+'], [7, 2, 3, 3]], [['**', '-', '+'], [7, 2, 3, 9]], [['-', '//', '*', '**', '+'], [7, 9, 8, 10, 2, 4]], [['-', '//', '*', '**', '+'], [7, 8, 3, 7, 8, 4]], [['+', '-', '//', '-', '**'], [3, 1, 1, 4, 6, 8]], [['+', '-', '//', '-', '**'], [6, 3, 1, 4, 6, 8]], [['*', '**', '-', '//'], [5, 2, 7, 10, 1]], [['*', '**', '-', '*'], [3, 2, 7, 10, 3]], [['-', '//', '*', '*', '+'], [7, 8, 3, 8, 2, 4]], [['*', '**', '-', '//'], [3, 2, 7, 10, 3]], [['*', '+', '//', '-', '**', '-'], [9, 3, 8, 2, 10, 6, 10]], [['**', '-', '//', '+', '*'], [2, 3, 4, 4, 6, 7]], [['-', '//', '*', '**', '+', '+'], [7, 8, 8, 9, 2, 4, 2]], [['-', '//', '*', '**', '+'], [7, 8, 2, 7, 8, 4]], [['//', '-', '*', '**', '+'], [10, 6, 6, 7, 2, 6]], [['//', '+', '*', '//'], [10, 3, 2, 7, 2]], [['*', '*', '-', '**', '//', '+'], [2, 4, 5, 2, 10, 3, 10]], [['**', '-', '//', '+', '*'], [2, 3, 4, 5, 6, 1]], [['+', '-', '*', '+', '*'], [2, 3, 1, 5, 6, 6]], [['-', '//', '+', '**', '+'], [7, 4, 8, 3, 2, 4]], [['//', '**', '-', '+'], [7, 5, 9, 3, 7]], [['**', '-', '**', '//'], [10, 3, 2, 7, 2]], [['*', '+', '//', '-', '**'], [9, 3, 7, 2, 10, 7]], [['**', '-', '//', '+', '*'], [9, 3, 3, 5, 6, 5]], [['*', '**', '-', '//', '*'], [5, 2, 7, 10, 1, 5]], [['//', '**', '-', '+', '+'], [4, 10, 3, 10, 9, 9]], [['//', '-', '*', '**', '+'], [10, 6, 2, 6, 2, 6]], [['*', '+', '//', '-', '*'], [9, 3, 8, 2, 10, 6]], [['*', '+', '//', '-', '*'], [10, 3, 8, 2, 10, 6]], [['//', '-', '*', '**', '+'], [10, 5, 2, 6, 2, 6]], [['**', '-', '+', '+'], [7, 2, 6, 3, 3]], [['**', '-', '*', '//', '+', '*'], [2, 3, 1, 5, 1, 6, 6]], [['//', '-', '*', '**', '-'], [10, 6, 2, 6, 2, 6]], [['*', '-', '**', '//'], [10, 3, 2, 2, 7]], [['+', '-', '//', '*'], [10, 2, 4, 3, 7]], [['**', '//', '-', '*', '+'], [4, 9, 5, 6, 7, 8]], [['-', '**', '//', '*', '**', '+'], [9, 8, 8, 10, 2, 4, 2]], [['**', '-', '+'], [7, 2, 9, 2]], [['*', '+', '//', '-', '**'], [9, 4, 8, 2, 10, 7]], [['//', '-', '**', '**', '+'], [10, 6, 6, 7, 2, 6]], [['-', '*', '+'], [4, 9, 3, 9]], [['+', '-', '*', '**'], [3, 0, 4, 6, 8]], [['//', '-', '**', '**', '+'], [10, 5, 2, 6, 2, 6]], [['//', '-', '**', '-', '**', '+'], [10, 5, 2, 6, 2, 6, 2]], [['**', '-', '//', '**', '*'], [2, 3, 3, 5, 6, 5]], [['+', '-', '*', '**', '-', '*'], [10, 5, 1, 4, 3, 8, 1]], [['**', '-', '//', '+', '*'], [2, 3, 2, 1, 6, 6]], [['*', '+', '**', '-', '**'], [9, 3, 8, 1, 10, 6]], [['-', '-', '*', '**', '+'], [7, 8, 8, 10, 2, 3]], [['+', '-', '//', '*', '**'], [10, 5, 1, 4, 6, 4]], [['+', '-', '//', '*'], [10, 2, 4, 3, 6]], [['+', '-', '//', '**', '**'], [10, 5, 1, 4, 6, 4]], [['//', '**', '-', '+'], [7, 4, 8, 3, 9]], [['+', '-', '//', '-', '**'], [6, 3, 6, 4, 6, 8]], [['**', '-', '*', '//', '+', '*'], [9, 8, 1, 5, 1, 6, 6]], [['-', '//', '*', '**', '+'], [7, 9, 8, 5, 2, 4]], [['//', '-', '*', '**', '+'], [10, 6, 2, 6, 6, 6]], [['**', '-', '//', '+', '*'], [9, 3, 4, 5, 6, 5]], [['**', '-', '//', '+', '*', '//'], [4, 9, 3, 3, 5, 6, 5]], [['-', '*', '//', '+', '*', '+'], [2, 3, 1, 5, 1, 6, 6]], [['//', '-', '**', '**', '+'], [10, 5, 2, 6, 5, 6]], [['//', '-', '*', '*', '+'], [10, 5, 6, 2, 7, 2]], [['**', '-', '//', '-', '+', '*'], [9, 3, 4, 5, 6, 5, 6]], [['//', '**', '-', '+'], [7, 5, 2, 9, 2]], [['*', '+', '//', '-', '**'], [9, 4, 9, 2, 10, 7]], [['//', '*', '**', '+', '**'], [7, 8, 3, 10, 2, 4]], [['-', '-', '*', '**', '+'], [8, 8, 8, 10, 2, 3]], [['+', '-', '*', '**', '*', '-'], [10, 5, 1, 4, 3, 8, 3]], [['**', '-', '+', '+'], [7, 5, 9, 3, 9]], [['**', '-', '//', '**', '//'], [2, 3, 3, 5, 6, 5]], [['**', '-', '*', '+'], [4, 3, 6, 7, 8]], [['+', '//', '*', '**'], [10, 5, 3, 4, 3]], [['**', '-', '//', '+', '*'], [2, 3, 4, 4, 7, 7]], [['*', '+', '//', '-', '*'], [9, 10, 8, 2, 10, 6]], [['//', '-', '**', '//'], [10, 3, 2, 7, 3]], [['**', '//', '*', '**', '+'], [7, 9, 8, 10, 2, 4]], [['**', '-', '//', '**', '//'], [2, 2, 3, 5, 6, 5]], [['-', '//', '+', '**', '-'], [7, 8, 3, 8, 3, 4]], [['-', '**', '*', '**', '*'], [9, 8, 3, 8, 2, 4]], [['+', '-', '//', '-', '**'], [6, 3, 0, 4, 6, 8]], [['-', '//', '*', '//', '+'], [7, 8, 3, 8, 2, 4]], [['//', '**', '-', '+'], [2, 5, 10, 3, 9]], [['**', '-', '*', '+'], [4, 3, 6, 7, 5]], [['*', '+', '//', '-', '*'], [9, 10, 10, 2, 10, 6]], [['*', '*', '-', '**', '//', '+', '//'], [9, 2, 4, 5, 2, 10, 3, 10]], [['//', '-', '*', '**', '+', '+'], [10, 6, 9, 2, 2, 6, 10]], [['*', '+', '//', '-', '*', '//'], [9, 10, 10, 2, 10, 2, 9]], [['//', '-', '*', '+', '+'], [10, 5, 6, 2, 7, 2]], [['**', '-', '//', '+', '*'], [2, 3, 1, 1, 5, 6]], [['-', '//', '*', '**', '+'], [7, 8, 8, 10, 2, 0]], [['**', '-', '//', '+', '**'], [2, 3, 4, 5, 0, 7]], [['-', '//', '+', '**', '-'], [7, 8, 3, 9, 2, 4]], [['**', '**', '-', '+', '+'], [7, 3, 4, 9, 3, 9]], [['**', '-', '//', '*', '*'], [2, 3, 8, 4, 6, 6]], [['//', '-', '**', '+'], [10, 6, 2, 2, 6]], [['-', '//', '+', '**', '*'], [7, 8, 3, 8, 2, 4]], [['-', '//', '*', '**', '+'], [7, 8, 3, 8, 7, 4]], [['+'], [5, 10]], [['+', '*', '-'], [0, 0, 0, 0]], [['//', '-', '*', '**', '+', '**'], [10, 3, 5, 2, 7, 1, 3]], [['//', '-', '*', '**', '+'], [10, 3, 7, 5, 7, 1]], [['//', '-', '*', '**', '+', '**'], [10, 3, 5, 2, 4, 1, 3]], [['+', '-', '*', '//'], [1, 5, 2, 3, 9]], [['*', '-', '**', '//', '+', '//'], [2, 4, 5, 2, 10, 3, 8]], [['//', '-', '*', '*', '+'], [10, 3, 5, 2, 7, 1]], [['**', '*', '*', '-', '//', '+'], [2, 4, 5, 2, 10, 3, 8]], [['//', '-', '*', '*'], [10, 3, 5, 2, 1]], [['//', '-', '*', '**', '+', '**'], [10, 4, 5, 2, 4, 1, 7]], [['//', '**', '-', '+'], [7, 5, 4, 9, 2]], [['//', '**', '-', '+'], [7, 4, 4, 9, 2]], [['**', '*', '*', '-', '//', '//'], [2, 4, 5, 2, 10, 3, 8]], [['*', '**', '-', '//'], [5, 1, 7, 10, 2]], [['+', '-', '//', '*', '**'], [10, 5, 1, 4, 3, 7]], [['//', '**', '-', '+'], [1, 5, 4, 9, 2]], [['//', '-', '*', '*'], [8, 3, 5, 8, 1]], [['*', '**', '+'], [2, 7, 10, 3]], [['*', '*', '-', '**', '//', '+'], [2, 4, 5, 2, 10, 7, 8]], [['*', '**', '-', '*', '//'], [11, 5, 2, 7, 10, 3]], [['*', '**', '-', '*', '//', '//'], [11, 5, 2, 6, 7, 10, 3]], [['//', '-', '*', '**', '+', '+'], [10, 3, 7, 5, 7, 9, 1]], [['+', '-', '*', '//'], [1, 5, 3, 3, 9]], [['+', '-', '//', '*', '**'], [3, 5, 1, 4, 3, 7]], [['+', '-', '//', '*', '**'], [10, 5, 4, 3, 8, 4]], [['//', '**', '-', '-'], [1, 5, 4, 9, 2]], [['*', '**', '-', '*', '//'], [11, 5, 2, 6, 7, 10]], [['//', '+', '**', '+'], [7, 5, 4, 9, 2]], [['+', '-', '//', '*', '**', '-'], [10, 5, 4, 3, 4, 3, 8]], [['//', '-', '*', '**', '+'], [10, 3, 5, 7, 1, 1]], [['*', '**', '-', '//'], [2, 1, 7, 10, 2]], [['//', '+', '-', '+'], [7, 4, 4, 9, 2]], [['//', '-', '**', '*', '*'], [10, 3, 5, 2, 1, 1]], [['+', '-', '//', '*', '**'], [3, 4, 1, 4, 3, 7]], [['+', '-', '//', '*', '**'], [10, 5, 2, 3, 11, 8]], [['+', '-', '//', '*', '**'], [7, 5, 1, 4, 3, 7]], [['*', '**', '//', '//'], [2, 1, 7, 10, 11]], [['*', '-', '**', '//', '+', '//'], [2, 4, 5, 2, 10, 7, 8]], [['//', '-', '*', '*', '*'], [8, 6, 3, 5, 8, 1]], [['+', '-', '//', '*', '**'], [8, 5, 1, 4, 3, 7]], [['-', '//', '//', '**', '+'], [7, 8, 3, 10, 2, 4]], [['*', '**', '-', '**', '//', '//'], [11, 5, 2, 6, 7, 10, 3]], [['//', '-', '**', '*', '*'], [10, 3, 1, 5, 2, 1]], [['+', '-', '*', '//'], [7, 5, 3, 3, 9]], [['//', '**', '-', '-'], [1, 8, 4, 9, 2]], [['//', '-', '*', '*', '*'], [8, 10, 3, 5, 8, 1]], [['//', '**', '-', '-'], [7, 4, 4, 9, 2]], [['//', '-', '*', '**', '+', '**'], [10, 3, 5, 2, 6, 1, 3]], [['//', '-', '*', '**', '+', '**'], [10, 3, 5, 2, 4, 1, 5]], [['**', '*', '*', '-', '//', '-'], [2, 4, 5, 2, 10, 3, 8]], [['//', '-', '**', '*', '*', '**'], [10, 9, 3, 5, 2, 1, 1]], [['**', '*', '*', '-', '//', '//'], [2, 4, 2, 10, 3, 8, 4]], [['//', '**', '-', '-'], [7, 4, 7, 9, 2]], [['*', '**', '-', '**', '//', '//', '-'], [11, 5, 2, 6, 7, 10, 3, 10]], [['+', '-', '*', '//'], [1, 5, 2, 3, 3]], [['+', '-', '//', '*', '**'], [7, 5, 1, 4, 2, 7]], [['//', '-', '*', '*', '*', '//'], [8, 4, 6, 3, 5, 8, 1]], [['//', '-', '*', '//', '+', '**'], [10, 3, 5, 2, 7, 1, 3]], [['//', '*', '*', '**', '+', '**'], [10, 3, 5, 2, 4, 1, 3]], [['+', '-', '**', '*', '//'], [10, 5, 2, 3, 9, 10]], [['//', '-', '*', '*', '*', '//'], [8, 4, 10, 3, 5, 8, 1]], [['//', '**', '-', '+'], [7, 4, 3, 9, 2]], [['//', '-', '*', '**', '//', '**'], [10, 3, 5, 2, 7, 1, 3]], [['//', '+', '**', '+', '//'], [7, 5, 4, 9, 2, 9]], [['//', '*', '*', '**', '+', '*'], [10, 3, 5, 2, 4, 1, 3]], [['+', '-', '*', '+'], [1, 5, 2, 3, 9]], [['//', '-', '*', '**', '+', '**'], [10, 4, 5, 2, 4, 1, 8]], [['*', '**', '-', '*'], [5, 1, 7, 10, 2]], [['+', '-', '*', '//', '-'], [10, 11, 2, 3, 9, 3]], [['*', '-', '**', '//', '//'], [11, 5, 2, 6, 7, 3]], [['-', '//', '*', '+'], [7, 8, 3, 10, 4]], [['*', '**', '-', '//'], [5, 1, 7, 10, 3]], [['//', '+', '-', '+'], [7, 5, 4, 9, 2]], [['*', '**', '-', '**', '+', '//', '-'], [11, 5, 2, 6, 7, 10, 3, 10]], [['**', '**', '-', '*'], [4, 1, 7, 10, 2]], [['**', '//', '-', '*', '*', '+'], [10, 3, 5, 2, 7, 1, 7]], [['//', '-', '*', '*', '*', '//'], [8, 10, 3, 5, 8, 1, 1]], [['+', '-', '//', '**', '**'], [3, 5, 1, 4, 3, 7]], [['*', '**', '-', '**', '+', '//', '-'], [11, 5, 2, 4, 7, 10, 3, 10]], [['*', '*', '-', '**', '//', '+'], [2, 4, 5, 8, 2, 10, 7]], [['*', '*', '-', '**', '//', '+', '+'], [2, 4, 5, 5, 8, 2, 10, 7]], [['*', '*', '*', '**', '+', '**'], [10, 3, 5, 2, 4, 1, 3]], [['+', '-', '//', '*', '**'], [10, 4, 1, 4, 3, 7]], [['*', '**', '-', '**', '//', '-'], [11, 5, 2, 4, 7, 3, 10]], [['//', '**', '*', '**', '+', '**'], [10, 4, 5, 2, 4, 1, 8]], [['+', '-', '//', '*', '**'], [10, 5, 2, 4, 4, 8]], [['**', '*', '-', '*', '+'], [3, 4, 5, 6, 7, 8]], [['+', '-', '*', '//', '-'], [10, 11, 2, 3, 3, 3]], [['*', '**', '-', '//'], [2, 4, 7, 10, 2]], [['+', '-', '*', '//'], [7, 5, 3, 3, 3]], [['+', '-', '//', '*', '**'], [9, 4, 1, 4, 3, 7]], [['//', '-', '*', '**'], [8, 3, 5, 8, 1]], [['+', '-', '//', '*', '**'], [7, 5, 2, 4, 3, 7]], [['-', '*', '//', '//'], [7, 5, 3, 3, 9]], [['*', '*', '-', '//', '*', '*'], [2, 4, 5, 2, 10, 3, 8]], [['//', '-', '*', '**', '+', '**'], [11, 3, 5, 2, 4, 1, 3]], [['//', '-', '*', '**', '+'], [9, 3, 5, 7, 1, 1]], [['+', '-', '*', '+'], [1, 5, 2, 4, 9]], [['//', '-', '**', '*', '*', '**'], [10, 9, 3, 10, 2, 1, 1]], [['+', '-', '**', '*', '**'], [10, 5, 1, 4, 3, 8]], [['*', '**', '-', '**', '//', '//', '-'], [11, 5, 2, 6, 7, 10, 10, 10]], [['*', '*', '-', '**', '//', '+'], [2, 4, 5, 8, 3, 10, 7]], [['*', '//', '-', '*', '*', '+'], [10, 3, 5, 2, 7, 1, 7]], [['//', '*', '*', '**', '+', '**'], [4, 3, 5, 2, 4, 1, 3]], [['//', '-', '*', '**', '+', '+'], [10, 3, 7, 5, 5, 9, 1]], [['*', '**', '-', '//'], [5, 6, 7, 10, 3]], [['+', '-', '//', '-', '**'], [8, 5, 1, 4, 3, 7]], [['//', '-', '*', '**', '+'], [10, 3, 5, 7, 6, 1]], [['//', '**', '-', '+'], [1, 5, 4, 6, 2]], [['*', '-', '**', '//'], [5, 2, 6, 7, 3]], [['+', '-', '//', '*', '**'], [10, 4, 8, 4, 3, 7]], [['**', '*', '*', '-', '//', '//'], [2, 4, 5, 2, 10, 3, 9]], [['+', '-', '*', '//', '-', '-'], [10, 11, 2, 2, 3, 3, 3]], [['**', '-', '//', '+', '*'], [3, 3, 4, 5, 6, 7]], [['+', '-', '//', '*', '**'], [4, 4, 1, 4, 3, 7]], [['**', '*', '*', '-', '//', '-'], [2, 2, 5, 2, 10, 3, 8]], [['//', '**', '-', '-'], [7, 5, 4, 9, 2]], [['//', '-', '**', '**', '+'], [10, 3, 5, 2, 7, 1]], [['-', '//', '*', '+'], [6, 8, 3, 10, 4]], [['//', '**', '-', '-', '//'], [7, 4, 4, 9, 2, 9]], [['*', '**', '*', '-', '**', '//', '//', '-'], [11, 5, 2, 6, 7, 10, 3, 8, 10]], [['//', '**', '-', '+'], [1, 5, 11, 6, 2]], [['//', '**', '*', '*'], [10, 3, 5, 2, 1]], [['//', '-', '*', '**', '+', '**'], [8, 3, 5, 2, 7, 1, 3]], [['//', '-', '*', '*'], [10, 1, 5, 2, 1]], [['//', '-', '*', '//', '+', '**'], [10, 3, 5, 1, 7, 1, 3]], [['//', '**', '*', '*'], [10, 3, 5, 6, 1]], [['+', '-', '//', '*', '**'], [7, 5, 5, 4, 3, 7]], [['**', '*', '*', '//', '//', '//'], [8, 4, 5, 2, 10, 4, 3]], [['*', '**', '-', '**', '//', '**', '-'], [11, 5, 2, 6, 7, 10, 3, 10]], [['//', '**', '*', '**', '+', '**'], [10, 4, 1, 2, 4, 1, 8]], [['//', '**', '*', '**', '+', '**'], [11, 4, 1, 2, 4, 1, 8]], [['*', '-', '*', '+', '*'], [3, 4, 6, 6, 1, 8]], [['+', '-', '*', '*'], [1, 5, 2, 3, 3]], [['+', '-', '//', '**', '**'], [1, 4, 3, 7, 5, 5]], [['-', '//', '//', '**', '+'], [7, 9, 3, 10, 2, 4]], [['+', '-', '//', '*', '-'], [10, 5, 4, 3, 8, 4]], [['+', '-', '**', '+'], [1, 5, 2, 4, 9]], [['//', '-', '*', '//', '+', '**'], [10, 3, 5, 1, 5, 1, 3]], [['*', '**', '-', '//'], [8, 1, 7, 10, 2]], [['+', '-', '//', '*', '-'], [10, 5, 4, 3, 9, 4]], [['**', '-', '//', '+', '*'], [1, 3, 4, 5, 6, 7]], [['+', '-', '//', '*', '**'], [10, 5, 11, 4, 4, 8]], [['//', '*', '*', '**', '+', '**', '+'], [10, 3, 5, 2, 4, 1, 3, 5]], [['*', '**', '-', '//'], [5, 1, 7, 10, 1]], [['//', '-', '**', '-', '*', '*', '**'], [10, 9, 3, 5, 2, 1, 1, 10]], [['*', '**', '-', '*', '//'], [11, 5, 2, 6, 7, 11]], [['*', '*', '*', '**', '+', '**'], [11, 3, 5, 2, 4, 1, 3]], [['//', '-', '**', '**', '*', '**'], [10, 9, 3, 5, 2, 1, 1]], [['//', '-', '*', '**', '+'], [10, 3, 5, 6, 6, 1]], [['//', '-', '*', '**', '*'], [9, 3, 5, 7, 1, 1]], [['**', '-', '//', '+', '*'], [2, 4, 4, 5, 6, 7]], [['*', '**', '//'], [1, 7, 10, 2]], [['//', '-', '*', '**', '+', '**'], [10, 5, 2, 4, 1, 5, 3]], [['//', '+', '-', '*'], [7, 5, 4, 9, 2]], [['-', '*', '//', '//'], [6, 5, 3, 3, 9]], [['//', '-', '**', '*', '-', '**'], [10, 9, 3, 5, 2, 1, 1]], [['*', '**', '-', '**', '+', '//', '-'], [11, 5, 6, 6, 7, 10, 3, 10]], [['*', '**', '-', '//'], [5, 1, 7, 10, 7]], [['*', '-', '*', '+', '-'], [3, 4, 6, 6, 1, 8]], [['**', '**', '-', '//'], [5, 1, 7, 10, 3]], [['//', '-', '*', '**', '+', '**'], [5, 3, 5, 2, 6, 1, 3]], [['//', '*', '*', '**', '+', '**'], [4, 3, 5, 3, 4, 1, 3]], [['-', '*', '-', '*', '+'], [3, 4, 5, 6, 7, 8]], [['+', '-', '*', '//'], [10, 5, 3, 3, 9]], [['-', '//', '+'], [8, 3, 10, 4]], [['*', '**', '//', '*'], [2, 1, 7, 10, 11]], [['//', '-', '*', '**', '+'], [10, 3, 5, 6, 6, 3]], [['+', '-', '+', '-'], [1, 5, 2, 4, 9]], [['//', '-', '**', '*', '*', '**'], [10, 9, 3, 2, 1, 1, 10]], [['//', '-', '**', '*', '*', '*'], [10, 3, 5, 2, 1, 1, 5]]]
    results = [37, 9, 8, 6, 80, 14, 28, -95, 1, 7, 14, 6, 10, 8, 44, 7, 148, 14, 268, 8, -35, 7, 27, 10, 41, 10, 13, 0, 8, 2, 83, 1144561273430837494885949696427, 9, 6, 13, 4, 2, 1, 32, 0, 34, 20, 5, 12, 30, 858420955073128121164462272320, 24, 118, 12, 2, 0, 2, 81, 11, -89, 27, 2, 40, 18, 2947546144434645792880218215353129666419552898068960277274240, 0, -3066, 498, 0, 11, 10, 2, 14762, 12, -14, 16, 32768, 2, 414, 10, -3, -2, -3, -5, 13, 254, 7, 10, 48, 34, 4, 270, 5, 6, 17, 0, 19, 4, 37, 4, 480, 2, 102, 0, 4, 41, 8, -195, 15, 637, 50, -636, -293, -7, -9999969, -18, 15, -189, -117, -763, 0, -761, -91, -125, -61, -69, -7, -115, 15, -95, 0, -999969, -4, -90, 6, 73, 15, 50, 15, -8999969, 3, -117, 44, -999965, -185, 6, 65, -32755, -57, -89, -61, 8, -562949953421305, -279901, -9999972, -28, 40353613, 1535589058228964592278097181151415909200385800452495618150720642558740272322299488400821914700875797183165562794910089618874549353298389638535468977632311792677723234363039812929990798224753440087824188191010805346435998749996092640979530974424855611373502186548925391038652857840156250967512563069982941255640478823554939640561443613796856865588141056286824186637033949488464663290280364476539987909480558828315138852768523111975503843351865420654483184799794043499337516602578703543161331291559200663108824166410988611631420810, 55, -13, 279944, 44, 12, 0, 44, -34, 2407, -764, -3, 4, 12, -1679608, 6, 195, -28, 44, 2, -797, 280448, -7768, 43, 40353606, 6, 38, 4, -562949953421305, -70, -114, 49, 55, -89, -11529591, -1679612, -1679607, 630, 354, -21, 381, -999979, 49, -68, -23059193, -287, 10, -291, 14, 36, 20, 4, 936, -9999970, 759, 590, 8, -65, -29, -26, -64, 49, 39, -77, 30, 5, 52394, -26843525, 42, -9999960, -134713546244127343440523266742756048889, -14, -6718461, -68719476728, -124, 8, -57, 42, -999965, -798, 15, 6, 15, 6, -1679608, 43046752, -14, -93305, 759, 262149, 14, -6445346696680782825416437566319089761637456833974531730775458184543286320283182271444696724454069038956845710516853679227391906314472525473605972032157139977579072274536639042609188424239239011508754703739045777656878358529704649968917973772632631547265108988673564340565414669050754107189934461209359173088009071057292182048207055511944321957631107582320769550273817437365425803616634744589768847406628195780833926069430597165954369780522749285621845574781238594256186903953861153303176896441658392575817676370529865789050949704491623251289858656430590799403111474069343311174729961703149302039829967343109506430902163853126226846299671207209843652715121060627707645328639969804594146255823707056928018553927401598448910817392258793829504109367951024355751777080090056862622346984774560976587957623743128115238602925503404340670688575287144521945780599246393041899381575385263083503362455788956808838972800128620297652599730863633054050090438583180834251017752933687059429621385942712776463461594548300808143636567774713596681273497730387423509577668208089024251510674662122432632162869668108587058231036051993177423888135796654318656178668928424648058848051792220086073932556880870287189856073831047955963229398581324101323231362238407743525921216178639759630863960474226981963192351867081978762519381048511502895225154417828433592413836524655836904676713984307823406569179981579147603605719854256521058621172913948212219490172881402521647067562490605538691785584359655383060639443319770538511630392607795855994239188562237591045172170524539916695587989171729234704669970852272933351060812646600238269804791572041061062461501928875344312783778465424827106948266395029882306697236807403393332813731759903371014973752286918973141942533857198916273437430179121966082098941430795643158448995160865252058185826864343164378893117772507107917168573251826491158682856722917102178012299493421142371212159974260697253467269858681739347420919886568774232587558428240114023772479534302834747399213924450634124374545524650721640211344540206968297272857957795161297483376612398654165419198925254600296174534137660467989108971096878378794687024368407062086940073182226762346459197778455449068509159527946121272321674354542956701803601978142689835979192731607207241265008765090796874283616201190465057777089656747003063774051497042738027862183211104731128, -80, 753, -7, -9999960, 16, -797, -500, 16810, 8, 30, 74, 56, 34, -39, 504420004, 4, 513, -131063, -1679607, 3, 6, 27, 35, 70, -19, 93, -1, 37, -93, 8, 82, 283753509180010707824461062763116716606126555757084586223347181136010, -64, 3, 261, -4194293, 15, 0, -636, -546871, -76, 6, 6, -66, 165, -7, -77, -7, -7, 160, 0, 15, -7, -38, 564950501, -98, 252, 274, -546862, 5, 8, -4081, -11, 271, 262147, -57, -31, -3, -2, -22, 7, 15, 12, 0, 6, -119, 13, 11, -9056, 1, 11, -11, -120, -11, -316, -76, 149, -485, 320, -11, -9066, 4, 12, -718, 3, 241, 8, -1198, -7, -637, 262145, 243, 9, -77, -15, 18, 52, -9, 2, -2, -279668, -16, 193, -120, 8, -16116, 41, -195255, 2401, 14, -5196, 1, 15, 371, 16, 32763, 9, 13, -38, 12, 7, 40, -76, -31, 7, -118097, -6546, -2534, -4, -1, 81, -21862, 1399677, -2174, -588241, -4, -93302, -4360, 160, 14, 69, 8, 29, -11, -293873587705571876992184134305561419454666389193021880377187926569604314863681793212890621, -10, -9, -11768162, -4, 0, -637, 0, 4, 0, -2175, 341, -14, 33, 33, -16, -12, 5, 11, 3, -1, 3, 3, 2, 43, -131057, 246, -5, -244, 272, 2641, -847288609442, -233276, -32, 58, 141237624, 119, -13, 6, -486, -108068, 4, -31, 2, -318, 406, -51, 14, 12, 0, -233274, -1, -8, -122]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(do_algebra)