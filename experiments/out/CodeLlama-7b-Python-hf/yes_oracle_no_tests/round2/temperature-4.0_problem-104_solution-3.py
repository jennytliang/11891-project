def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: x
	Do not include these tokens in the code: n
	"""

    def j(x):
        for i in range(len(x)):
            if x[i] % 2 == 0:
                x.pop(i)
        return x

    return j(x)


if __name__ == "__main__":
    print("Unique digits: ", unique_digits([15, 33, 1422, 1]))
    print("Unique digits: ", unique_digits([152, 323, 1422, 10]))
