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
	Do not include these tokens in the code: opening
	"""
    # c = opening bracket count
    # nt = closing bracket count
    c = 0
    nt = 0
    for i in brackets:
        if i == "(":
            c += 1
        else:
            nt += 1
    if c == nt:
        return True
    else:
        return False



def main():
    print(correct_bracketing("()"))
    print(correct_bracketing("((())))"))
    print(correct_bracketing("(((())))"))
    print(correct_bracketing(")"))


if __name__ == "__main__":
    main()
