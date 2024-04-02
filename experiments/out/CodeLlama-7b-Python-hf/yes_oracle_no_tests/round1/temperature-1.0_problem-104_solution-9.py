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
    return [x for x in x if not any(c in str(x) for c in '02468')]


if __name__ == '__main__':

    solution = unique_digits
    to_test = [
        [15, 33, 1422, 1],
        [152, 323, 1422, 10],
        [],
    ]
    for values in to_test:
        print(f'{solution.__name__} = {solution(values)}')
