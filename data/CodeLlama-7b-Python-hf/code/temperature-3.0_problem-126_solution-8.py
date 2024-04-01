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
    '''

    # Check that there is only one duplicate in the list
    if len(lst) != len(set(lst)):
        print('This list has duplicates.')
        return False

    # If len(lst) is 1, it is sorted
    if len(lst) == 1:
        return True

    # Set the first index to 0
    index = 0
    while index < len(lst) - 1:
        # Check if value at index is greater than value at next index
        if lst[index] > lst[index + 1]:
            return False
        # Increment index
        index += 1
    # If we make it through the loop, return True
    return True
    

lst = [1, 2, 2, 3, 4]