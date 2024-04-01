def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    if not lst:
        return "Yes"
    elif len(lst) == 1:
        if lst[0] == '(':
            return "No"
        else:
            return "Yes"
    else:
        a = lst[0]
        b = lst[1]
        newlst = lst[2:]
    if a == '(' and b == ')':
        return match_parens(newlst)
    elif a == ')' and b == '(':
        return "No"
    else:
        return match_parens(lst[1:])

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
