from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    depths = []
    current_depth = 0

    def count_depth(depth: int, string: str) -> int:
        nonlocal current_depth

        for character in string:
            if character == "(":
                current_depth += 1
            elif character == ")":
                current_depth -= 1

            depth = max(depth, current_depth)

        return depth

    for group in paren_string.split():
        depths.append(count_depth(0, group))

    return depths


test_string = '(()()) ((())) () ((())()())'
test_string2 = '((((())(())))(())()()))'

# # uncomment to test sub-functions
# assert count_depth(0, test_string) == 2
# assert count_depth(0, test_string2) == 4

# test parse_nested_parens
# print(parse_nested_parens(test_string))  # [2, 3, 1, 3]
# print(parse_nested_parens(test_string2))  # [5, 2]
print(parse_nested_parens(input()))
