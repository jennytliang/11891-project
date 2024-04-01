from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Do not include these tokens in the code: # TODO : implement your solution
	"""
    return [
        max(
            [
                len(x)
                for x in paren_string.replace("(", "(((").split("(((")[1:][:-1].split(")" * (len(x) - 1))
                for x in paren_string.replace(")", ")))").split(")))")[1:][:-1].split("(" * (len(x) - 1))
            ]
        )
        for paren_string in paren_string.split()
    ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
