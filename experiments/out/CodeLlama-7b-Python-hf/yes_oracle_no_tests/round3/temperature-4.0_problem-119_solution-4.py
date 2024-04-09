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
    
	Include these tokens in the code: s : str ) -> bool :
	Do not include these tokens in the code: string ):
	'''


    def valid_paretheses(s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack == []:
                    return False
                else:
                    stack.pop()
        return stack == []

    def is_good(s1, s2):
        return valid_paretheses(s1 + s2)

    if lst[0] == ')' or lst[1] == '(':
        return 'No'
    else:
        return 'Yes' if is_good(lst[0], lst[1]) else 'No'
