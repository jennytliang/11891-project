def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """

    # s0 = list(filter((lambda s: s!= ' '), s0))   #removes spaces in string

    s1= list(filter((lambda s: s != ' '), list(s1)))
    check = list(filter((lambda s: s != ' '), list(s0)))
    check_sort = sorted(sorted(check), reverse=True)    #sort alphabetically so last letter is in first postion
    check_length = len(check)

    for ind, i in enumerate(check_sort):
        try:
            i_pop = s1.index(i)
            s1_rm = s1.remove(i)
            check_rm = check.pop(ind)
        except ValueError as e: #if check contains extra letter
            print(e)
            return check_length

    return 0 if len(set(check_sort) - set(s1)) > 0 else f'{check_length} of {len(check_sort)}'      #if 0 then they have same characters. If more than zero, check letter


def main():
    s0 = 'eabdcd' #'bcad'     #string to check. should be short in case of error
    target = False
    print(f'string0 = \'{s0}\'')

    with open('404.md', 'r+', newline='\n') as f:
        s = f.readlines()[65].rstrip()
        target = True if (isinstance(same_chars(s, s0), int) or same_chars(s,s0) == str(0)) else False  #if we have a list
        result = f"{'is' if target else 'isn\'t'} match"
        print(f'string0 = \'{s}\' -- {result}. ')

    print('All done !')
""" def is_check(s1: str, s0 : str): #test if string0 is inside another string
        s1s = list(filter((lambda s: not s.startswith('<div'), list(s1.split('.')[1]))))"""

# string0 is inside another string?
""" def is_tester(check):   #test if string0 is in string
        for el in check:
             try:
                 if el <= len(string0)-1:
                    string1[-(len(check)-((len(check))+el))] <= string0 <= string1[-el]"""

