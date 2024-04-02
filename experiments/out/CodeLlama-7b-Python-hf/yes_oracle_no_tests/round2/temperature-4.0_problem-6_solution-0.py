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

    # Find the index of the first non-whitespace character
    start = 0
    for i in range(len(paren_string)):
        if not paren_string[i].isspace():
            start = i
            break

    # Find the index of the first right parentheses
    end = len(paren_string) - 1
    for i in range(len(paren_string) - 1, 0, -1):
        if not paren_string[i].isspace():
            end = i
            break

    # Find the deepest nesting level of parentheses
    max_depth = 0
    depth = 0
    for i in range(start, end + 1):
        if paren_string[i] == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        else:
            depth -= 1

    # Split the string into substrings
    substrings = paren_string[end + 1:].split()

    # Recursively call the function on the rest of the substrings
    return [max_depth] + parse_nested_parens(substrings)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
