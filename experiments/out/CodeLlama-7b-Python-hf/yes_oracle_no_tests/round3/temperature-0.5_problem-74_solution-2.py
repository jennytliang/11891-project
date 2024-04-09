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
    
    # set up empty lists to append to
    lst1_total = []
    lst2_total = []
    lst1_total_chars = 0
    lst2_total_chars = 0
    
    # iterate through each item in lst1
    for i in lst1:
        
        # add the length of the item to the total
        lst1_total_chars += len(i)
        
        # append the item to lst1_total
        lst1_total.append(i)
        
    # iterate through each item in lst2
    for i in lst2:
        
        # add the length of the item to the total
        lst2_total_chars += len(i)
        
        # append the item to lst2_total
        lst2_total.append(i)
        
    # if lst1 has more chars than lst2, return lst1_total
    if lst1_total_chars > lst2_total_chars:
        return lst1_total
    
    # if lst2 has more chars than lst1, return lst2_total
    elif lst2_total_chars > lst1_total_chars:
        return lst2_total
    
    # otherwise, return lst1_total
    else:
        return lst1_total
    