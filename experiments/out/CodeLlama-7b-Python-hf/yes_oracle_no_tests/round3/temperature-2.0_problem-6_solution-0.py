from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: max _ depth , c nt = 0 ,
	"""

    def count_depth(s: str) -> int:
  
        nonlocal max_depth
        if s == '(':
            cnt += 1
            max_depth = max(max_depth, cnt)
        elif s == ')':
            cnt -= 1
        return max_depth

    max_depth = 0
    cnt = 0
    return [count_depth(s) for s in paren_string.replace(' ', '')]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
