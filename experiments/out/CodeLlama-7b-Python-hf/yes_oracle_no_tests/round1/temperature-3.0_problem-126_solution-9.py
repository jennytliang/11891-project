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
    
	Include these tokens in the code: count = dict ()
	'''
    # Initialize count dictionary
    count = {}

    # Loop over lst
    for i in lst:
        # If i is in count dictionary
        if i in count:
            # Increment count
            count[i] += 1
        # Else
        else:
            # Set count to 1
            count[i] = 1

    # Loop over count dictionary
    for i in count:
        # If count is greater than 1
        if count[i] > 1:
            # Return False
            return False

    # Loop over lst
    for i in range(len(lst)-1):
        # If current element is greater than next element
        if lst[i] > lst[i+1]:
            # Return False
            return False

    # Return True
    return True


# print(is_sorted([1, 2, 2, 3, 3, 4]))
# print(is_sorted([1, 2, 2, 2, 3, 4]))
# print(is_sorted([1, 2, 3, 4, 5]))
# print(is_sorted([1, 2, 3, 4, 5, 6]))
# print(is_sorted([1, 2, 3, 4, 5, 6, 7]))
# print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8]))
# print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9]))