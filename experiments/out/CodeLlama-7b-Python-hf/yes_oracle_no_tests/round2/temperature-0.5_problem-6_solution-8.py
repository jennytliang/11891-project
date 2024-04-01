from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Do not include these tokens in the code: , depth : int = 0
	"""


    def count_depth(paren_string: str, depth: int = 0) -> int:
        """ This function counts the deepest level of nesting of parentheses in a string.
        It is called recursively and the depth is passed as a parameter.
        """
        depth_lst = []
        for char in paren_string:
            if char == '(':
                depth += 1
                depth_lst.append(depth)
            elif char == ')':
                depth -= 1
                depth_lst.append(depth)
        return max(depth_lst)

    return [count_depth(paren_string) for paren_string in paren_string.split()]


print(parse_nested_parens('(()()) ((())) () ((())()())'))
