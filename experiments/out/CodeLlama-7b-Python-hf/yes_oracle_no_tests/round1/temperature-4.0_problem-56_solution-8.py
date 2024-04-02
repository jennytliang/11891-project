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
    return True


def count_brackets(brackets: str):
    """ brackets is a string of "<" and ">".
    return the number of opening brackets minus the number of closing brackets.

    >>> count_brackets(">")
    0
    >>> count_brackets("<")
    1
    >>> count_brackets("<<><>>")
    0
    >>> count_brackets("><<>")
    -2
    
	Include these tokens in the code: c nt =
	"""
    return 0


def remove_outward_brackets(brackets: str):
    """ brackets is a string of "<" and ">".
    return a string that removes all pairs of outermost brackets.

    >>> remove_outward_brackets("><")
    ''
    >>> remove_outward_brackets("<><><><>")
    '<><><><>'
    >>> remove_outward_brackets("><<>")
    '<>'
    >>> remove_outward_brackets("<><<>")
    '<><>'
    
	Include these tokens in the code: c nt =
	"""
    return ""


def remove_innermost_brackets(brackets: str):
    """ brackets is a string of "<" and ">".
    return a string that removes the innermost brackets.

    >>> remove_innermost_brackets("><")
    '><'
    >>> remove_innermost_brackets("<><><><>")
    '<><><>'
    >>> remove_innermost_brackets("><<>")
    '><'
    >>> remove_innermost_brackets("<><<>")
    '<><>'
    
	Include these tokens in the code: c nt =
	"""
    return ""


def remove_outermost_pair(brackets: str):
    """ brackets is a string of "<" and ">".
    return a string with the outermost pair of brackets removed.

    >>> remove_outermost_pair("><")
    '<>'
    >>> remove_outermost_pair("<><><><>")
   