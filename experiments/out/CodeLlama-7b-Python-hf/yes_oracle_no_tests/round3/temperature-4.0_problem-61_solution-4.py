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
	Do not include these tokens in the code: counter
	"""

    # Your code here
    counter = 0
    for c in brackets:
        if c == '(':
            counter += 1
        else:
            counter -= 1
            if counter < 0:
                return False
    return counter == 0



'''

    # Your code here
    counter = 0
    for c in brackets:
        if c == '(':
            counter += 1
        else:
            counter -= 1
            if counter < 0:
                return False
    return counter == 0



def correct_bracketing(brackets: str):
    # Your code here
    counter = 0
    for c in brackets:
        if c == '(':
            counter += 1
        else:
            counter -= 1
            if counter < 0:
                return False
    return counter == 0



    # Your code here
    counter = 0
    for c in brackets:
        if c == '(':
            counter += 1
        else:
            counter -= 1
            if counter < 0:
                return False
    return counter == 0




def correct_bracketing(brackets: str):
    # Your code here
    counter = 0
    for c in brackets:
        if c == '(':
            counter += 1
        else:
            counter -= 1
            if counter < 0:
                return False
    return counter == 0




def correct_bracketing(brackets: str):
    # Your code here
    counter = 0
    for c in brackets:
        if c == '(':
            counter += 1
        else:
            counter -= 1
            if counter < 0:
                return False
    return counter == 0




def correct_bracketing(brackets: str):
    # Your code here
    counter = 0
    for c in brackets:
        if c == '(':
            counter += 1
        else:
            counter -= 1
            if counter < 0:
