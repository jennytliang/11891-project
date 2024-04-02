from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    return [max(count_depth(s, c) for c in '()') for s in paren_string.split()]


def count_depth(s: str, c: str) -> int:
    return sum(c in s for s in s.split())


print(parse_nested_parens('(()()) ((())) () ((())()())'))
