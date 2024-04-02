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
    """ Input to this function is a string representing a group of nested parentheses.
    Output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
    """
    count = 0
    max_count = 0
    for char in string:
        if char == "(":
            count += 1
            max_count = max(max_count, count)
        elif char == ")":
            count -= 1
    return max_count


def test_count_depth():
    assert count_depth("(()())") == 2
    assert count_depth("((()))") == 3
    assert count_depth("(((())))") == 4


if __name__ == "__main__":
    import doctest

    doctest.testmod()
