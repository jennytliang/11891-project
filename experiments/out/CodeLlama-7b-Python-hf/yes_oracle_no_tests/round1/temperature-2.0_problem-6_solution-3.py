from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    # TODO: Write your code here

    # return [count_depth(s) for s in paren_string.split()]
    return [count_depth(s) for s in paren_string.split()]


def count_depth(s: str) -> int:
    """
    Input to this function is a string representing a group for nested parentheses.
    Output the deepest level of nesting of parentheses.

    >>> count_depth('(()())')
    2
    >>> count_depth('((()))')
    3
    >>> count_depth('()()()')
    1
    """
    # TODO: Write your code here
    depth = 0
    max_depth = 0
    for char in s:
        if char == '(':
            depth += 1
            max_depth = max(depth, max_depth)
        elif char == ')':
            depth -= 1

    return max_depth


if __name__ == '__main__':
    import doctest

    doctest.testmod()
