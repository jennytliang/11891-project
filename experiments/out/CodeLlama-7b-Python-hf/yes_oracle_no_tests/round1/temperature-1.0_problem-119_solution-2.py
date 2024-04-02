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
        count = 0
        for i in s:
            if i == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0

    # your code here
    lst = ['(*(', '*)*']
    result = "Yes"
    for i in range(len(lst)):
        for j in range(len(lst)):
            new1 = lst[i]
            new2 = lst[j]
            if i == j:
                continue
            else:
                new = new1+new2
                if valid_parens(new):
                    pass
                else:
                    result = "No"

    return result
if __name__ == '__main__':
    print("Example:")
    print(match_parens(['(*(', '*)*)']))
    print(match_parens(["(())"]))
    print(match_parens(["(()", "(())))"]))
    print(match_parens(["(*)", "(*"])

    # These "asserts" are used for self-checking and not for an auto-testing
    assert match_parens(["(*(", "*)*)"] == "Yes")
    assert match_parens(["(*(", "*)*)))"] == "No")
    assert match_parens(["()"] == "Yes")
    assert match_parens(["(*)"] == "Yes")
    assert match_parens(["*())"] == "No")
    assert match_parens(["(()", "(*)))"] == "No")
    assert match_parens(["(*)", "(*") == "No")
    print("Coding complete? Click 'Check' to earn cool rewards!")



'''
def match_parens(lst):
    i=0
    while i < len(lst):    # iterates through the whole string each time
        if lst[i:i+2] == ["(",")"] or lst[i:i+2] == ["[","]"] or lst[