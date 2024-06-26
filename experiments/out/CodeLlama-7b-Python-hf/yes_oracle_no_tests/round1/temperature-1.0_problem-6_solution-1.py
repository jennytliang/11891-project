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
    """ Counts the deepest level of nesting of parentheses in a string.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> count_depth('(()()) ((())) () ((())()())')
    3
    """
    if len(s) == 0:
        return 0
    if s[0] != '(':
        raise ValueError(f'{s} is not a valid string')
    return 1 + count_depth(s[1:]) if s[1] == '(' else 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
