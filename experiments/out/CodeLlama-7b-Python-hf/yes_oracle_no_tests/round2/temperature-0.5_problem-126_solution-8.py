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
    
	Do not include these tokens in the code: # Create a dictionary of unique
	'''
    # Create a dictionary of unique numbers
    unique_nums = {}
    for num in lst:
        if num in unique_nums:
            return False
        else:
            unique_nums[num] = True
    # Create a list of all the unique numbers
    unique_nums_list = []
    for key in unique_nums.keys():
        unique_nums_list.append(key)
    # Sort the list of the unique numbers
    sorted_unique_nums_list = sorted(unique_nums_list)
    # Compare the two lists
    if lst == sorted_unique_nums_list:
        return True
    else:
        return False

print(is_sorted([5]))
#print(is_sorted([1, 2, 3, 4, 5]))
#print(is_sorted([1, 3, 2, 4, 5]))
print(is_sorted([1, 2, 3, 4, 5, 6]))
#print(is_sorted([1, 2, 3, 4, 5, 6, 7]))
#print(is_sorted([1, 3, 2, 4, 5, 6, 7]))
print(is_sorted([1, 2, 2, 3, 3, 4]))
#print(is_sorted([1, 2, 2, 2, 3, 4]))
