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
    lst1 = lst1[:]  # make a copy of the list so we don't change what is given
    lst2 = lst2[:]  # make a copy of the list so we don't change what is given
    total1 = 0
    for l in lst1:
        total1 += len(l)

    total2 = 0
    for l in lst2:
        total2 += len(l)

    if total1 == total2:
        lst1.sort()
        return lst1
    elif total1 < total2:
        lst1.sort()
        return lst1
    else:
        lst2.sort()
        return lst2


print(total_match([], []))
# >> []
