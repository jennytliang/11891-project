from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: : str ) -> int : max
	Do not include these tokens in the code: , current
	"""


    def count_difference(paren_string):
        if len(paren_string) == 0:
            return 0

        if paren_string[0] == '(':
            return 1 + count_difference(paren_string[1:])
        else:
            return count_difference(paren_string[1:])

    return [count_difference(paren_string) for paren_string in paren_string.split(' ')]


def parse_nested_parens_stack(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens_stack('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: : str ) -> int : max
	Do not include these tokens in the code: , current
	"""

    def count_difference(paren_string):
        stack = []
        for paren in paren_string:
            if paren == '(':
                stack.append(paren)
            else:
                stack.pop()
        return len(stack)

    return [count_difference(paren_string) for paren_string in paren_string.split(' ')]


def parse_nested_parens_stack_2(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens_stack('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: :