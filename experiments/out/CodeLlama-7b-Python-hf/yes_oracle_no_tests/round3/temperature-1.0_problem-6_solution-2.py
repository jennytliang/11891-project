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
  
	# cnt = 0
	# for i in s:
	#     if i == '(':
	#         cnt += 1
	#     elif i == ')':
	#         cnt -= 1
	#     if cnt < 0:
	#         cnt = 0
	# return cnt

        # max_depth = 0
        # for i in s:
        #     if i == '(':
        #         max_depth += 1
        #     elif i == ')':
        #         max_depth -= 1
        #     if max_depth < 0:
        #         max_depth = 0
        # return max_depth

        # cnt = 0
        # for i in s:
        #     if i == '(':
        #         cnt += 1
        #     elif i == ')':
        #         cnt -= 1
        #     if cnt < 0:
        #         cnt = 0
        # return cnt

        cnt = 0
        max_depth = 0
        for i in s:
            if i == '(':
                cnt += 1
            elif i == ')':
                cnt -= 1
            if cnt > max_depth:
                max_depth = cnt
        return max_depth

    return [count_depth(s) for s in paren_string.split()]


def parse_nested_parens_2(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens_2('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]

    """

    def count_depth(s: str) -> int:
        # max_depth = 0
        # for i in