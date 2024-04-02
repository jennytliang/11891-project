from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: nt , group , results
	"""

    # Initialize variables
    # nt is the number of parentheses we have to balance
    nt = 0
    # group is the string we are currently working on
    group = ""
    # results is the final list of groups
    results = []

    for char in paren_string:
        # if char is "(" increase nt
        if char == "(":
            nt += 1
        # if char is ")" decrease nt
        elif char == ")":
            nt -= 1
        # if char is "(" and nt is 0, we have found a new group
        if char == "(" and nt == 0:
            # add the previous group to the results
            results.append(group)
            # reset group
            group = ""
            # increase nt
            nt += 1
        # add char to group
        group += char
    # add the final group to the results
    results.append(group)

    return results


def main():
    print(separate_paren_groups('( ) (( )) (( )( ))'))


if __name__ == "__main__":
    main()
