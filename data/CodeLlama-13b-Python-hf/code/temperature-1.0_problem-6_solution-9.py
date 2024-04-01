from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    return [parse_paren_group(paren_group) for paren_group in paren_string.split()]


def parse_paren_group(paren_group: str) -> int:
    """ Input to this function is a string represented a single group for nested parentheses.
    For this group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_paren_group('(()())')
    2
    >>> parse_paren_group('((()))')
    3
    >>> parse_paren_group('()')
    1
    >>> parse_paren_group('(())()()')
    1
    >>> parse_paren_group('(()(()))')
    3
    >>> parse_paren_group('')
    0
    """
    if not paren_group:
        return 0

    if paren_group[0] != '(' or paren_group[-1] != ')':
        raise ValueError('Parentheses are not properly balanced')

    max_depth = 0
    current_depth = 0
    for paren in paren_group:
        if paren == '(':
            current_depth += 1
        elif paren == ')':
            current_depth -= 1
        max_depth = max(max_depth, current_depth)
    return max_depth


if __name__ == '__main__':
    import doctest

    doctest.testmod()
