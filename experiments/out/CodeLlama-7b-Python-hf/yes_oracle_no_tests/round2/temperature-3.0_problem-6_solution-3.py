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


def count_depth(s: str) -> int:
    """ Input to this function is a string representing a group of nested parentheses.
    Output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
    
    >>> count_depth('(()()) ((())) () ((())()())')
    3
    """
    counter = 0
    max_counter = 0
    for c in s:
        if c == '(':
            counter += 1
            if counter > max_counter:
                max_counter = counter
        elif c == ')':
            counter -= 1
    return max_counter


if __name__ == '__main__':
    import doctest

    doctest.testmod()
