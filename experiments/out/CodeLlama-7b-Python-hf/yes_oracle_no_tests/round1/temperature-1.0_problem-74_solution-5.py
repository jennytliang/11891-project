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
    c1 = sum([len(i) for i in lst1]) #calculate the total number of characters in the list1
    c2 = sum([len(i) for i in lst2]) #calculate the total number of characters in the list2
    
    if c1==c2: #check to see if the total number of characters in the list1 and the list2 are the same
        return lst1 #return the first list
    
    return ([lst1, lst2][c1>c2]) # otherwise return the list that has the fewest characters

    
    
lst = ['a','s','d','f','g']
def total_match(lst1,lst2):
	if sum([len(x) for x in lst1])>sum([len(y) for y in lst2]):
		return lst1

	else:
		return lst2
    


total_match([], []) == []
    
print(total_match([], ['h', 'hello'])) == []
print(total_match([], ['h'])) == 'h'
print(total_match(['hi', 'admin'], ['hI', 'Hi'])) == ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])) == ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])) == ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5'])) == '4'