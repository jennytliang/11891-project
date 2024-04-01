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
    
	Include these tokens in the code:  count = dict ()  for
	'''

    if len(lst) == 0:
        return True
    if len(lst) == 1:
        return True
    if len(lst) > 1:
        last_num = lst[0]
        num_count = 0
        for i in range(1, len(lst)):
            if lst[i] < last_num:
                return False
            if lst[i] == last_num:
                num_count += 1
            if num_count > 1:
                return False
            last_num = lst[i]
        return True


print(is_sorted([1, 2, 3, 4, 5, 6, 7]))
print(is_sorted([1, 2, 3, 4, 5, 6]))
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8]))
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print(is_sorted([1, 2, 3, 4, 5, 6