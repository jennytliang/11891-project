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

    def valid_parens(string_to_test):
        open_paren = 0
        close_paren = 0
        for i in string_to_test:
            if i == '(':
                open_paren += 1
            elif i == ')':
                close_paren += 1
            if open_paren < close_paren:
                return False
        return open_paren == close_paren

    def concat_strings(string_one, string_two):
        string_one_copy = string_one[:]
        string_two_copy = string_two[:]
        concat_string = ''
        while len(string_one_copy) != 0 and len(string_two_copy) != 0:
            concat_string += string_one_copy[0]
            concat_string += string_two_copy[0]
            string_one_copy = string_one_copy[1:]
            string_two_copy = string_two_copy[1:]
        return concat_string

    def check_valid_parens(string_one, string_two):
        concat_string = concat_strings(string_one, string_two)
        return valid_parens(concat_string)

    if len(lst) != 2:
        return 'No'
    if valid_parens(lst[0]) == False or valid_parens(lst[1]) == False:
        return 'No'
    if check_valid_parens(lst[0], lst[1]) == True:
        return 'Yes'
    else:
        return 'No'


def main():
    print('All tests passed: ' + str(match_parens(['()(', ')']) == 'Yes'))
    print('All tests passed: ' + str(match_parens([')(', ')']) == 'No'))


if __name__ == '__main__':
    main()
