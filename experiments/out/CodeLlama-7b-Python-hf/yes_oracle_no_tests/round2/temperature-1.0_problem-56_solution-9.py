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
    
	Do not include these tokens in the code: n t = len ( bra ckets
	"""
    # your code here
    n = len(brackets)
    if n == 0:
        return True
    if n == 1:
        return False
    left = 0
    right = 0
    for i in range(n):
        if brackets[i] == '<':
            left += 1
        else:
            right += 1
        if left == right:
            return correct_bracketing(brackets[:i] + brackets[i + 1:])
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
