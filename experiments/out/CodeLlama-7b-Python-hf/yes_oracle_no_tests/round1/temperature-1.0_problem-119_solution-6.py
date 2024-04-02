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
    
	Include these tokens in the code: def valid _ par ens ( s : str )
	'''
    
    assert(lst[0][1]=='(')
    assert(lst[1][0]==')')
    
    def valid_parens(string):
        count = 0
        for c in string:
            if c == '(': count += 1
            if c == ')': 
                if count > 0: count -= 1
                else:return False
        return count == 0

    if valid_parens(lst[0][1]+lst[1]):
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
   l = [('()(','()')]
   print(match_parens(l))