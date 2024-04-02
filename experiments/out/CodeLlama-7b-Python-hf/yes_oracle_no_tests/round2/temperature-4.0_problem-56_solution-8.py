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

    # c = opening bracket
    # n = closing bracket
    # t = true

    # cnt = 0
    # for b in brackets:
    #     if b == "<":
    #         cnt += 1
    #     if b == ">":
    #         cnt -= 1
    # return cnt == 0

    # if brackets[0] == "<":
    #     return False
    # if brackets[len(brackets) - 1] == ">":
    #     return False

    # cnt = 0
    # for i in range(len(brackets)):
    #     if brackets[i] == "<":
    #         cnt += 1
    #     if brackets[i] == ">":
    #         cnt -= 1
    #     if cnt < 0:
    #         return False
    # return cnt == 0

    # cnt = 0
    # for b in brackets:
    #     if b == "<":
    #         cnt += 1
    #     if b == ">":
    #         cnt -= 1
    #     if cnt < 0:
    #         return False
    # return cnt == 0

    # cnt = 0
    # for b in brackets:
    #     if b == "<":
    #         cnt += 1
    #     if b == ">":
    #         cnt -= 1
    #     if cnt < 0:
    #         return False
    # return cnt == 0

    # cnt = 0
    # for i in range(len(brackets)):
    #     if brackets[i] == "<":
    #         cnt += 1
    #     if brackets[i] == ">":
    #         cnt -= 1
    #     if cnt < 0:
    #         return False
    # return cnt == 0

    cnt = 0
    for i in range(len(brackets)):
        if brackets[i] == "<":