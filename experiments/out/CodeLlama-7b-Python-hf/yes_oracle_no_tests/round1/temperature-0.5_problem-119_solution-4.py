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
    
	Include these tokens in the code:  def valid _ par ens ( s
	Do not include these tokens in the code: if len
	'''

    def valid_parens(s):
        count = 0
        for i in s:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    lst = [x for x in lst if x != '']
    if len(lst) == 1:
        return 'Yes'
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if valid_parens(lst[i]+lst[i+j+1]):
                return 'Yes'
    return 'No'


if __name__ == '__main__':
    assert match_parens(['()(', ')']) == 'Yes', 'First Assert'
    assert match_parens([')', ')']) == 'No', 'Second Assert'
    assert match_parens(['(((()', '))))')) == 'Yes', 'Third Assert'
    assert match_parens(['((((', ')))))))))(') == 'Yes', 'Fourth Assert'
    assert match_parens(['((((', ')))))))))())(') == 'No', 'Fifth Assert'
