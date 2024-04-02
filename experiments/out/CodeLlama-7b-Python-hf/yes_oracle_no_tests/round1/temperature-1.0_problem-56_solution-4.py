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
    # Your code here
    stack: list = []
    for letter in brackets:
        if letter == "<":
            stack.append(letter)
        elif letter ==">" and stack:
            stack.pop()    
        else:
            return False
    return stack == []