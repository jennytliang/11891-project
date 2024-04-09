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
    
	Include these tokens in the code: c nt =
	"""

    # c: counter
    # n: number of opening brackets
    # t: type of brackets
    c, n, t = 0, 0, brackets[0]
    if t == "<":
        n += 1
    else:
        return False

    for i in range(1, len(brackets)):
        if brackets[i] == t:
            c += 1
        else:
            if n == c:
                t = brackets[i]
                n += 1
            else:
                c -= 1
    return (n == c)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
