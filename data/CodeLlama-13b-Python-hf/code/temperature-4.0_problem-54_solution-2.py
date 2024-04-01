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

    return 0 if len(set(check_sort) - set(s1)) > 0 else f'{check_length} of {len(check_sort)}'      #if 0 then they have same characters