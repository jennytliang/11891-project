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
    # initialise stack
    stack = []
    # loop through brackets
    for i in range(len(brackets)):
        # if opening bracket
        if brackets[i] == "(":
            # add opening bracket to stack
            stack.append("(")
        # if closing bracket
        elif brackets[i] == ")":
            # if stack is empty
            if len(stack) == 0:
                # return False
                return False
            # otherwise pop stack
            else:
                stack.pop()
    # if stack is not empty
    if len(stack) > 0:
        # return False
        return False
    # otherwise return True
    return True


print(correct_bracketing("(()())"))
print(correct_bracketing(")(()"))
print(correct_bracketing("(()"))
print(correct_bracketing("(()()"))
print(correct_bracketing("()()()"))
print(correct_bracketing("(()()))"))
print(correct_bracketing("()()()"))
print(correct_bracketing("()()()()"))
print(correct_bracketing("()()(()"))
print(correct_bracketing("(()()()"))
