from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Return a list of output after parsing every group of strings.
    output = [
        max(
            1 + (index, row.count('(') + 1).index(value) 
            for value in (row.count(")") + 1, index),
            key=lambda pair: pair[0]
        ) - (row.count(")") + 1, index) * 1
        for index, row in enumerate(paren_string.split())
    ][0]

    return output

