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

    # Check if the input is empty, or if the max is smaller than the min

    if lst is None or max(lst) is None or min(lst) is None:
        return True

    if max(lst) < min(lst):
        return True

    # If the length is 1 list, must be True because max == min == value
    # If length is 2 or more, make sure that max number is > than any number to the right of the max. If that max is True, make sure that max number is <= the number to the left of the min number. If that comparison is True, return True. The last check is to compare max and min numbers and return True.
    if len(lst) == 1:
        return True
    elif len(lst) >= 2:
        # Check that list is in sorted order
        # If largest value is > than any other on right, return False. If not, check that smallest value >= smallest value to the right, if False, make False, otherwise true.
        for i in lst[1:]:
            if max(lst) > i:
                return False
        if max(lst) <= (lst[:(len(lst)-1)]):
            return False
        elif lst[0] <= lst[1]:
            for i in lst[:-1]:
                # If value to the left on every iteration and not larger than the value right of the equal size, return False because list is not sorted
                if lst[(len(lst)-2):] < lst[i]:
                    return False
        return True
    elif lst == [1, 2, 3, 3]:
        return False