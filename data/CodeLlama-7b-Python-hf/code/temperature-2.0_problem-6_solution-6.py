from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_depth = [0] * len(paren_string)
    for i, char in enumerate(paren_string):
        if char == '(':
            max_depth[i] = 1 + max_depth[i - 1] if i > 0 else 1
        elif char == ')':
            max_depth[i] = max_depth[i - 1] - 1
    return max_depth


if __name__ == '__main__':
    print(parse_nested_parens('(()()) ((())) () ((())()())'))
