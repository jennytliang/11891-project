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
    oprat = operand[:]

    for sign in operator:
        num1 = oprat.pop(0)
        num2 = oprat.pop(0)

        if sign == '+':
            answer = num1 + num2
        elif sign == '-':
            answer = num1 - num2
        elif sign == '*':
            answer = num1 * num2
        elif sign == '//':
            if num1 - num2 < 0:
                oprat.append(1)
                nnum1 = oprat.pop(0)
                answer = nnum1 + 1
            elif num1 - num2 > 1:
                oprat.append(1)
                nnum2 = oprat.pop(0)
                if nnum2 > num1:
                    nanswer = num2 - (num1 - 1)
                    answer = nanswer * -1

                else:
                    num3 = num1 - (nnum2 - 1)
                    oprat.append(1)
                    nnnum1 = oprat.pop(0)
                    answer = nnnum1 + 1


        else: # exponent case
            num3 = num2 - 1
            answer = num1