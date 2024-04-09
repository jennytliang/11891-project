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
	Do not include these tokens in the code: # Your code here
	"""
    # c = count of opening brackets
    c = 0
    # nt = count of closing brackets
    nt = 0
    # if count of opening brackets is greater than count of closing brackets
    # then return False
    if c > nt:
        return False
    # if brackets is empty
    if brackets == "":
        return True
    # if the first character is "("
    if brackets[0] == "(":
        # increase count of opening brackets
        c += 1
    # if the first character is ")"
    if brackets[0] == ")":
        # increase count of closing brackets
        nt += 1
    # if the first character is "("
    if brackets[0] == "(":
        # call correct_bracketing function with brackets[1:]
        return correct_bracketing(brackets[1:])
    # if the first character is ")"
    if brackets[0] == ")":
        # call correct_bracketing function with brackets[1:]
        return correct_bracketing(brackets[1:])


print(correct_bracketing("(()())"))
print(correct_bracketing(")("))
print(correct_bracketing(")()()("))
print(correct_bracketing("((()))"))
print(correct_bracketing("(((((((("))
