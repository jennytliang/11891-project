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

    # --------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # --------------------------------------------------------------------------
    nt = 0
    group = ""
    results = []

    for ch in paren_string:
        if ch == '(':
            nt += 1
            group += ch
        elif ch == ')':
            nt -= 1
            group += ch
            if nt == 0:
                results.append(group)
                group = ""
        else:
            group += ch

    return results


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------

def main():
    test1 = '( ) (( )) (( )( ))'
    print(separate_paren_groups(test1))


    test2 = '((((((()))))))'
    print(separate_paren_groups(test2))

    test3 = '()()'
    print(separate_paren_groups(test3))

    test4 = '(()()'
    print(separate_paren_groups(test4))

    test5 = ''
    print(separate_paren_groups(test5))

    test6 = '((())'
    print(separate_paren_groups(test6))

    test7 = '((())())'
    print(separate_paren_groups(test7))

    test8 = '((())())'
    print(separate_paren_groups(test8))


main()
