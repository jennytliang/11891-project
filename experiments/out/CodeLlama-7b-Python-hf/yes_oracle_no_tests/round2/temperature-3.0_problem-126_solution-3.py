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
    
	Include these tokens in the code: dict ()
	Do not include these tokens in the code: {}
	'''

    
 
    # if len(lst) == 1:
    #     return True
    
    # for i in range(1,len(lst)):
    #     if lst[i] < lst[i-1]:
    #         return False
    
    # return True
    
    return sorted(lst) == lst
    
print(is_sorted([5]))
#➞ True
print(is_sorted([1, 2, 3, 4, 5]))
#➞ True
print(is_sorted([1, 3, 2, 4, 5]))
#➞ False
print(is_sorted([1, 2, 3, 4, 5, 6]))
#➞ True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))
#➞ True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))
#➞ False
print(is_sorted([1, 2, 2, 3, 3, 4]))
#➞ True
print(is_sorted([1, 2, 2, 2, 3, 4]))
#➞ False


# def is_sorted(lst):
#     """Return True if the list is sorted, False otherwise."""
#     if len(lst) == 1:
#         return True
#     for i in range(1, len(lst)):
#         if lst[i] < lst[i - 1]:
#             return False
#     return True


# def is_sorted(lst):
#     return sorted(lst) == lst
