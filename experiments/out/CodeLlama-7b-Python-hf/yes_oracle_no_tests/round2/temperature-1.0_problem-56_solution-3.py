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

    # c stands for counter
    # n stands for nested
    c = 0
    # n stands for nested
    n = False

    # for char in given brackets string,
    # compare each character to correct closing bracket
    for char in brackets:
        # if char == "<"
        # increase c by 1 and set n to True
        # and return False if c == 0
        if char == "<":
            c += 1
            n = True
            if c == 0:
                return False
        # if char == ">" and n is True
        # n is set to False and if c == 0
        # return False else decrease c
        if char == ">" and n is True:
            n = False
            if c == 0:
                return False
            c -= 1
    # finally
    # if c == 0, return True, else return False
    if c == 0:
        return True
    return False



def main():
    import doctest
    doctest.testmod()
    s = input("enter string separated by spaces for bracket balancing::")
    print(correct_bracketing(s))


if __name__ == "__main__": main()