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
	Do not include these tokens in the code: string _ to _ test ):
	'''


    def valid_pairs(s1, s2):
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True


    def balanced(s):
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                if len(stack) == 0:
                    return False
                if stack.pop() != '(':
                    return False
        return len(stack) == 0


    def match_parens(lst):
        s1 = lst[0]
        s2 = lst[1]
        if valid_pairs(s1, s2):
            return 'Yes'
        if valid_pairs(s2, s1):
            return 'Yes'
        return 'No'

    return match_parens(lst)


print(match_parens(['()(', ')']))
print(match_parens([')', ')']))
