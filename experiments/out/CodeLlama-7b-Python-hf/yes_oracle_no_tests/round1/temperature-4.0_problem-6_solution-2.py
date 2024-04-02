from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    return [count_depth(group) for group in paren_string.split()]


def count_depth(paren_string: str) -> int:
    """
    >>> count_depth('(()()) ((())) () ((())()())')
    3
    >>> count_depth('(())')
    1
    >>> count_depth('')
    0
    """
    if len(paren_string) == 0:
        return 0
    if paren_string[0] != '(':
        raise ValueError('Must start with (')
    if paren_string[-1] != ')':
        raise ValueError('Must end with )')
    return 1 + count_depth(paren_string[1:-1])


if __name__ == '__main__':
    import doctest

    doctest.testmod()
