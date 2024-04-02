from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    def count_depth(s):
        paren_depth, max_depth = 0, 0
        for paren in s:
            paren_depth = paren_depth + 1 if paren == "(" else paren_depth - 1
            max_depth = paren_depth if paren_depth > max_depth else max_depth
        return max_depth

    return [count_depth(s) for s in paren_string.split()]

if __name__ == '__main__':
    str_list = '(()()) ((())) () ((())()())'.split()
    print(f'String list: \n {str_list} \n')
    for s in str_list:
        print(f"For the string {s}:")
        print(f"{parse_nested_parens(s)}")

    print(parse_nested_parens('(()()) ((())) () ((())()())'))

    # import doctest
    # doctest.testmod()