from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    return [count_depth(s) for s in paren_string.split(" ")]


def count_depth(s: str) -> int:
    """Returns the deepest level of nesting of parentheses in the string s
    
    >>> count_depth('(()()) ((())) () ((())()())')
    3
    >>> count_depth('((((()))))')
    4
    >>> count_depth('((((((())))))))')
    6
    >>> count_depth('()')
    1
    >>> count_depth('')
    0
    """
    if len(s) == 0:
        return 0
    count = 0
    max_count = 0
    for c in s:
        if c == "(":
            count += 1
            max_count = max(max_count, count)
        elif c == ")":
            count -= 1
    return max_count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
