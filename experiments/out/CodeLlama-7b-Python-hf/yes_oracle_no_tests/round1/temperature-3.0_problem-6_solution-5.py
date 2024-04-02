from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    result = []
    for group in paren_string.split():
        result.append(count_depth(group))
    return result


def count_depth(paren_string: str) -> int:
    """ Counts the deepest level of nesting of parentheses for the given string.

    >>> count_depth('(()()) ((())) () ((())()())')
    3
    >>> count_depth('() () ((())) ()')
    2
    >>> count_depth('(())((()())(()(())))')
    4
    """
    if len(paren_string) == 2:
        return 0

    deepest_depth = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            depth = 1 + count_depth(paren_string[i+1:])
            if depth > deepest_depth:
                deepest_depth = depth
    return deepest_depth


def main():
    import doctest
    doctest.testmod()

    s = '(()()) ((())) () ((())()())'
    print(parse_nested_parens(s))


if __name__ == '__main__':
    main()
