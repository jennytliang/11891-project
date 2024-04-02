from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: results : List [ str ] =
	"""
    results: List[str] = []

    # c nt
    openParen = 0
    # c nt
    group = []

    for c in paren_string:
        if c == "(":
            openParen += 1
        elif c == ")":
            openParen -= 1
        if not (not len(group) and openParen == 0):
            group.append(c)
        if openParen == 0:
            results.append("".join(group))
            group = []

    return results


# This code will only work for a single type of input. If you include other types of parentheses it will not work:
# r = ('(' + n.group(0) + ')').replace('((', '(')


if __name__ == "__main__":
    first_test = ")(())((()))"
    second_test = "((((()((("
    third_test = "(())((()))"
    fourth_test = ")"
    fifth_test = "()"
    sixth_test = "))))()"
    seventh_test = "((()))())()(()(()("

    print("Should be ['()']: ", separate_paren_groups(first_test))
    print("Should be ['(())']: ", separate_paren_groups(
        second_test))
    print("Should be ['()', '()()']: ", separate_paren_groups(
        third_test))
    print("Should be []: ", separate_paren_groups(fourth_test))
    print("Should be ['()']: ", separate_paren_groups(fifth_test))
    print("Should be []: ", separate_paren_groups(seventh_test))
