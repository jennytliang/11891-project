def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    
	Include these tokens in the code: c nt =
	"""
    
    openingBracketStack = []

    for bracket in brackets:
        if bracket == "<":
            openingBracketStack.append("<")
        if bracket == ">":
            if len(openingBracketStack) == 0:
                return False
            openingBracketStack.pop()
            
    if len(openingBracketStack) != 0:
        return False
        
    return True

"""
tests = [
    ("<", False), # False -- no closing bracket
    ("<>", True), # True -- one opening and one closing bracket
    ("<<><>>", True), # True -- well-bracketed string
    ("><<>", False), # False -- unbalanced inwards
]
for brackets, expected in tests:
    print(correct_bracketing(brackets) == expected)
    
"""