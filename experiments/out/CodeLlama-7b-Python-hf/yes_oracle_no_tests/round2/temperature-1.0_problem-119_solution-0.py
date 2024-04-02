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

    def valid_parens(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            if char == ')':
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    def rec_solve(list1, list2):
        n = len(list1)
        m = len(list2)
        t, t_ = [], []
        # Recursive Step.
        for i in range(n):
            for j in range(m):
                t.append(list1[i] + list2[j])
                t_.append(list2[j] + list1[i])

        # Base step.
        for element in t:
            if valid_parens(element):
                return 'Yes'
        for element in t_:
            if valid_parens(element):
                return 'Yes'

        # If there is no solution then return.
        return 'No'

    # Driver Code.
    return rec_solve(lst[0], lst[1])

print(match_parens(['()(', ')']) == 'Yes')
print(match_parens([')', ')']) == 'No')
print(match_parens(['((((((())))', ')']) == 'No')

