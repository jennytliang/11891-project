from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    return [count_depth(paren) for paren in paren_string.split(' ')]


def count_depth(paren_str: str):
    """ For this input function get a string of only one 'N' character (number of parenthes(e/es/es) ). Return the max
    depth of the parentheses.

    >>> count_depth('((((((())(((()))))()))()()()()()())())')
    6
    """
    max_depth, depth = 1, 1
    for paren in paren_str * 2:
        if paren == '(':
            depth += 1
        elif paren == ')':
            depth -= 1
        if depth > max_depth:
            max_depth = depth
    return max_depth


if __name__ == '__main__':
    print(parse_nested_parens('(()()) ((())) () ((())()())'))
    print(count_depth('((((((())(((()))))()))()()()()()())())'))
    import doctest

    doctest.testmod()
