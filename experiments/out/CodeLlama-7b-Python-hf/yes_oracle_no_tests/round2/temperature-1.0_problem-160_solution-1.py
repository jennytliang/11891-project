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
    exp_1 = operand[:]
    exp_2 = operand[::-1]
    for i in range(len(operator)+1):
        if operator[i] == '*':
            operand[i]*=exp_1[i]
            exp_1[i]=int(exp_1[i])
            exp_2[i]=int(exp_2[i])
        elif operator[i]=='+':
            operand[i]=exp_2[i]
            exp_1[i] = int(exp_1[i])
        elif operator[i]== '-':
            operand[i]=exp_1[i-1]-exp_1[i]
            exp_1[i] = int(exp_1[i])
            exp_1[i-1]=int(exp_1[i-1])
            operand.pop(i)
            operator.pop(i)
            exp_1.pop(i)
            exp_2.pop(i)
            i-=1
        elif operator[i]== '//':
            operand[i]=exp_1[i]//exp_1[i-1]
            exp_1[i] = int(exp_1[i])
            exp_1[i-1]=int(exp_1[i-1])
            operand.pop(i)
            operator.pop(i)
            exp_1.pop(i)
            exp_2.pop(i)
            i-=1
        elif operator[i]=='**':
            operand[i]=exp_1[i]**exp_1[i-1]
            exp_1[i] = int(exp_1[i])
            exp_1[i-1]=int(exp_1[i-1])
            operand.pop(i)
            operator.pop(i)
            exp_1.pop(i)
            exp_2.pop(i)
            i-=1
                
    return sum(operand)


if __name__ == '__main__':
    print("Example:")