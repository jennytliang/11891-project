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

    def valid_paren_string(string):
        """
        This function uses a stack to check if a valid
        string of parentheses is passed

        Precondition: string consists of only ( and ) 
        and string is not empty
        """
        counter = 0
        stack = []
        for paren in string:
            if stack and paren == '(':
                stack.pop()
            else:
                stack.append(paren)
                counter += 1
        
        return 'Yes' if counter == 0 else 'No'

    string1 = lst[0];
    string2 = lst[1];

    return valid_paren_string(string1 + string2)

if __name__ =='__main__':
    print ("Pass" if (match_parens(['()(', ')'])) == 'Yes' else "Fail")
    print ("Pass" if (match_parens(['()(','&']) == 'No') else "Fail")
    print ("Pass" if (match_parens([')','(']) == 'No') else "Fail")
