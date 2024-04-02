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
    # 1. check input
    if not paren_string or paren_string == "":
        return []

    # 2. init
    output_list = []
    paren_group = ""
    open_paren_count = 0
    close_paren_count = 0

    # 3. traverse
    for char in paren_string:
        if char == "(":
            open_paren_count += 1
        elif char == ")":
            close_paren_count += 1
        else:
            continue
        # 4. check
        if open_paren_count == close_paren_count:
            output_list.append(paren_group)
            paren_group = ""
            open_paren_count = 0
            close_paren_count = 0
        # 5. append
        paren_group += char

    # 6. return
    return output_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
