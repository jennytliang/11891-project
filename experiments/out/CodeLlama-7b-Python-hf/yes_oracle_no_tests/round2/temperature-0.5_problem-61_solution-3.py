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
    
	Include these tokens in the code: c nt =
	"""
    # 1. If the string is empty, return True.
    # 2. If the first character is "("
    # 2a. If the last character is ")" return True
    # 2b. Else return False
    # 3. Else return False
    # 4. Repeat the procedure, starting with the first and last characters of the string
    # 5. If the string is not empty, return False
    if brackets == "":
        return True
    if brackets[0] == "(":
        if brackets[-1] == ")":
            return True
        else:
            return False
    else:
        return False


print(correct_bracketing("("))
print(correct_bracketing("()"))
print(correct_bracketing("(()())"))
print(correct_bracketing(")(()"))
