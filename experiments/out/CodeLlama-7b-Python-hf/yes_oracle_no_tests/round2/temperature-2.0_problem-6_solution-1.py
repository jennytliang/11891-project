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
    >>> count_depth('(()())')
    2
    >>> count_depth('((()))')
    3
    """
    depth = 0
    max_depth = 0
    for i in range(len(s)):
        if s[i] == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif s[i] == ')':
            depth -= 1
    return max_depth


if __name__ == "__main__":
    import doctest

    doctest.testmod()
