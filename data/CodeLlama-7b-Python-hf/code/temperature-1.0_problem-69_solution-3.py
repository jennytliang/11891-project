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
    if len(lst) == 1:
        if lst[0] > 0:
            return lst[0]
        else:
            return -1
    elif len(lst) == 2:
        if lst[0] > lst[1] and lst[0] > 0:
            return lst[0]
        elif lst[1] > 0:
            return lst[1]
        else:
            return -1
    elif len(lst) == 3:
        if lst[0] > lst[1] and lst[0] > lst[2] and lst[0] > 0:
            return lst[0]
        elif lst[1] > lst[2] and lst[1] > 0:
            return lst[1]
        elif lst[2] > 0:
            return lst[2]
        else:
            return -1
    elif len(lst) == 4:
        if lst[0] > lst[1] and lst[0] > lst[2] and lst[0] > lst[3] and lst[0] > 0:
            return lst[0]
        elif lst[1] > lst[2] and lst[1] > lst[3] and lst[1] > 0:
            return lst[1]
        elif lst[2] > lst[3] and lst[2] > 0:
            return lst[2]
        elif lst[3] > 0:
            return lst[3]
        else:
            return -1
    elif len(lst) == 5:
        if lst[0] > lst[1] and lst[0] > lst[2] and lst[0] > lst[3] and lst[0] > lst[4] and lst[0] > 0:
            return lst[0]
        elif lst[1] > lst[2] and lst[1] > lst[3] and lst[1] > lst[4] and lst[1] > 0:
            return lst[1]
        elif lst[2] > lst[3] and lst[2] > lst[4] and lst[2] > 0:
            return lst[2]
        elif lst[3] > lst[4] and lst[3] > 0:
            return lst[3]
        elif lst[4] > 0:
            return lst[4]
        else:
            return -1