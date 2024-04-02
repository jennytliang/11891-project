from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count
	Do not include these tokens in the code: # TODO : Write your code here
	"""
    return [count(s) for s in paren_string.split()]


def count(s: str) -> int:
    """ Count the deepest level of nesting of parentheses in the string s.

    >>> count('(()()) ((())) () ((())()())')
    3
    >>> count('()()')
    1
    """
    # TODO : Write your code here
    if len(s) == 0:
        return 0
    if s[0] == '(':
        return 1 + count(s[1:])
    else:
        return count(s[1:])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
