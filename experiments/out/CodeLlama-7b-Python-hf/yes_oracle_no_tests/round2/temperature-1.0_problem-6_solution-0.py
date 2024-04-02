from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count
	Do not include these tokens in the code: return [( bal - open
	"""
    nested_parened = paren_string.split(" ")
    return [max((bal - open) for open, bal in zip("()(", nested_parened))]


if __name__ == "__main__":
    print(
        sorted(parse_nested_parens('(()()) ((())) () ((())()())'))
    )
