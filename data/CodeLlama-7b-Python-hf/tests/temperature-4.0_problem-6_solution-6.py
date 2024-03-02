from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def count_level(chars):
        # Base cases
        # We start by counting the first parentheses and reducing 1 point to the result to eliminate the first parenthesis.
        # Then if we have 2 or higher points, we go deeper into this function by reducing the number of parenthesis by the same number from the result.
        # Then if we have even number of parenthesis, we go back to the next base case for the reduced string.

        result = 1
        for character in chars:
            if character == ')':
                result += 1
            # Check if the string has more than 1 closing parentheses.
            if result > 1:
                result -= 1

            if result == 0:

                # If there is a zero points we have counted all the
                # nested brackets and need to return the counter back to base case.
                break
            if character == '(':
                # If we have equal number of parenthesis we can return since we've now counted them correctly
                # if there is only one parentheses.
                if result == 1:
                    return
                # The number of nested brackets is still increasing, we must continue counting.
                else:
                    result -= 1

    return [count_level(parenstring) for parenstring in paren_string.split(' ')]






METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]


check(parse_nested_parens)