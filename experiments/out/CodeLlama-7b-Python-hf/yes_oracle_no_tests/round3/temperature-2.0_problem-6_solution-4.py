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
    """
    >>> count_depth('(()()) ((())) () ((())()())')
    3
    """
    stack = []
    for character in string:
        if character == '(':
            stack.append(character)
        elif character == ')':
            if stack:
                stack.pop()
            else:
                return 0
    return len(stack)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
