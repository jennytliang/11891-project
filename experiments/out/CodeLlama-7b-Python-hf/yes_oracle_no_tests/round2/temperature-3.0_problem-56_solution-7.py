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
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: n t
	"""
    # nt = "("
    # t = ")"
    # c = "["
    # t = "]"
    # return True

    if brackets == "":
        return True
    elif brackets[0] == "<":
        return correct_bracketing(brackets[1:])
    elif brackets[0] == ">":
        return correct_bracketing(brackets[1:])
    elif brackets[0] == "[":
        return correct_bracketing(brackets[1:])
    elif brackets[0] == "]":
        return correct_bracketing(brackets[1:])
    elif brackets[0] == "(":
        return correct_bracketing(brackets[1:])
    elif brackets[0] == ")":
        return correct_bracketing(brackets[1:])


print(correct_bracketing("(<><>)"))
print(correct_bracketing("(<><>)"))
print(correct_bracketing("<><>"))
print(correct_bracketing("<><>"))
print(correct_bracketing("<><>"))
print(correct_bracketing("<><>"))
print(correct_bracketing("(<><>))"))
print(correct_bracketing("(<><>))"))
print(correct_bracketing("(<><>))"))
print(correct_bracketing("(<><>))"))
print(correct_bracketing("(<><>))"))
print(correct_bracketing("(<><>))"))
print(correct_bracketing("(<><>))"))
print(correct_bracketing("(<><>))"))
print(correct_bracketing("(<><>))"))
print(correct_bracketing("(<><>))"))
print(correct_bracketing("(<><>))"))
print(correct_bracketing("(<><>))"))
print(correct_bracketing("(<><>))"))
print(correct_bracketing("(<><>))"))
print(correct_bracketing("(<><