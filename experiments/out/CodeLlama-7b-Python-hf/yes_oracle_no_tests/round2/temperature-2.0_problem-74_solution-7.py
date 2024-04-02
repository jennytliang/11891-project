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
    lst1 = lst1.split()
    lst2 = lst2.split()
    lst1 = list(map(len, lst1))
    lst2 = list(map(len, lst2))
    if sum(lst1) < sum(lst2):
        return lst1
    elif sum(lst1) > sum(lst2):
        return lst2
    else:
        return lst1


# total_match('hi admin', 'hI Hi') #, ['hI', 'Hi']
# total_match('hi admin', 'hi hi admin') #, ['hi', 'admin']
# total_match('hi admin', 'hi hi hi') #, ['hi', 'hi', 'hi']
# total_match('hi admin', 'hI hi hi') #, ['hI', 'hi', 'hi']
# total_match('hi admin', 'hI hi hi admin') #, ['hI', 'hi', 'hi']
# total_match('hi admin', 'hI hi admin') #, ['hI', 'hi', 'admin']
# total_match('hi admin', 'hI admin') #, ['hI', 'admin']
# total_match('hi admin', 'hI') #, ['hI']
# total_match('4', '1 2 3 4 5') #, ['4']
# total_match('4', '1 2 3 4 5 6') #, ['1', '2', '3', '4', '5', '6']
# total_match('4', '1 2 3 4') #, ['4']
# total_match('4', '1 2 3 4 6') #, ['1', '2', '3', '4', '6']
# total_match('4', '1 2 3 5') #, ['1', '2', '3', '5']
# total_match('4', '1 2 3 5 6') #, ['1', '2', '3', '5', '6']
# total_match('hi', 'hi') #, ['hi']
# total_