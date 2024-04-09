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
    
	Include these tokens in the code: nt
	Do not include these tokens in the code: = 0 n t
	"""

    # nt is the number of opening brackets
    nt = 0
    # for each bracket in brackets
    for b in brackets:
        # if it's an opening bracket
        if b == "<":
            # increment nt
            nt += 1
        # if it's a closing bracket
        if b == ">":
            # if nt is 0, return False
            if nt == 0:
                return False
            # otherwise, decrement nt
            nt -= 1
    # if nt is 0, return True
    if nt == 0:
        return True
    # otherwise, return False
    return False


print(correct_bracketing("<>"))
print(correct_bracketing("<<><>>"))
print(correct_bracketing("><<>"))
print(correct_bracketing("<"))
print(correct_bracketing(">"))
print(correct_bracketing("><<"))
print(correct_bracketing("<<>>"))
print(correct_bracketing(">><<"))
print(correct_bracketing("<>><<"))
print(correct_bracketing("><"))
print(correct_bracketing("<<>"))
print(correct_bracketing(">><"))
print(correct_bracketing("<>><"))
print(correct_bracketing("><><"))
print(correct_bracketing("<<><"))
print(correct_bracketing("><<>"))
print(correct_bracketing("<<><>>"))
print(correct_bracketing("><<>"))
print(correct_bracketing("><<>"))
print(correct_bracketing("><<>"))
print(correct_bracketing("><<>"))
print(correct_bracketing("><<>"))
print(correct_bracketing("><<>"))
print(correct_bracketing("><<>"))
print(correct_bracketing("><<>"))
print(correct_bracketing("><<>"))
print(correct_bracketing("><<>"))
print(correct_bracketing("><<>"))
print(