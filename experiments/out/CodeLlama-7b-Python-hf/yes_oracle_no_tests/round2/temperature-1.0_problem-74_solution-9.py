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
	lst_new_1 = []
  
	lst_new_2 = []

	for i in lst1:
		lst_new_1.append(len(i))
	    
	for j in lst2:
	   lst_new_2.append(len(j))

	if lst_new_1[0]<lst_new_2[0]:
	  return(lst1)

	if lst_new_1 == lst_new_2:
	  return(lst1)


	return(lst2)



total_match(['121','4'], ['124','12'])