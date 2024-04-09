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
	Do not include these tokens in the code: total
	'''
    # pass
    # total = 0
    # for i in lst1:
    #     for j in i:
    #         total += ord(j)
    # for i in lst2:
    #     for j in i:
    #         total += ord(j)
    # if total == 0:
    #     return []
    # elif total > 0:
    #     return lst1
    # else:
    #     return lst2
    
    total = 0
    for i in lst1:
        for j in i:
            total += ord(j)
    for i in lst2:
        for j in i:
            total -= ord(j)
    if total > 0:
        return lst1
    elif total < 0:
        return lst2
    else:
        return []
    

print(total_match(['hi', 'admin'], ['hI', 'Hi']))
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))
print(total_match(['4'], ['1', '2', '3', '4', '5']))