from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    output = []
    for group in paren_string.split(" "):
        output.append(count_depth(group))
    return output


def count_depth(paren_string: str) -> int:
    """ Input to this function is a string that contains only parentheses.
    Output the deepest level of nesting of parentheses.
    
    >>> count_depth('()')
    1
    >>> count_depth('(()()) ((())) () ((())()())')
    3
    """
    max_depth = 0
    depth = 0
    for char in paren_string:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        max_depth = max(max_depth, depth)
    return max_depth


if __name__ == "__main__":
    import doctest
    doctest.testmod()
