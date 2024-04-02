from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: max _ depth , c nt
	Do not include these tokens in the code: Count the of parentheses by iter ating over
	"""

    def count_depth(s: str) -> int:
  
        if s == '':
            return 0
        elif s[-1] == ')':
            return count_depth(s[:-1]) + 1
        else:
            return count_depth(s[:-1])
    
    return [count_depth(s) for s in paren_string.split(' ')]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
