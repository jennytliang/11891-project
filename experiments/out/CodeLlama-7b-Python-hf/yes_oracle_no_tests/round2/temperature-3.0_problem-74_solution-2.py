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
    
	Include these tokens in the code: c
	'''
    total_chars = 0
    for i in lst1:
        for j in i:
            total_chars += 1
    for i in lst2:
        for j in i:
            total_chars += 1
    if total_chars == 0:
        return []
    count = 0
    if lst1[0] == lst2[0]:
        return lst1
    elif len(lst1) == len(lst2):
        for i in lst1:
            for j in i:
                count += 1
        for i in lst2:
            for j in i:
                count += 1
        if count > total_chars:
            return lst1
        else:
            return lst2
    elif total_chars == 0:
        return []
    else:
        for i in lst1:
            for j in i:
                count += 1
        if count > total_chars:
            return lst2
        else:
            return lst1
