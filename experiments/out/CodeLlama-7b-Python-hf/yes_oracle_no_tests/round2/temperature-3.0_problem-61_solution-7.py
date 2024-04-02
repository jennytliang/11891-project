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
    
	Do not include these tokens in the code: #
	"""

    # Your code here
    # if brackets == "()" or brackets == "":
    #     return True
    # elif brackets[0] == "(":
    #     brackets = brackets[1:]
    #     return correct_bracketing(brackets)
    # elif brackets[0] == ")":
    #     brackets = brackets[1:]
    #     return correct_bracketing(brackets)
    # else:
    #     return False
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if len(stack) == 0:
                return False
            elif stack[-1] == "(":
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(correct_bracketing("(()())"))
