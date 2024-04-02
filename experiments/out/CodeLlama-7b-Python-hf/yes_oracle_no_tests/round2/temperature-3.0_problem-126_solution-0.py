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
    
	Do not include these tokens in the code: # create a dictionary to
	'''
    # create a dictionary to hold the numbers and their count
    # if number already exists in dictionary, add 1 to its count
    # if count > 1, return False
    
    num_count = {}
    for num in lst:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    if len(num_count) > 1:
        return False
    else:
        for num in num_count:
            if num_count[num] > 1:
                return False
            else:
                return True

def is_sorted(lst):
    # create a dictionary to hold the numbers and their count
    # if number already exists in dictionary, add 1 to its count
    # if count > 1, return False
    
    num_count = {}
    for num in lst:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    if len(num_count) > 1:
        return False
    else:
        for num in num_count:
            if num_count[num] > 1:
                return False
            else:
                return True


def is_sorted(lst):
    # create a dictionary to hold the numbers and their count
    # if number already exists in dictionary, add 1 to its count
    # if count > 1, return False
    
    num_count = {}
    for num in lst:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    if len(num_count) > 1:
        return False
    else:
        for num in num_count:
            if num_count[num] > 1:
                return False
            else:
                return True


def is_sorted(lst):
    # create a dictionary to hold the numbers and their count
    # if number already exists in dictionary, add 1 to its