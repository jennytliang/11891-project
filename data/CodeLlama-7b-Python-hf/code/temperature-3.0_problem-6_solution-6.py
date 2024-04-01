from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    depth = 0
    result = []
    for elem in paren_string.split():
        depth_elem = 0
        for parenth in elem:
            if parenth == "(":
                depth_elem += 1
            elif parenth == ")":
                depth_elem -= 1

        depth = max(depth, depth_elem)
        result.append(depth)
    return result

