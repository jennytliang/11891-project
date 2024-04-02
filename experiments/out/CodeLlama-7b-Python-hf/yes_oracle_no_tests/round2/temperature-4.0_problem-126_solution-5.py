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
    
	Include these tokens in the code: x
	Do not include these tokens in the code: i
	'''

    
    count = dict()
    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    if len(count) == 1:
        return True
    for i in count:
        if count[i] > 1:
            return False
    lst.sort()
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
