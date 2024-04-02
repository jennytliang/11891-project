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
    """
    >>> count_depth('()')
    2
    >>> count_depth('()()((())())')
    4
    >>> count_depth('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if len(s) == 0:
        return 0
    if s[0] != '(':
        raise ValueError(f'String should start with open parentheses: {s}')
    if s[-1] != ')':
        raise ValueError(f'String should end with close parentheses: {s}')
    if '(' not in s and ')' not in s:
        return 1
    return 2 + count_depth(s[1:-1])


if __name__ == '__main__':
    import doctest

    doctest.testmod()
