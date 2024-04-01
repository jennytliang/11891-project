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


    def total_match(lst1, lst2):
        if len(lst1) > len(lst2):
            return lst1
        elif len(lst2) > len(lst1):
            return lst2
        else:
            return lst1
    return total_match(lst1, lst2)


# lst1 = ['hi', 'admin']
# lst2 = ['hI', 'Hi']
# lst3 = ['hi', 'hi', 'admin', 'project']
# lst4 = ['hI', 'hi', 'hi']
# lst5 = ['4']
# lst6 = ['1', '2', '3', '4', '5']

# print(total_match(lst1, lst2))
# print(total_match(lst1, lst3))
# print(total_match(lst1, lst4))
# print(total_match(lst5, lst6))