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
    # your code here
    stack = []
    for c in brackets:
        if c == '<':
            stack.append(c)
        elif c == '>':
            if stack:
                stack.pop()
            else:
                return False
    return not stack


def correct_bracketing_2(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_2("<")
    False
    >>> correct_bracketing_2("<>")
    True
    >>> correct_bracketing_2("<<><>>")
    True
    >>> correct_bracketing_2("><<>")
    False
    
	Do not include these tokens in the code: #
	"""
    # your code here
    return not any(brackets.count(c) % 2 for c in '<>')


def main():
    import doctest
    doctest.testmod()
    print(correct_bracketing('<<><>>'))
    print(correct_bracketing('><<>'))


if __name__ == '__main__':
    main()