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
    
    # Set the number of items in the list
    lst_len = len(lst)
    
    # Set the number of duplicates in the list
    lst_count = lst.count(lst[0])
    
    # If the number of duplicates is more than 1, return False
    if lst_count > 1:
        return False
    
    # If the number of duplicates is 1, return True
    elif lst_count == 1:
        return True
    
    # If the number of duplicates is 0, return False
    elif lst_count == 0:
        return False
    
    # Set the number of occurrences of the first item in the list
    lst_first_item = lst.count(lst[0])
    
    # Set the number of occurrences of the last item in the list
    lst_last_item = lst.count(lst[-1])
    
    # If the number of occurrences of the first item is less than the
    # number of occurrences of the last item, return False
    if lst_first_item < lst_last_item:
        return False
    
    # If the number of occurrences of the first item is greater than or
    # equal to the number of occurrences of the last item, return True
    elif lst_first_item >= lst_last_item:
        return True
    
    # Otherwise return False
    else:
        return False
    
def is_sorted_asc(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 