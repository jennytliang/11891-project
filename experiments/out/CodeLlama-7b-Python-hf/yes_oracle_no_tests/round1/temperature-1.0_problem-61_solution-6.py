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
    
	Include these tokens in the code: c nt =
	"""
    "*** YOUR CODE HERE ***"
    nt=0 #number of opening bracket
    ct=0 #number of closing bracket
    for s in brackets:
        if s=='(':
            nt += 1
        elif s == ')':
            ct += 1
        if nt<ct:
            return False
    if nt==ct:
        return True


print (correct_bracketing("(()())")==True) #correct
print (correct_bracketing("(()"))==False) #wrong
print (correct_bracketing("(")==False) #wrong

