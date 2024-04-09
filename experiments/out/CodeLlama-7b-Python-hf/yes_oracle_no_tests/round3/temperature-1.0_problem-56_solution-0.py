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
    stack = []
    for c in brackets:
        if c == '<':
            stack.append(c)
        if c == '>':
            if stack == []:
                return False
            else:
                stack.pop()
    return stack == []


def main():
    print(correct_bracketing("<>"))
    print(correct_bracketing("<<><>>"))
    print(correct_bracketing("><<>"))
    print(correct_bracketing(""))
    print(correct_bracketing(">"))
    print(correct_bracketing("<<>"))
    print(correct_bracketing("<><>"))
    print(correct_bracketing("<><>>"))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()