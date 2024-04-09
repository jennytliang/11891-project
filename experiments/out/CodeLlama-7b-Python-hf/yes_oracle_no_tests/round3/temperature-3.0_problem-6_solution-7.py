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
    for group in paren_string.split():
        result.append(count_depth(group))
    return result


def count_depth(group: str) -> int:
    """
    >>> count_depth('(()()) ((())) () ((())()())')
    2
    >>> count_depth('()()')
    1
    >>> count_depth('')
    0
    """
    depth = 0
    for char in group:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
    return depth


def count_depth_optimized(group: str) -> int:
    """
    >>> count_depth('(()()) ((())) () ((())()())')
    2
    >>> count_depth('()()')
    1
    >>> count_depth('')
    0
    """
    return group.count('(') - group.count(')')


def count_depth_optimized_2(group: str) -> int:
    """
    >>> count_depth('(()()) ((())) () ((())()())')
    2
    >>> count_depth('()()')
    1
    >>> count_depth('')
    0
    """
    depth = 0
    for char in group:
        depth += 1 if char == '(' else -1
        if depth < 0: return 0
    return depth


if __name__ == '__main__':
    import doctest

    doctest.testmod()
