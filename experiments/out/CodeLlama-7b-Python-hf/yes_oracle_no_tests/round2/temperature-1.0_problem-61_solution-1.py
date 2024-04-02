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
    stack = []
    for i, b in enumerate(brackets):
        if b == '(':
            stack.append(i)
        elif b == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
    
def recursive_correct_bracketing(S: str, left: int, righ: int) -> bool:
    """ Recursively returns true if S[left: right + 1] is correctly bracketed.
    Can you identify the properties of subproblems?

    Do not modify this method.
    """
    if left == righ:  # Base case: we are only looking at one symbol
        return True
    elif left == righ - 1:  # Base case: we are only looking at two symbols
        return S[left] == '(' and S[right] == ')'
    elif correct_bracketing(S[left + 1: right]):  # Inductive step: we look for the inner case of correct brackets
        if S[left] == '(':  # If the left symbol is a bracket, then we move one forward to find the same number of brackets
            return (S[left] == S[right]) and recursive_correct_bracketing(S, left+1, right - 1)
        elif S[left] == ')':  # If the left symbol is not a bracket, then we move two forwards to find both brackets of the same kind or the same number of brackets
            return (S[left] == S[right]) or recursive_correct_bracketing(S, left+1, right - 1)
    return False
        
 
if __name__ == '__main__':
    import doctest
    doctest.testmod()
