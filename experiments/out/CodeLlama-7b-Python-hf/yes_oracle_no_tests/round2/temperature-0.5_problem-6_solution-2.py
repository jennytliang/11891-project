from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    result = []
    for group in paren_string.split(' '):
        result.append(count_depth(group))
    return result


def count_depth(s: str) -> int:
    """ Input to this function is a string represented a group for nested parentheses.
    Output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> count_depth('(()()) ((())) () ((())()())')
    3
    """
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
