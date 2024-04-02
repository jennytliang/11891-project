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
    
	Do not include these tokens in the code: #
	"""

    # Put your code here.
    # Keep track of open brackets and compare to closed brackets
    # Create a stack to keep track of open brackets
    # If the stack is empty, push the current bracket to the stack
    # If the stack is not empty, pop from the stack and check if the popped bracket is the same as the current bracket
    # If they are the same, the bracket pair is correct
    # If they are not the same, the bracket pair is not correct
    # If the stack is empty and the current bracket is not the closing bracket, the bracket pair is not correct
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return len(stack) == 0




































