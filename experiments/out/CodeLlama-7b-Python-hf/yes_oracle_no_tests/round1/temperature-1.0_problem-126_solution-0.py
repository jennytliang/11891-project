def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    
	Include these tokens in the code: count = dict ()
	'''
    if not lst or len(lst) == 1 or not lst[0]:
        return True
    # create an initial dict that contains {element: 1}
    count = dict()
    
    for i in lst: 
        elem = int(lst[i])
        if count.get(lst[i]):
            return False
        else:
            count[elem] = 1
            
    
    # make sure only numbers between 0-9 occur in the list
    if 10 in count:
        return False
    
    # check if sorted from 0-9
    
    if not count.get(0):
        current = 1
        while count.get(current):
            if count.get(current) > 1:
                return False
            else:
                current += 1

    else:
        current = 0
        while count.get(current):
            if count.get(current) > 1:
                return False
            else:
                current += 1
    
    
    return True
