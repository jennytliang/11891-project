from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code:   def count _ depth ( s
	Do not include these tokens in the code: # TODO : implement your solution here
	"""

    # TODO : implement your solution here
    def count_depth(s):
        counter = 0
        for c in s:
            if c == '(':
                counter += 1
            elif c == ')':
                counter -= 1
        return counter

    return [count_depth(s) for s in paren_string.split()]
