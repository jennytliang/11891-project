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
    # pass
    l1 = set([x for i in lst1 for x in i])
    l2 = set([x for i in lst2 for x in i])
    if len(l1) == len(l2):
        return lst1
    if len(l1) > len(l2):
        return lst2
    return lst1


# total_match(['hi', 'admin'], ['hI', 'Hi']) #➞ ['hI', 'Hi']
# total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) #➞ ['hi', 'admin']
# total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) #➞ ['hI', 'hi', 'hi']
# total_match(['4'], ['1', '2', '3', '4', '5']) #➞ ['4']
# total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) #➞ ['hi', 'admin']
total_match([], [])
print('----------------------------------------------------------------------')
# ---------------------------------------------------------------------
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
    
	Include these tokens in the code: c 1