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
    
    # Create a dictionary to count the number of occurrences of each number
    count = {}
    for i in range(len(lst)):
        if lst[i] in count:
            count[lst[i]] += 1
        else:
            count[lst[i]] = 1

    # If any number has more than 1 occurrence, return False
    for i in count:
        if count[i] > 1:
            return False

    # If all numbers have only one occurrence, check if they are in order
    lst_sorted = sorted(lst)
    for i in range(len(lst)):
        if lst[i] != lst_sorted[i]:
            return False

    return True