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
    # Your code here
    stack = []
    for i in range(len(brackets)):
        if brackets[i] == "<":
            stack.append(i)
        elif brackets[i] == ">":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


# Simple test 1
# print(correct_bracketing("<"))

# Simple test 2
# print(correct_bracketing("<>"))

# Simple test 3
# print(correct_bracketing("<<><>>"))

# Simple test 4
# print(correct_bracketing("><<>"))

# Simple test 5
# print(correct_bracketing("<><>"))


# Harder test 1
# print(correct_bracketing("<><><>"))

# Harder test 2
# print(correct_bracketing("<<><><>"))

# Harder test 3
# print(correct_bracketing("<<><>>"))

# Harder test 4
# print(correct_bracketing("<<><>><<"))

# Harder test 5
# print(correct_bracketing("<><><><>"))

# Harder test 6
# print(correct_bracketing("<><><><><>"))

# Harder test 7
# print(correct_bracketing("<<><><><><><><><><>"))

# Harder test 8
# print(correct_bracketing("><><><><><><><><><><>"))

# Harder test 9
# print(correct_bracketing("<<><><><><><><><><><>"))

# Harder test 10
# print(correct_bracketing("<<><><><><><><><><><><><>"))

# Harder test 11
# print(correct_bracketing("<<><><><><><><><><><><><><>"))

# Harder test 12
# print(correct_bracketing("<<><><><><