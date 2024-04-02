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
    
	Include these tokens in the code: count
	Do not include these tokens in the code: sorted
	'''
    # Your code here
    if len(lst) == 1:
        return True

    if len(lst) == 2:
        if lst[0] == lst[1]:
            return False
        elif lst[0] < lst[1]:
            return True
        else:
            return False

    if lst[0] == lst[1]:
        return False

    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False
    return True
