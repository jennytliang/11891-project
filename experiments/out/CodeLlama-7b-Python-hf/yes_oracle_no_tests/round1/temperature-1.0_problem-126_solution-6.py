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
    # check if list is empty
    if len(lst) == 0:
        return True
    
    # check if list has only one element
    if len(lst) == 1:
        return True
    
    # check if list has more than one element
    if len(lst) > 1:
        # check if list has more than one duplicate
        count = dict()
        for i in lst:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i in count:
            if count[i] > 1:
                return False
        # check if list is sorted
        for i in range(len(lst)-1):
            # check if next element is not greater than current element
            if lst[i] > lst[i+1]:
                return False
        # check if list has more than one duplicate
        return True
