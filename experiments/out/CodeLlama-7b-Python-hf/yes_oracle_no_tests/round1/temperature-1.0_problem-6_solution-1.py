from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""

    # this is a recursive function that passes the index of the last character
    # if parentheses is open, then it is a "deep" paren
    depth = []

    def count_depth(s, last):
        """ this takes in a string and last char"""
        nonlocal depth
        for i, char in enumerate(s):
            if i == last:
                return depth[0]
            if char == '(':
                depth.append(0)
            elif char == ')':
                if i > last:
                    depth[len(depth) - 1] +=1
            count_depth(s, last+1)

    return count_depth(paren_string, 0)


if __name__ == "__main__":
    print(
        "The biggest depth of nesting for each of the group in parenthesis. E.g. () --> 0, )((() --> 1 ",
    )
    print(parse_nested_parens('(()()) ((())) () ((())()())'))
