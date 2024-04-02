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
    
	Do not include these tokens in the code: # check for length of
	'''
    if len(lst) == 1:
        return True
    elif len(lst) == 2:
        if lst[1] > lst[0]:
            return True
        else:
            return False
    else:
        for i in range(len(lst)-1):
            if lst[i+1] < lst[i]:
                return False
        return True


# def is_sorted(lst):
#     '''
#     Given a list of numbers, return whether or not they are sorted
#     in ascending order. If list has more than 1 duplicate of the same
#     number, return False. Assume no negative numbers and only integers.

#     Examples
#     is_sorted([5]) ➞ True
#     is_sorted([1, 2, 3, 4, 5]) ➞ True
#     is_sorted([1, 3, 2, 4, 5]) ➞ False
#     is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
#     is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
#     is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
#     is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
#     is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    
#     Do not include these tokens in the code: # check for length of
#     '''
#     if len(lst) == 1:
#         return True
#     elif len(lst) == 2:
#         if lst[1] > lst[0]:
#             return True
#         else:
#             return False
#     else:
#         for i in range(len(lst)-1):
#             if lst[i+1] < lst[i]:
#                 return False
#         return