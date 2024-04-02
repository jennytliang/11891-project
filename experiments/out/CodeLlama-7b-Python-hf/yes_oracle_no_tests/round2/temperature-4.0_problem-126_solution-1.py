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
    
	Do not include these tokens in the code: # check that all elements are integers
	'''
    # If length of lst is 1, then it is sorted
    if len(lst) == 1:
        return True
    # If length of lst is 2, then check if sorted
    if len(lst) == 2:
        if lst[0] <= lst[1]:
            return True
        else:
            return False
    # If length of lst is 3 or more, then check if sorted
    if len(lst) >= 3:
        for i in range(0, len(lst)):
            if lst[i] > lst[i+1]:
                return False
        return True

def test_is_sorted():
    assert is_sorted([5]) == True
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 3, 2, 4, 5]) == False
    assert is_sorted([1, 2, 3, 4, 5, 6]) == True
    assert is_sorted([1, 2, 3, 4, 5, 6, 7]) == True
    assert is_sorted([1, 3, 2, 4, 5, 6, 7]) == False
    assert is_sorted([1, 2, 2, 3, 3, 4]) == True
    assert is_sorted([1, 2, 2, 2, 3, 4]) == False

if __name__ == '__main__':
    test_is_sorted()