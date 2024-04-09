from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: max _ depth , c nt =
	Do not include these tokens in the code: Count the of the parentheses in a string
	"""

    def count_depth(s: str) -> int:
  
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
        
        return depth

    return [count_depth(s) for s in paren_string.split()]


def main():
    print(parse_nested_parens('(()()) ((())) () ((())()())'))


if __name__ == "__main__":
    main()
