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

    # c is the number of closing brackets
    # n is the number of opening brackets
    c = 0
    n = 0
    for i in brackets:
        if i == ">":
            c += 1
        else:
            n += 1
    return c == n


# print(correct_bracketing("<>"))
# print(correct_bracketing("<"))
# print(correct_bracketing("<<><>>"))
# print(correct_bracketing("><<>"))

def replace_char(string: str, index: int, char: str):
    """ string is a string of length at least 1.
    index is an int where 0 <= index < len(string).
    char is a string of length 1.
    return a string where the char has been inserted at index in string.

    >>> replace_char("ab", 1, "c")
    'a[c]b'
    >>> replace_char("ab", 0, "c")
    '[c]b'
    >>> replace_char("ab", 2, "c")
    'ac[c]'
    >>> replace_char("ab", 2, "cd")
    'ac[cd]'
    >>> replace_char("ab", 2, "cd")
    'ac[cd]'
    >>> replace_char("ab", 2, "cd")
    'ac[cd]'

	Include these tokens in the code: c slicing =
	"""

    # c is the string of length 1 to insert
    c = char
    return string[:index] + c + string[index:]


# print(replace_char("ab", 1, "c"))
# print(replace_char("ab", 0, "c"))
# print(replace_char("ab", 2, "c"))
# print(replace_char("ab", 2, "cd"))
# print(replace_char("ab", 2, "cd"))
# print(replace_char("ab", 2, "cd"))

def remove_char(string: str, index: