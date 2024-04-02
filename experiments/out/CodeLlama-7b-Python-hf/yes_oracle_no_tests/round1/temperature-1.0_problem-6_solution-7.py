from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    return [count_max_depth(s) for s in paren_string.split()]


def count_max_depth(s: str) -> int:
    """
    Return the maximum depth of the parentheses in the string s
    """
    if s == '':
        return 0
    max_depth = 0
    depth = 0
    for c in s:
        if c == '(':
            depth += 1
            max_depth = max(depth, max_depth)
        elif c == ')':
            depth -= 1
    return max_depth


def parse_nested_parens_alt(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens_alt('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    return [count_max_depth_alt(s) for s in paren_string.split()]


def count_max_depth_alt(s: str) -> int:
    """
    Return the maximum depth of the parentheses in the string s
    """
    if s == '':
        return 0
    depth = 0
    for c in s:
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
    return depth


if __name__ == '__main__':
    import doctest

    doctest.testmod()
