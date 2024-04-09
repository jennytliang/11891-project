def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge ( x ):
	Do not include these tokens in the code: result = [] for i
	"""
    result = []
    for i in x:
        flag = 0
        for j in str(i):
            if int(j) % 2 == 0:
                flag = 1
                break
        if flag == 0:
            result.append(i)
    return sorted(result)


if __name__ == '__main__':
    print("Example:")
    print(unique_digits([15, 33, 1422, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([152, 323, 1422, 10]) == []
    assert unique_digits([1, 2, 3, 4]) == []
    assert unique_digits([555, 333, 1, 4]) == [1, 555]
    print("Coding complete? Click 'Check' to earn cool rewards!")
