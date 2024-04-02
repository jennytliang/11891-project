from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    groups = paren_string.split(' ')
    return [count_depth(group) for group in groups]


def count_depth(group: str) -> int:
    """ Count the deepest level of nesting of parentheses in the string """
    depth = 0
    for char in group:
        if char == '(':
            depth += 1
        if char == ')':
            depth -= 1
    return depth


def test_count_depth():
    assert count_depth('(()())') == 2
    assert count_depth('()()()') == 1
    assert count_depth('((()))') == 3


if __name__ == '__main__':
    print(parse_nested_parens('(()()) ((())) () ((())()())'))
