from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    if not paren_string:
        return []
    max_depth = 0
    for token in paren_string.split():
        d = count_depth(token)
        if d > max_depth:
            max_depth = d
    return [max_depth] * len(paren_string.split())


def count_depth(s: str) -> int:
    """
    >>> count_depth('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
    """
    open_count = 0
    depth = []
    for c in s:
        if c == '(':
            open_count += 1
        elif c == ')':
            open_count -= 1

        if open_count < 0:
            raise ValueError('There are too many closing parentheses')

        depth.append(open_count)

    if open_count:
        raise ValueError('There are unmatched opening parentheses')
    return max(depth)


def parse_nested_parens_opt(s: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens_opt('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    if not s:
        return []
    paren_groups = count_subs(s)
    depth_groups = map(count_depth, paren_groups)
    return list(map(max, depth_groups))


def count_subs_alt(s):
    paren_groups = []
    last_idx = 0
    while last_idx < len(s):
        open_paren_count = 0
        for idx,