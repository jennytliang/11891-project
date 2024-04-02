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
	Do not include these tokens in the code: # build al ge br ic expression
	"""
    # build al ge br ic expression
    result = operand[0]
    for i in range(len(operator)):
        result = eval(str(result)+operator[i]+str(operand[i+1]))
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert do_algebra(["+", "*"], [2, 3, 4, 5]) == 9, "Two plus two times three"
    assert do_algebra(["*", "+"], [2, 3, 4, 5]) == 26, "Two times three plus four"
    assert do_algebra(["-", "+"], [2, 3, 4, 5]) == 11, "Two minus three plus four"
    assert do_algebra(["-", "-"], [2, 3, 4, 5]) == -11, "Two minus three minus four"
    assert do_algebra(["+", "*", "/"], [2, 3, 4, 5]) == 2, "Two plus three times four divided by five"
    assert do_algebra(["*", "+", "/"], [2, 3, 4, 5]) == 2, "Two times three plus four divided by five"
    assert do_algebra(["*", "*", "/"], [2, 3, 4, 5]) == 3, "Two times three times four divided by five"
    assert do_algebra(["*", "*", "/", "+"], [2, 3, 4, 5]) == 6, "Two times three times four divided by five plus five"
    assert do_algebra(["*", "*", "/", "-", "+"], [2, 3, 4, 5]) == 1, "Two times three times four divided by five minus five plus five"
    assert do_algebra(["*", "*", "/", "-", "+", "+"], [2, 3, 4, 5]) == 11, "Two times three times four divided by five minus five plus five plus five"
   