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
	Do not include these tokens in the code: my _ dict
	'''
    # My 2 cents
    lst.sort()
    lst2 = []
    for val in lst:
        if val in lst2:
            lst2.append(val)
    return len(lst2) == len(lst)
    
def is_sorted2(lst):
    # If list of duplicates
    if len(lst) > len(set(lst)):
        return False

    # If odd number of numbers
    if len(lst) % 2 == 1:
        return True

    for idx in range(1, len(lst), 2):
        if lst[idx] < lst[idx-1]:
            return False
    return True


is_sorted([])  # => True
is_sorted([1])  # => True
is_sorted([1, 2, 3])  # => True
is_sorted([3, 2, 1])  # => False
is_sorted([1, 2, 3, 2])  # => False
