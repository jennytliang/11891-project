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
    
	Include these tokens in the code: c 1 , c 2 =
	Do not include these tokens in the code: return list ( filter ( lambda x
	'''
    
    if lst1 == []:
        return []
    
    elif lst1 == lst2:
        return lst1
    
    else:
        lst1_sum = 0
        lst2_sum = 0

        for i in lst1:
            lst1_sum += len(i)
        for i in lst2:
            lst2_sum += len(i)

        if lst1_sum == lst2_sum:
            return lst1

        elif lst1_sum < lst2_sum:
            return lst1

        else:
            return lst2


def total_match1(lst1, lst2):
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
    
	Include these tokens in the code: c 1 , c 2 =
	Do not include these tokens in the code: return list ( filter ( lambda x
	'''
    
    if lst1 == []:
        return []
    
    elif lst1 == lst2:
        return lst1
    
    else:
        lst1_sum = 0
        lst2_sum = 0

        for i in lst1:
            lst1_sum += len(i)
        for i in lst2:
            lst2_sum += len(i)

        if lst1_