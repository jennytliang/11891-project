def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge ( x ): for ch in
	"""
    return list(map(int, sorted([''.join(i) for i in ([x] if not set.intersection(set(str(i)), set('02468')) else [])]))[0:-1])

if __name__ == '__main__':
    print("Example:")
    print(unique_digits([14, 356, 145, 35, 64,4, 198, 964]))
    print(unique_digits([152, 323, 1422, 10]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert unique_digits([14, 356, 145, 35, 64,4, 198, 964]) == [4, 14, 198, 356]
    assert unique_digits([152, 323, 1422, 10]) == []
    assert unique_digits([26, 152, 323, 1422, 10]) == [152, 323]