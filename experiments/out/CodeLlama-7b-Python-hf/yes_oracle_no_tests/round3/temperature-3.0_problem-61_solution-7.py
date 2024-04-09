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
    # c is the index of the last opening bracket
    # n is the number of opening brackets encountered
    # t is the number of closing brackets encountered
    n, t = 0, 0
    # 1. initialize n and t to 0
    c = -1
    # 2. start scanning the input string from left to right
    for i in range(len(brackets)):
        # 3. if the current character is "("
        if brackets[i] == "(":
            # 4. increment n
            n += 1
        # 5. if the current character is ")"
        if brackets[i] == ")":
            # 6. increment t
            t += 1
            # 7. if n = 0
            if n == 0:
                # 8. return False
                return False
            # 9. decrement n
            n -= 1
        # 10. if n > 0
        if n > 0:
            # 11. if the current character is ")"
            if brackets[i] == ")":
                # 12. increment c
                c += 1
    # 13. if n > 0
    if n > 0:
        # 14. return False
        return False
    # 15. if t > c + 1
    if t > c + 1:
        # 16. return False
        return False
    # 17. return True
    return True


# print(correct_bracketing("("))
# print(correct_bracketing("()"))
# print(correct_bracketing("(()())"))
# print(correct_bracketing(")(()"))
# print(correct_bracketing("(()))"))
