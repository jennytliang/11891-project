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
	Do not include these tokens in the code: if len ( lst ) <=
	'''
    
    # convert to a set to remove duplicates
    set_lst = set(lst)

    # check that set length matches lst length
    if len(set_lst) == len(lst):
        # check that set length is 1 less than lst length
        if len(set_lst) == len(lst) - 1:
            # check that set is in ascending order
            if set_lst == set(range(min(set_lst), max(set_lst) + 1)):
                return True
            else:
                return False
        # check that set length is 1 more than lst length
        elif len(set_lst) == len(lst) + 1:
            # check that set is in descending order
            if set_lst == set(range(max(set_lst), min(set_lst) - 1, -1)):
                return True
            else:
                return False
        # check that set length is the same as lst length
        elif len(set_lst) == len(lst):
            # check that set is in ascending order
            if set_lst == set(range(min(set_lst), max(set_lst) + 1)):
                return True
            # check that set is in descending order
            elif set_lst == set(range(max(set_lst), min(set_lst) - 1, -1)):
                return True
            else:
                return False
    else:
        return False


print(is_sorted([1, 2, 2, 3, 3, 4]))


def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
   