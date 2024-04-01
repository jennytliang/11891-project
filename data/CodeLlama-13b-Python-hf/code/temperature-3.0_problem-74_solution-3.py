def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    
    def str_chars_num(s1, s2):
        s1 = list(filter(None, s1))
        if len(s1) > len(s2):
            return len(''.join(s1))
        else:
            return len(''.join(s2))

    if len(lst1) == 0 and len(lst2) == 0:
        return []
    elif str_chars_num(lst1, lst2) == str_chars_num(lst2, lst1):
        return lst1
    elif str_chars_num(lst1, lst2) < str_chars_num(lst2, lst1):
        return lst1
    return lst2
