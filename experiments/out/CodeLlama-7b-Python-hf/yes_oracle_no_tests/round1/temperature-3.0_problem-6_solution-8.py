from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    return [count_depth(group) for group in paren_string.split()]


def count_depth(paren_string: str) -> int:
    """ Input to this function is a string representing a group for nested parentheses
    Output the deepest level of nesting of parentheses
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
    """
    depth = 0
    for paren in paren_string:
        if paren == '(':
            depth += 1
        elif paren == ')':
            depth -= 1
    return depth


def count_depth_stack(paren_string: str) -> int:
    """ Input to this function is a string representing a group for nested parentheses
    Output the deepest level of nesting of parentheses
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
    """
    depth = 0
    stack = []
    for paren in paren_string:
        if paren == '(':
            stack.append(depth)
            depth += 1
        elif paren == ')':
            depth = stack.pop()
    return depth


def main():
    print(parse_nested_parens('(()()) ((())) () ((())()())'))


if __name__ == '__main__':
    main()
