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
    
	Include these tokens in the code: c 1 , c 2 = sum ( map (
	'''
    
    if lst1 == [] or lst2 == []:
        return []
    else:
        lst1 = list(map(lambda x: sum(map(lambda y: len(y), x)), lst1))
        lst2 = list(map(lambda x: sum(map(lambda y: len(y), x)), lst2))
        for i in range(len(lst1)):
            for j in range(len(lst2)):
                if lst1[i] < lst2[j]:
                    return lst1
                elif lst1[i] > lst2[j]:
                    return lst2
                else:
                    return lst1
