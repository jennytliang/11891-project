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
	Do not include these tokens in the code: opening
	"""
    # cnt = 0
    # for b in brackets:
    #     if b == "<":
    #         cnt += 1
    #     if b == ">":
    #         cnt -= 1
    # return cnt == 0
    # return len([c for c in brackets if c == ">"]) == len([c for c in brackets if c == "<"])
    return brackets.count(">") == brackets.count("<")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
