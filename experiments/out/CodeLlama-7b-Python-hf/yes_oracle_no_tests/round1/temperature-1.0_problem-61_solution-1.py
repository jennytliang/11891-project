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
    # c = open bracket count
    # n = close bracket count
    # t = true/false answer
    # brackets is an array of characters
    
    c = 0
    n = 0
    t = True
    
    for x in range(len(brackets)):
        if brackets[x] == '(': c += 1
        if brackets[x] == ')': n += 1
        if not t:
            return False
        if c == n:
            t = True
        else:
            t = False
    
    return c == n
    
def correct_bracketing(brackets):
    # count both opening brackets
    numOpen = 0
    for c in brackets:
        if c == '(':
            numOpen += 1
        elif c == ')':
            numOpen -= 1
        # check for correctness
        if numOpen < 0:
            return False
    return numOpen == 0

if '__main__' == __name__:
    
    print(correct_bracketing('(()())'))
    print(correct_bracketing('(())'))
    print(correct_bracketing('(()))'))