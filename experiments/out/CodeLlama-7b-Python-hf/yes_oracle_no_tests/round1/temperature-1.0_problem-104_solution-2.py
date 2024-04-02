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
	Do not include these tokens in the code: result = [] for num
	"""

    nums = []
    result = []

    def judge(num):
        if num < 10: return result.append(num)
        if num % 2 != 0: return result.append(num)

    for each in x:
        if each < 10:
            result.append(each)
        else:
            judge(each)

    return list(dict.fromkeys(result)) if len(result) > 0 else result


test = [15, 33, 1422, 1]
expected = [1, 15, 33]
result = unique_digits(test)
assert expected == result

test = [152, 323, 1422, 10]
result = unique_digits(test)
assert len(result) == 0

print("Tests Passed")
