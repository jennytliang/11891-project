from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    res = []

    for group_paren_string in paren_string.split():
        res.append(1 + count_depth(group_paren_string, '('))
    return res


def count_depth(paren_string: str, paren_symbol: str) -> int:
    d = 0
    for p in paren_string:
        if p == '(':
            d += 1
        elif p == ')':
            d -= 1
    return d


def clean_parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    return [1 + count_depth(group_paren_string, '(') for group_paren_string in paren_string.split()]


def clean_parse_nested_parens_pythonic(paren_string: str) -> List[int]:
    """ We can do it even more pythonically since all I want out is list of counts """
    return [1 + count_depth(group_paren_string, '(') for group_paren_string in paren_string.split()]


def test_two_sum():
    """Example test cases"""
    assert parse_nested_parens('(()())  ((())) () ((())()())') == [2, 3, 1, 3]


if __name__ == "__main__":
    print(parse_nested_parens('(()())  ((())) () ((())()())'))
    print(clean_parse_nested_parens_pythonic('(()())  ((())) () ((())()())