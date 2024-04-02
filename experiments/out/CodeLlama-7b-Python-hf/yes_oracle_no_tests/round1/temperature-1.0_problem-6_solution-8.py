from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    new_list = []
    for val in paren_string.split():
        paren = ['']
        for i, x in enumerate(val):
            if x ==  '(':
                paren.append('*')
            if x ==  ')':
                paren = paren[1:]
        new_list.append(len(paren))
    #print(new_list)
    return new_list


def main():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert parse_nested_parens("((((((()))))))") == [7]
    assert parse_nested_parens("((()()) ((())) () ((())()())") == [2, 3, 1, 3]


if __name__ == "__main__":
    main()
