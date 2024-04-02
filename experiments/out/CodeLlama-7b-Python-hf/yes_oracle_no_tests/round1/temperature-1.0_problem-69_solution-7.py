def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    
	Include these tokens in the code: count = dict ()
	'''

    count = {}
    for item in lst:
        count[item] = count.get(item, 0) + 1
    
    max_freq = max(count.values())

    for item, freq in list(dict(count).items()):
        if freq >= item and freq > max_freq:
            max_freq = freq

    if max_freq > count[max_freq]:
        max_freq = count[max_freq]
    else:
        max_freq = -1

    return max_freq

def test_1():
    lst = [4, 1, 2, 2, 3, 1]
    assert search(lst) == 2

def test_2():
    lst = [1, 2, 2, 3, 3, 3, 4, 4, 4]
    assert search(lst) == 3

def test_3():
    lst = [5, 5, 4, 4, 4]
    assert search(lst) == -1

def test_4():
    lst = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    assert search(lst) == 4