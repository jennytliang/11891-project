from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: max _ depth , c nt = 0 ,
	Do not include these tokens in the code: if s == ' ': return
	"""


    def count_depth(s: str) -> int:
 
        cnt = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
            if cnt == 0:
                return i

    return [count_depth(s) for s in paren_string.split()]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
