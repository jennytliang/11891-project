from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group ,
	"""
    groups = []
    current_group = ""
    n = len(paren_string)
    open_paren_count = 0
    for i in range(n):
        if paren_string[i] == "(":
            open_paren_count += 1
        elif paren_string[i] == ")":
            open_paren_count -= 1
        if open_paren_count == 0:
            groups.append(current_group)
            current_group = ""
        elif i == n - 1:
            current_group += paren_string[i]
            groups.append(current_group)
        else:
            current_group += paren_string[i]
    return groups


if __name__ == "__main__":
    input_string = input("Enter a string containing multiple groups of nested parentheses: ")
    groups = separate_paren_groups(input_string)
    for group in groups:
        print(group)
