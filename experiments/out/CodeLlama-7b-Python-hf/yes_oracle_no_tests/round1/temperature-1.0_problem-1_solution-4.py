from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group , results =
	"""
    results = []
    group = ""
    open_brace_count = 0
    for i in paren_string:
        if i.isspace() or i == ")":
            pass
        elif i == "(":
            open_brace_count = open_brace_count + 1
        if open_brace_count == 0:
            results.append(group)
            group = ""
        group = group + i
        if i == ")":
            open_brace_count = open_brace_count - 1
            if open_brace_count < 0:
                raise Exception(
                    "Braces do not match in the string, open_brace_count < 0")
    return results


if __name__ == "__main__":
    paren_string = "(((((((( (( )( )) ) ) ) ) ) ) )) )"
    print(separate_paren_groups(paren_string))
