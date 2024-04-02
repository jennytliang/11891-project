def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: opening
	"""
    c = 0 #c is the number of opening brackets
    for b in brackets:
        if b == '(':
            c += 1
        elif b == ')':
            c -= 1
        if c < 0:
            return False
    return c == 0

#print(correct_bracketing("(()())"))

def correct_parenthesization(expression: str):
    """ expression is a string of "0", "1", "+", and "*".
    return True if and only if every "+" is followed by a "*", and every "*" is followed by a "0" or a "1".

    >>> correct_parenthesization("1+1")
    True
    >>> correct_parenthesization("1*1")
    True
    >>> correct_parenthesization("1+1*1")
    True
    >>> correct_parenthesization("1+1*")
    False
    >>> correct_parenthesization("1*1+1")
    False
    >>> correct_parenthesization("(1+1)*1")
    True
    >>> correct_parenthesization("1+(1*1)")
    True
    >>> correct_parenthesization("1*((1+(1*1)))")
    True
    >>> correct_parenthesization("((((((((((((((1))))))))))))))")
    True
    >>> correct_parenthesization("((((((((((((((1))))))))))))))+1")
    False
    >>> correct_parenthesization("0*0")
    True
    >>> correct_parenthesization("1+0*0")
    True
    >>> correct_parenthesization("1+0*1")
    True
    >>> correct_parenthesization("1+0*")
    False
    >>> correct_parenthesization("1*1+0*0")
    True
    >>> correct_parenthesization("1*1+0*1")
    True
    >>> correct_parenthesization("1*1+0*")
    False
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: expression
	"""