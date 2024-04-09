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
    
	Include these tokens in the code: : str ) -> bool :
	Do not include these tokens in the code: ):
	'''

    def valid_parens(s):
        stack = []
        for c in s:
            if c == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

    def check_parens(lst):
        str1 = lst[0]
        str2 = lst[1]
        if valid_parens(str1 + str2):
            return 'Yes'
        elif valid_parens(str2 + str1):
            return 'Yes'
        else:
            return 'No'

    return check_parens(lst)


print(match_parens(['()(', ')']) == 'Yes')
print(match_parens([')', ')']) == 'No')
