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

    # for each loop in the string
    #   create a nested parsing function
    for group in paren_string.split():
        mycount = 0
        mydepth = 0
        def count_depth(my_string, my_count, my_depth):
            for x in my_string:
                if x == '(':
                    my_count += 1
                    my_depth = my_depth + 1
                    count_depth(my_string, my_count, my_depth)
                elif x == ')':
                    my_depth = my_depth - 1
                    my_count += 1
            output.append(my_count)
            return my_count
        count_depth(group, mycount, mydepth)
    return output
