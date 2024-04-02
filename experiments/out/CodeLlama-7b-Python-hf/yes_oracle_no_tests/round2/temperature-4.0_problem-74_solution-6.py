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
	Do not include these tokens in the code: # pass char _ count
	'''
    
    lst1_set= set(lst1)
    lst2_set= set(lst2)
    
    if len(lst1) > len(lst2):
        return [i for i in lst1 if len(i) <= len(lst2)]
    
    elif len(lst2) > len(lst1):
        return [i for i in lst2 if len(i) <= len(lst1)]
    
    else:
        return lst1
    
    
    
    
def total_match_2(lst1, lst2):
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
	Do not include these tokens in the code: # pass char _ count
	'''
    
    lst1_set= set(lst1)
    lst2_set= set(lst2)
    
    if len(lst1) > len(lst2):
        return [i for i in lst1 if len(i) <= len(lst2)]
    
    elif len(lst2) > len(lst1):
        return [i for i in lst2 if len(i) <= len(lst1)]
    
    else:
        return lst1
    
    
    
    
def total_match_3(lst1, lst2