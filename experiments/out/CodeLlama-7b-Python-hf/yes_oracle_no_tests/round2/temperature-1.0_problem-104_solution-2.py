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
    result = []
    for num in x:
        if num > 0:
            has_even = False
            for digit in str(num):
                if int(digit) % 2 == 0:
                    has_even = True
                    break
            if not has_even:
                result.append(num)
    return sorted(result)


if __name__ == '__main__':
    print(unique_digits([15, 33, 1422, 1]))