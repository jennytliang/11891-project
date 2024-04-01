from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    result = []
    for paren_group in paren_string.split():
        curr = 0
        nested = 0
        for paren in paren_group:
            if paren == '(':
                curr += 1
                if curr > nested:
                    nested = curr
            else:
                curr -= 1
        result.append(nested)
    return result

