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
	c1 = sum(map(lambda x:len(x), lst1))
	c2 = sum(map(lambda x:len(x), lst2))
	if c1 == c2:
	    return lst1
	elif c1 > c2:
	    return lst2
	else:
	    return lst1
            
        
def total_match2(lst1, lst2):
    total1=sum([len(x) for x in lst1])
    total2=sum([len(x) for x in lst2])
    
    if total2>total1:
        return lst2
    else:
        return lst1
    
def total_match3(lst1, lst2):
    c1=0
    for x in lst1:
        c1+=len(x)
    
    c2=0
    for x in lst2:
        c2+=len(x)
    
    if c1==c2:
       return lst1
    elif c1>c2:
       return lst2
    else:
       return lst1