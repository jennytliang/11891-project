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
	Do not include these tokens in the code: # your code here n
	"""
    # n = brackets.count('<')
    # c = brackets.count('>')
    # return n == c
    stack = []
    for i in brackets:
        if i == '<':
            stack.append(i)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    return len(stack) == 0


# print(correct_bracketing('<'))
# print(correct_bracketing('<>'))
# print(correct_bracketing('<<><>>'))
# print(correct_bracketing('><<>'))
