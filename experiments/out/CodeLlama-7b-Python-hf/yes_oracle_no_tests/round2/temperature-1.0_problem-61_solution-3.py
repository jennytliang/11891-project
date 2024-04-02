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
    
	Do not include these tokens in the code: #
	"""


def find_matching_bracket(start: str, brackets: str):
    """ Return the index of the matching  bracket

    >>> find_matching_bracket('(', '([(5+3)-2])')
    14
    >>> find_matching_bracket(')', '([(5+3)-2])')
    >>> find_matching_bracket('[', '([(5+3)-2])')

	Do not include these tokens in the code: #
    
	"""


def is_matched(expression: str):
    """ return True if all the brackets in expression are matched
        Return False otherwise.
    >>> is_matched('([(5+3)-2])')
    True
    >>> is_matched('[(5+3)-2]')
    False
    
	Do not include these tokens in the code: #

    """
