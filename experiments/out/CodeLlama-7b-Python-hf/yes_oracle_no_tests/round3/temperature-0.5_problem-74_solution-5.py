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
    return lst1 if sum(map(len, lst1)) < sum(map(len, lst2)) else lst2


# lst1 = ['hi', 'admin']
# lst2 = ['hI', 'Hi']
# lst3 = lst1 if sum(map(len, lst1)) < sum(map(len, lst2)) else lst2
# print(lst3)
# print(total_match(lst1, lst2))
# print(total_match([], []))
# print(total_match(['hi', 'admin'], ['hI', 'Hi']))
# print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
# print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))
# print(total_match(['4'], ['1', '2', '3', '4', '5']))