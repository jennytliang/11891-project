from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    output = []
    for paren_group in paren_string.split():
        max_depth = 0
        for char in paren_group:
            if char == '(':
                max_depth += 1
            elif char == ')':
                max_depth -= 1
        output.append(max_depth)
    return output


def main():
    test_string = '(()()) ((())) () ((())()())'
    output = parse_nested_parens(test_string)
    print(output)


if __name__ == '__main__':
    main()
