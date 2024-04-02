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
    if not lst: return 'No'
    if len(lst) == 1: return 'No'
    if not lst[0]: return 'No'
    if not lst[1]: return 'No'

    result=[]
    result.append(calc(lst[0],lst[1]))

    if(result):
       return 'Yes'
    else:
        return 'No'


result=[]
def calc(token1,token2):
    final='('+token1+token2+')'
    final=final.replace('()','')

    if(final==''):
        return True
    else:
        return False


if __name__ == '__main__':
	a= [('(()',')))'])
	print(match_parens(a))
    
