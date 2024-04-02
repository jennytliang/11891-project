from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    def count_level(s: str) -> int:
        level = 0
        for char in s:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
        return level
    return [count_level(group) for group in paren_string.split()]


# Submission
def parse_nested_parens_submission(paren_string):
    """ This method takes string as input, parses into groups of parentheses separated by spaces
    and then parses each group of parentheses to count the nested parentheses.
    Output returned as list of nested parentheses in each group, as list of integers.
    """
    # break up string into the individual groups of parentheses separated by white space
    p_string = paren_string.split()

    # create a list to hold the depth of each group
    depth_list = []

    # initialize a count for the deepest level of parentheses
    deepest = 0

    # loop through the groups of parentheses with length
    for str_counter in range(0, len(p_string)):
        # find the length of the string
        len_str = len(p_string[str_counter])
        # loop through the string
        for char_counter in range(0, len_str):
            if p_string[str_counter][char_counter] == "(":
                # increment the count of the parentheses
                deepest += 1
            elif p_string[str_counter][char_counter] == ")":
                # decrement the count of the parentheses
                deepest -= 1
        # add the deepest number of parentheses to the list
        depth_list.append(deepest)
        # reset the count to 0
        deepest = 0

    # return the list with the deepest number of parenthesis for each string
    return depth_list


# Test Trunk
test_parens = "(()()) ((())) () ((())()())"
print('Test 1:')
print(parse_nested_parens(test_parens))
print('\n')
print('Test 2: