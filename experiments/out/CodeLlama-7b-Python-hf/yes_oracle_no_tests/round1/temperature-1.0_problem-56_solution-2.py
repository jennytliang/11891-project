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

    c = brackets.count('<')
    nt = brackets.count('>')
    if c-nt != 0:
        return False
    return True
def contains_2w(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if the string contains "><" as a substring

    >>> contains_2w("<")
    False
    >>> contains_2w("<>")
    False
    >>> contains_2w("><")
    True
    >>> contains_2w("<><")
    True
    """
    

    return str(brackets).find('><') != -1

# def correct_bracketing(brackets: str):
#     """ brackets is a string of "<" and ">".
#     return True if every opening bracket has a corresponding closing bracket.
    
#     >>> correct_bracketing("<")
#     False
#     >>> correct_bracketing("<>")
#     True
#     >>> correct_bracketing("<<><>>")
#     True
#     >>> correct_bracketing("><<>")
#     False
#     """
    

#     c = brackets.count('<')
#     nt = brackets.count('>')
#     if c-nt != 0:
#         return False
#     return True
# def contains_2w(brackets: str):
#     """ brackets is a string of "<" and ">".
#     return True if the string contains "><" as a substring

#     >>> contains_2w("<")
#     False
#     >>> contains_2w("<>")
#     False
#     >>> contains_2w("><")
#     True
#     >>> contains_2w("<><")
#     True
#     """
    

#     if str(brackets).find('><') != -1:
#         return True
#     return False
# def has_2_watson(str):
#     return str.find("Brian") != -1
