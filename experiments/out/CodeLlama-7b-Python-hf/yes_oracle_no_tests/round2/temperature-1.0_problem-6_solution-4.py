from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    def count_depth(s: str) -> int:
        """ Count the depth of the parentheses in a string. 
        >>> count_depth('(()())')
        2
        >>> count_depth('((((()))))')
        4
        """
        return s.count('(') - s.count(')')

    return [count_depth(s) for s in paren_string.split()]


def parse_nested_parens_optimized(paren_string: str) -> List[int]:
    """ Same as above but using the built-in function max.

    >>> parse_nested_parens_optimized('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    return [max(s.count('('), s.count(')')) for s in paren_string.split()]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
