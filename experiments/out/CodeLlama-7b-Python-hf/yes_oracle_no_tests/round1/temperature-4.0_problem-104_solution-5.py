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
	Do not include these tokens in the code: # The idea is to keep
	"""
    # The idea is to keep a set of all unique digits, and then check if the
    # number has any even digit, if so, remove it from the set.
    # The set will be the final answer
    all_digits = set(str(x) for x in range(10))

    # Loop through all integers
    for num in x:
        num_str = str(num)
        # Loop through all digits in the number
        for digit in num_str:
            # If the digit is even, remove it from the set
            if int(digit) % 2 == 0:
                all_digits.remove(digit)

    return sorted(list(all_digits))


def test_unique_digits():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([152, 323, 1422, 10]) == []
    assert unique_digits([10, 100, 1000]) == [1, 10]
    assert unique_digits([10, 100, 1000, 10000]) == [1, 10]
    assert unique_digits([100, 1000, 10000, 100000]) == [100, 1000]
    assert unique_digits([100, 1000, 10000, 100000, 1000000]) == [100, 1000]
    assert unique_digits([100, 1000, 10000, 100000, 1000000, 10000000]) == [100]
    assert unique_digits([100, 1000, 10000, 100000, 10