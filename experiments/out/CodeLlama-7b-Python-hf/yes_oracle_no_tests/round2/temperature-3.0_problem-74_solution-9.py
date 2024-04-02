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
	lst1_total_chars = 0
	lst2_total_chars = 0
	
	for i in lst1:
		lst1_total_chars += len(i)
	for j in lst2:
		lst2_total_chars += len(j)
	
	if lst2_total_chars < lst1_total_chars:
		return lst2
	elif lst1_total_chars < lst2_total_chars:
		return lst1
	else:
		return lst1
