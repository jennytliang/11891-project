def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge
	Do not include these tokens in the code: # create set of all
	"""
    
    ret = list()
    for i in x:
        if '2' in str(i) or '4' in str(i) or '6' in str(i) or '8' in str(i):
            continue
        else:
            ret.append(i)
    ret.sort()
    return ret
    


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert unique_digits([3, 555, 150, 2020, 1, 2]) == [1, 3, 555], "Integers"
    assert unique_digits([3, 5, 6, 23, 7, 2, 15]) == [7, 15], "Integers"
    assert unique_digits([3, 5, 77, 91, 22, 110, 13]) == [], "Integers"
    assert unique_digits([26]) == [], "Singles"
    assert unique_digits([45, 47, 154, 487]) == [45, 47, 154, 487], "More than one digit"
    assert unique_digits([78, 457, 1222, 12459]) == [457, 78, 12459], "Sorting"
