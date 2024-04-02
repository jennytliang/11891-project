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
    # count unique numbers
    unique_nums = set(lst)
    # count number of unique numbers
    unique_count = len(unique_nums)
    # return if count of unique numbers is 1
    if unique_count == 1:
        return True
    # return if count of unique numbers is 2 and the first number is less than the second
    if unique_count == 2:
        if lst[0] < lst[1]:
            return True
    # return if count of unique numbers is 2 and the first number is greater than the second
    if unique_count == 2:
        if lst[0] > lst[1]:
            return True
    # return if count of unique numbers is 2 and the first number is greater than the second
    if unique_count == 2:
        if lst[0] == lst[1]:
            return False
    # return if count of unique numbers is 3 and the first number is less than the second and the third
    if unique_count == 3:
        if lst[0] < lst[1] < lst[2]:
            return True
    # return if count of unique numbers is 3 and the first number is greater than the second and the third
    if unique_count == 3:
        if lst[0] > lst[1] > lst[2]:
            return True
    # return if count of unique numbers is 3 and the first number is greater than the second and the third
    if unique_count == 3:
        if lst[0] > lst[1] < lst[2]:
            return False
    # return if count of unique numbers is 3 and the first number is greater than the second and the third
    if unique_count == 3:
        if lst[0] < lst[1] > lst[2]:
            return False
    # return if count of unique numbers is 3 and the first number is less than the second and the third
    if unique_count == 3:
        if lst[0] < lst[1] < lst[2]:
            return False
    # return if count of unique numbers is 3 and the first number is less than the second