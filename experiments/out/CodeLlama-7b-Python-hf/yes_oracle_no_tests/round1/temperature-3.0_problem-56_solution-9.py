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
    # 1. Keep track of how many opening brackets you've seen
    # 2. Keep track of how many closing brackets you've seen
    # 3. If you see a closing bracket, check that you haven't seen that many opening brackets yet
    # 4. If you see an opening bracket, increment the number of opening brackets you've seen
    # 5. If you see a closing bracket, decrement the number of opening brackets you've seen
    # 6. Return True if you've seen as many closing brackets as opening brackets after you've processed the whole string

    # 1. Keep track of how many opening brackets you've seen
    nt = 0
    # 2. Keep track of how many closing brackets you've seen
    ct = 0

    # 3. If you see a closing bracket, check that you haven't seen that many opening brackets yet
    # 4. If you see an opening bracket, increment the number of opening brackets you've seen
    for i in range(len(brackets)):
        if brackets[i] == "<":
            nt += 1
        elif brackets[i] == ">":
            ct += 1
            if nt < ct:
                return False
        else:
            return False

    return nt == ct


print(correct_bracketing("<"))
print(correct_bracketing("<>"))
print(correct_bracketing("<<><>>"))
print(correct_bracketing("><<>"))
