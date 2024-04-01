from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    return sum([1 for c in list(s[0].count('(') + 2) for s in paren_string.split() if c % 2]) // 2


if __name__ == "__main__":
    print(list(parse_nested_parens('(()()) ((())) () () (())()())))(((((((((()))))))()())()(()()))))')))')))())())())))(()()))) ((())) ()(()))))))))()((((')))