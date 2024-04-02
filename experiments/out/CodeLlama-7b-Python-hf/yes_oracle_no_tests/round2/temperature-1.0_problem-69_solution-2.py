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
    
	Do not include these tokens in the code: result = - 1
	'''
    lst.sort()
    lst_1 = []
    for i in lst:
        lst_1.append(lst.count(i))
    lst_2 = []
    for i in range(len(lst_1)):
        lst_2.append(lst[i]*lst_1[i])
    for i in range(len(lst_2)):
        if lst_2[i] <= lst[i]:
            lst_2[i] = -1
    for i in lst_1:
        if (i == 1) & (lst[i] > 1):
            return lst[i]
    return max(lst_2)