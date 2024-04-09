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
    
	Include these tokens in the code: par ens
	Do not include these tokens in the code: pa ired
	'''



    def parens_match(s):
        '''
        This function takes a string as input and returns True if the
        parentheses in the string match, and False otherwise.
        '''
        return s.count('(') == s.count(')')

    def parens_balanced(s):
        '''
        This function takes a string as input and returns True if the
        parentheses in the string are balanced, and False otherwise.
        '''
        return parens_match(s) and s.count('())') == 0

    def parens_concat(s1, s2):
        '''
        This function takes two strings as input and returns a new string
        that is the result of concatenating the two strings in some order.
        '''
        return s1 + s2


    lst_len = len(lst)
    lst_lst = []
    lst_lst_len = 0
    lst_lst_len_max = 0
    lst_lst_elem = ''
    lst_lst_elem_max = ''

    lst_lst_len_max = 2**lst_len
    lst_lst = ['' for x in range(lst_lst_len_max)]

    for i in range(lst_lst_len_max):
        lst_lst[i] = bin(i)[2:].zfill(lst_len)

    for i in lst_lst:
        for j in lst_lst:
            lst_lst_elem = i + j
            if parens_balanced(lst_lst_elem):
                lst_lst_elem_max = lst_lst_elem

    return lst_lst_elem_max


print(match_parens(['()(', ')']))
print(match_parens([')', ')']))
print(match_parens(['()()()', '()()()']))
print(match_parens(['(()','))']))























































