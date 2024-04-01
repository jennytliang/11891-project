from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Return a list of output after parsing every group of strings.
    output = [
        max(
            1 + (index, row.count('(') + 1).index(value) 
            for value in (row.count(")") + 1, index),
            key=lambda pair: pair[0]
        ) - (row.count(")") + 1, index) * 1
        for index, row in enumerate(paren_string.split())
    ][0]

    return output


test_input = ' ((())) () ((())()())'
test_ans = 2 + max(1 + (index, row.count('(')).index(value)
                # + 1 to convert the count from [0, 0, 1, 2, 2] to index from [1, 2, 3, 4] because the starting value to check for max is always start with the ending parens with 1 as base value, to compensate the ending paren from 0 indexing we added +1 so that the value will be [0,1,1]
                 # .index means that we are iterating and checking the index in the list of count values depending on the target value and index value, then the lambda value is to pick the closest parenthese that will be removed


