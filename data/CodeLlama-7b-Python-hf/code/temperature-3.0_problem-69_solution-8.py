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
    new_dict = {}
    for num in lst:
        if(num not in new_dict.keys()):
            new_dict[num] = 1
        else:
            new_dict[num] = new_dict[num] + 1
    for num in new_dict.keys():
        if(new_dict[num] >= num):
            return num 