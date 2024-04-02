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
    # write your code here
    result = []
    for i in x:
        flag = True
        for j in str(i):
            if int(j) % 2 == 0:
                flag = False
                break
        if flag:
            result.append(i)
    return sorted(result)


if __name__ == "__main__":
    print("Example:")
    print(unique_digits([15, 33, 1422, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([152, 323, 1422, 10]) == []
    assert unique_digits([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert unique_digits([33, 44, 55, 66]) == []
    assert unique_digits([10, 20, 30, 40]) == [10, 20, 30, 40]
    print("Coding complete? Click 'Check' to earn cool rewards!")
