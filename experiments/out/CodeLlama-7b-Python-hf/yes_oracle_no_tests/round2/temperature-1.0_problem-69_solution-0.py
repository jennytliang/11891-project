def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    
	Do not include these tokens in the code: # Make a dictionary counting keys appearance
	'''
    count=dict((item,lst.count(item)) for item in lst)
    for value in lst:
        if value>0 and count[value]>=value:
            return value
    return -1
    pass

def search2(lst2):
    d=dict( (x,lst2.count(x)) for x in lst2 ) 
    for el in lst2:
        if ( el in d and d[el] >= el ):
            return el
    return -1

if __name__ == '__main__':
    print (search([4, 1, 2, 2, 3, 1]))
    print (search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1
    print(search([5, 5, 4, 4, 4])) ## Returns -1