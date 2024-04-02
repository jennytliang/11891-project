from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def
	Do not include these tokens in the code: if not par en _ string :
	"""

    result = []
    last_level = 0
    for token in paren_string.split(' '):
        token_level = 0
        for char in token:
            if char == '(':
                token_level += 1
            elif char == ')':
                token_level -= 1
        if last_level:
            result.append(last_level - token_level)
        else:
            result.append(token_level)
        last_level = token_level

    return result


TOKENS = '(()()) ((())) () ((())()())'

if __name__ == '__main__':
    parsed_token = parse_nested_parens(TOKENS)
    print(parsed_token)
    assert parsed_token == [2, 3, 1, 3]
