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

    # 1. calculate the total number of chars in the all strings of the first list
    lst1_total_chars = sum(map(len, lst1))
    # 2. calculate the total number of chars in the all strings of the second list
    lst2_total_chars = sum(map(len, lst2))
    # 3. return the list that has total number of chars in the all strings of the list less than the other list
    if lst1_total_chars < lst2_total_chars:
        return lst1
    elif lst1_total_chars > lst2_total_chars:
        return lst2
    else:
        return lst1


print(total_match([], []))
print(total_match(['hi', 'admin'], ['hI', 'Hi']))
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))
print(total_match(['4'], ['1', '2', '3', '4', '5']))
