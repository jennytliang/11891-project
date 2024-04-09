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


def count_depth(string: str) -> int:
    """
    >>> count_depth('(())')
    2
    >>> count_depth('(()())')
    3
    """
    depth = 0
    for char in string:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
    return depth


if __name__ == "__main__":
    import doctest

    doctest.testmod()
