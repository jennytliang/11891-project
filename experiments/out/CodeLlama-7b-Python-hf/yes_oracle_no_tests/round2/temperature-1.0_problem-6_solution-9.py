from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    return [get_deepest_nesting(group) for group in paren_string.split()]


def get_deepest_nesting(paren_string: str) -> int:
    """
    >>> get_deepest_nesting('(()()) ((())) () ((())()())')
    3
    """
    if len(paren_string) < 2:
        return 0
    max_depth = 0
    depth = 0
    for c in paren_string:
        if c == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif c == ')':
            depth -= 1
    return max_depth


def parse_nested_parens_v2(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens_v2('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    return [get_deepest_nesting_v2(group) for group in paren_string.split()]


def get_deepest_nesting_v2(paren_string: str) -> int:
    """
    >>> get_deepest_nesting_v2('(()()) ((())) () ((())()())')
    3
    """
    if len(paren_string) < 2:
        return 0
    max_depth = 0
    depth = 0
    for c in paren_string:
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        max_depth = max(max_depth, depth)
    return max_depth


if __name__ ==