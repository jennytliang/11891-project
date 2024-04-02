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
	Do not include these tokens in the code: n t
	"""

    # write some checks for strings that may be false
    if brackets == "":
        return True

    elif brackets.count("<") < brackets.count(">"):
        return False

    elif brackets.count("|") > 0:
        return False

    c_count = brackets.count("<")
    n_count = brackets.count(">")
    n_c = 0

    c_ind = 0
    n_ind = 0

    while n_count > 0:
        c_ind = brackets.find("<", c_ind)
        n_ind = brackets.find(">", n_ind)
        if c_ind < n_ind:
            c_count = c_count - 1
            c_ind += 1

        elif c_ind >= n_ind:
            n_count = n_count - 1
            n_ind += 1


    if c_count == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()