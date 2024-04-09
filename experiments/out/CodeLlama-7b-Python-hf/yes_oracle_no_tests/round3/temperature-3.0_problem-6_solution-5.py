from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    # return [count_depth(s) for s in paren_string.split()]
    return [count_depth(s) for s in paren_string.split()]


def count_depth(string: str) -> int:
    """ Counts the depth of a string of parentheses """
    if len(string) == 0:
        return 0
    if string[0] != "(":
        raise ValueError(f"String {string} does not start with '('")
    if string[-1] != ")":
        raise ValueError(f"String {string} does not end with ')'")

    depth = 0
    for paren in string:
        if paren == "(":
            depth += 1
        if paren == ")":
            depth -= 1
    return depth


if __name__ == "__main__":
    import doctest

    doctest.testmod()
