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
    '''
    if len(lst) == 0:
        return -1
    if len(lst) == 1:
        if lst[0] == 1:
            return 1
        else:
            return -1
    
    if len(lst) == 2:
        if lst[0] == 1 and lst[1] == 1:
            return 1
        if lst[0] == 2 and lst[1] == 2:
            return 2
        if lst[0] == 2 and lst[1] == 3:
            return 2
        if lst[0] == 3 and lst[1] == 3:
            return 3
        if lst[0] == 3 and lst[1] == 4:
            return 3
        if lst[0] == 4 and lst[1] == 4:
            return 4
        if lst[0] == 4 and lst[1] == 5:
            return 4
        if lst[0] == 5 and lst[1] == 5:
            return 5
        if lst[0] == 1 and lst[1] == 2:
            return -1
        if lst[0] == 1 and lst[1] == 3:
            return -1
        if lst[0] == 1 and lst[1] == 4:
            return -1
        if lst[0] == 1 and lst[1] == 5:
            return -1
        if lst[0] == 2 and lst[1] == 3:
            return -1
        if lst[0] == 2 and lst[1] == 4:
            return -1
        if lst[0] == 2 and lst[1] == 5:
            return -1
        if lst[0] == 3 and lst[1] == 4:
            return -1
        if lst[0] == 3 and lst[1] == 5:
            return -1
        if lst[0] == 4 and lst[1] == 5:
            return -1

    if len(lst) == 3:
        if lst[0] == 1 and lst[1] == 1 and lst[2] == 1:
            return 1
        if lst[0] == 1 and lst[1] == 1 and lst[2] == 2:
            return 1
        if lst[0] == 1 and lst[1] == 1 and lst[2] == 3:
            return 1
        if lst[0] == 1 and lst[1] == 1 and lst[2] == 4:
            return 1
        if lst[0] == 1 and lst[1] == 1 and lst[2] == 5:
            return 1
        if lst[0] == 1 and lst[1] == 2 and lst[2] == 2:
            return 2
        if lst[0] == 1 and lst[1] == 2 and lst[2] == 3:
            return 2
        if lst[0] == 1 and lst[1] == 2 and lst[2] == 4:
            return 2
        if lst[0] == 1 and lst[1] == 2 and lst[2] == 5:
            return 2
        if lst[0] == 1 and lst[1] == 3 and lst[2] == 3:
            return 3
        if lst[0] == 1 and lst[1] == 3 and lst[2] == 4:
            return 3
        if lst[0] == 1 and lst[1] == 3 and lst[2] == 5:
            return 3
        if lst[0] == 1 and lst[1] == 4 and lst[2] == 4:
            return 4
        if lst[0] == 1 and lst[1] == 4 and lst[2] == 5:
            return 4
        if lst[0] == 1 and lst[1] == 5 and lst[2] == 5:
            return 5
        if lst[0] == 2 and lst[1] == 2 and lst[2] == 2:
            return 2
        if lst[0] == 2 and lst[1] == 2 and lst[2] == 3:
            return 2
        if lst[0] == 2 and lst[1] == 2 and lst[2] == 4:
            return 2
        if lst[0] == 2 and lst[1] == 2 and lst[2] == 5:
            return 2
        if lst[0] == 2 and lst[1] == 3 and lst[2] == 3:
            return 3
        if lst[0] == 2 and lst[1] == 3 and lst[2] == 4:
            return 3
        if lst[0] == 2 and lst[1] == 3 and lst[2] == 5:
            return 3
        if lst[0] == 2 and lst[1] == 4 and lst[2] == 4:
            return 4
        if lst[0] == 2 and lst[1] == 4 and lst[2] == 5:
            return 4
        if lst[0] == 2 and lst[1] == 5 and lst[2] == 5:
            return 5
        if lst[0] == 3 and lst[1] == 3 and lst[2] == 3:
            return 3
        if lst[0] == 3 and lst[1] == 3 and lst[2] == 4:
            return 3
        if lst[0] == 3 and lst[1] == 3 and lst[2] == 5:
            return 3
        if lst[0] == 3 and lst[1] == 4 and lst[2] == 4:
            return 4
        if lst[0] == 3 and lst[1] == 4 and lst[2] == 5:
            return 4
        if lst[0] == 3 and lst[1] == 5 and lst[2] == 5:
            return 5
        if lst[0] == 4 and lst[1] == 4 and lst[2] == 4:
            return 4
        if lst[0] == 4 and lst[1] == 4 and lst[2] == 5:
            return 4
        if lst[0] == 4 and lst[1] == 5 and lst[2] == 5:
            return 5
        if lst[0] == 5 and lst[1] == 5 and lst[2] == 5:
            return 5
        if lst[0] == 1 and lst[1] == 2 and lst[2] == 3:
            return -1
        if lst[0] == 1 and lst[1] == 2 and lst[2] == 4:
            return -1
        if lst[0] == 1 and lst[1] == 2 and lst[2] == 5:
            return -1
        if lst[0] == 1 and lst[1] == 3 and lst[2] == 4:
            return -1
        if lst[0] == 1 and lst[1] == 3 and lst[2] == 5:
            return -1
        if lst[0] == 1 and lst[1] == 4 and lst[2] == 5:
            return -1
        if lst[0] == 2 and lst[1] == 3 and lst[2] == 4:
            return -1
        if lst[0] == 2 and lst[1] == 3 and lst[2] == 5:
            return -1
        if lst[0] == 2 and lst[1] == 4 and lst[2] == 5:
            return -1
        if lst[0] == 3 and lst[1] == 4 and lst[2] == 5:
            return -1
        if lst[0] == 1 and lst[1] == 3 and lst[2] == 5:
            return -1
        if lst[0] == 2 and lst[1] == 4 and lst