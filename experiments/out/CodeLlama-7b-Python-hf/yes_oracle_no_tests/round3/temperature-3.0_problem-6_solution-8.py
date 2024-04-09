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
    for paren_group in paren_string.split():
        result.append(count_depth(paren_group))
    return result


def count_depth(paren_string: str) -> int:
    """ Calculate the deepest level of nesting of parentheses for a given string
    >>> count_depth('(()()) ((())) () ((())()())')
    3
    """
    depth = 0
    for paren in paren_string:
        if paren == '(':
            depth += 1
        elif paren == ')':
            depth -= 1
    return depth


if __name__ == '__main__':
    import doctest

    doctest.testmod()
