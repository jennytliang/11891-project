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
    
	Include these tokens in the code: count
	Do not include these tokens in the code: # your code here #
	'''
    max_lst = lst[:]
    max_lst.sort()
    max_lst.reverse()
    for i in max_lst:
        if i > 0:
            count = lst.count(i)
            if count >= i:
                return i
    return -1

def search2(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater 
    than 0, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    
	Include these tokens in the code: count
	Do not include these tokens in the code: # your code here #
	'''
    max_lst = lst[:]
    max_lst.sort()
    max_lst.reverse()
    for i in max_lst:
        if i > 0:
            count = lst.count(i)
            if count >= i:
                return i
    return -1

def search3(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater 
    than 0, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4,