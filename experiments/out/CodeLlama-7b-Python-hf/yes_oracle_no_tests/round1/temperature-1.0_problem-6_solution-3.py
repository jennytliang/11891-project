from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    paren_string = paren_string.replace(' ', '')
    levels = []
    for str_idx in range(len(paren_string)):
        if paren_string[str_idx] == '(':
            level = 1
            for idx in range(str_idx + 1, len(paren_string)):
                if paren_string[idx] == '(':
                    level += 1
                elif paren_string[idx] == ')':
                    if level == 1:
                        levels.append(idx - str_idx)
                        break
                    else:
                        level -= 1
    return levels


def main():
    print(f"Answer: {parse_nested_parens('(()()) ((())) () ((())()())')}")


if __name__ == "__main__":
    main()
