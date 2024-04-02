from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Do not include these tokens in the code: # this is a recursive function
	"""

    """
    def parse_nested_parens(self, s, stack=[]):
        if not s:
            return len(stack) - 1
        char = s[-1]
        if char == ")":
            stack.pop(-1)
        else:
            stack.append(char)
        return self.parse_nested_parens(s[:-1], stack)
    """

    stack = []
    str_to_analyze = paren_string
    longest_stack = []
    while str_to_analyze:
        char = str_to_analyze[-1]
        if char == ")":
            stack.pop(-1)
        else:
            stack.append(char)
        str_to_analyze = str_to_analyze[:-1]
    for item in longest_stack:
        if item in set("("):
            longest_stack.append(longest_stack.index(item)+1)
    

    return longest_stack

str_to_analyze = '()()) ((())) () ((())()())'
print(parse_nested_parens(str_to_analyze))
    