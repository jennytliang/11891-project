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

    def count_depth(s, current_depth, depth):
        if s == '':
            depth = current_depth
            return depth

        if s[0] == '(':
            current_depth += 1

        if s[0] == ')':
            current_depth -= 1

        return count_depth(s[1:], current_depth, depth)

    return [count_depth(s, 0, 0) for s in paren_string.split()]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
