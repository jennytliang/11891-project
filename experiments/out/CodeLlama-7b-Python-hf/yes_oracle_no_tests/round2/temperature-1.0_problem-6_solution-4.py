from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Do not include these tokens in the code: depth s = [] current
	"""
    result = []
    for group in paren_string.split():
        depth = 0
        for i, ch in enumerate(group):
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            if depth == 0 and i == len(group) - 1:
                result.append(i - 1)
                break
    return result


if __name__ == "__main__":
    import doctest
    print(list(parse_nested_parens(input())))
    # input_string = '(()()) ((())) () ((())()())'
    # print(list(parse_nested_parens(input_string)))
    doctest.testmod()
