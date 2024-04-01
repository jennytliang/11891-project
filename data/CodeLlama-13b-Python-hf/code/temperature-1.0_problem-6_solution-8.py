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

    max_level = 0
    current_level = 0
    for char in paren_group:
        if char == '(':
            current_level += 1
        elif char == ')':
            current_level -= 1
        max_level = max(max_level, current_level)
    return max_level


if __name__ == '__main__':
    import doctest

    doctest.testmod()
