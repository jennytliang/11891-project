from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    return [count_depth(s) for s in paren_string.split()]


def count_depth(s: str) -> int:
    if s[0] != '(' or s[-1] != ')':
        raise ValueError(f'Invalid paren_string: {s}')
    return count_depth_helper(s, 0)


def count_depth_helper(s: str, depth: int) -> int:
    if len(s) == 1:
        return depth
    if s[0] == '(':
        return count_depth_helper(s[1:], depth + 1)
    else:
        return count_depth_helper(s[1:], depth)
