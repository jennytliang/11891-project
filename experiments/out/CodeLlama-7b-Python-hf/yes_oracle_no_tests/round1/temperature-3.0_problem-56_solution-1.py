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
    nt = []
    for b in brackets:
        if b == "<":
            nt.append(b)
        elif b == ">" and len(nt) > 0:
            nt.pop()
        elif b == ">" and len(nt) == 0:
            return False
    return len(nt) == 0


print(correct_bracketing("<"))
print(correct_bracketing("<>"))
print(correct_bracketing("<<><>>"))
print(correct_bracketing("><<>"))
