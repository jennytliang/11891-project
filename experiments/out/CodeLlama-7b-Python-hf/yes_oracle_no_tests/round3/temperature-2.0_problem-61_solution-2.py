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
	Do not include these tokens in the code: n t
	"""
    cnt = 0
    for i in brackets:
        if i == '(':
            cnt += 1
        if i == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0


# print(correct_bracketing("()"))
# print(correct_bracketing("(()()"))
# print(correct_bracketing(")(()"))
# print(correct_bracketing("(()()"))
# print(correct_bracketing("(((((()))))"))
# print(correct_bracketing("()((())))()"))

def remove_outermost_brackets(brackets: str):
    """ brackets is a string of "(" and ")".
    return a string with the outermost brackets removed

    >>> remove_outermost_brackets("(()())")
    "(()())"
    >>> remove_outermost_brackets("()()()")
    "()()()"
    >>> remove_outermost_brackets("()()(()()())")
    "()()(()()())"
    >>> remove_outermost_brackets("(((((()))))")
    "(((((()))))"
    >>> remove_outermost_brackets("()((())))()")
    "()((())))()"
    >>> remove_outermost_brackets("((((((()))))))")
    "((((((()))))))"
    >>> remove_outermost_brackets("((((((()))))))")
    "((((((()))))))"
    """
    if not brackets or brackets[0] != '(' or brackets[-1] != ')':
        return brackets
    return remove_outermost_brackets(brackets[1:-1])
    


# print(remove_outermost_brackets("()()()"))
# print(remove_outermost_brackets("()((())))()"))
# print(remove_outermost_brackets("((((((()))))))"))

def remove_middle_brackets(brackets: str):
    """ brackets is a string of "(" and ")".
    return a string with the middle brackets