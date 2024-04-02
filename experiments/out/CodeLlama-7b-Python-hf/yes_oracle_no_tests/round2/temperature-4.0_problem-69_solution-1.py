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
    
	Do not include these tokens in the code: #
	'''
    if len(lst) == 0:
        return -1
    numDict = {}
    for num in lst:
        if num in numDict:
            numDict[num] += 1
        else:
            numDict[num] = 1
    lst = []
    for key in numDict:
        if numDict[key] >= key:
            lst.append(key)
    if len(lst) == 0:
        return -1
    else:
        return max(lst)


def search2(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater 
    than zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search2([4, 1, 2, 2, 3, 1]) == 2
        search2([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search2([5, 5, 4, 4, 4]) == -1
    '''
    if len(lst) == 0:
        return -1
    numDict = {}
    for num in lst:
        if num in numDict:
            numDict[num] += 1
        else:
            numDict[num] = 1
    lst = []
    for key in numDict:
        if numDict[key] >= key:
            lst.append(key)
    if len(lst) == 0:
        return -1
    else:
        return max(lst)


def search3(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater 
    than zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -