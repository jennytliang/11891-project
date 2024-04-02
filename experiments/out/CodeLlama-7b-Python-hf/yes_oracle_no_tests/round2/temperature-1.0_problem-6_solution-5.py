from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: : str ) -> int :
	Do not include these tokens in the code: ):
	"""

    def count_deeper_paren(string):
        """Takes the string, finds the position of the open paren and the closed paren and count
        how deep the nested parentheses are. Returns the deepest level of parentheses and a modified string

        If str1 = "((()())))", then str2 = ")()())" and ret_val = 4

        If str1 = "(()() ("and the rest of the string is removed, including the parens
        then str2 = "()" and ret_val = 2

        Do not include these in code: : str string -> int ret_val : : : : 2 : : : : ):
        """
        ret_val = 0
        i = 0
        stack = []

        while i < len(string) and string[i] == " ":
            i += 1

        if i != len(string):
            stack.append(string[i])
            open_paren = i
            count = 1

            while i < len(string) and stack:
                i += 1
                if string[i] == "(":
                    count += 1
                    stack.append(string[i])
                elif string[i] == ")":
                    stack.pop()
                    if len(stack) == 0:
                        ret_val = count - 1
                string = string[0:open_paren] + string[i:]

        return ret_val

    return map(lambda x: count_deeper_paren(x), paren_string.split())


class NestedParentheses:
    def maxDepth(self, s: str) -> int:
        result = nest_deeper_paren = 0
        nest_start = 0
        for i in range(len(s)):
            if s[i] == '(':
                nest_deeper_paren += 1
                if nest_deeper_paren > nest_start:
                    nest_start = nest_deeper_paren
            elif s[i] == ')':
                nest_deeper_paren -= 1
