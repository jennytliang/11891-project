from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    return [max(count_depth(s)) for s in paren_string.split()]


def count_depth(s: str) -> List[int]:
    """
    >>> count_depth('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Initialize stack and return list
    stack = []
    res = []

    # Traverse the Expression
    for i in range(len(s)):
        # If expression has opening paren,
        # push element onto the stack
        if s[i] == "(":
            stack.append(i)

        # If expression has closing paren,
        # pop the element from stack
        elif s[i] == ")":
            stack.pop()

            # If stack is empty, that means outermost paren has been found
            if not stack:
                res.append(i)

    return [res.index(i) + 1 for i in res]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
