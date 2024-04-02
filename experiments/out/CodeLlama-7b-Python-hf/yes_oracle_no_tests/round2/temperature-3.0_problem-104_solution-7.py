def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Do not include these tokens in the code: # == ================
	"""
    # == ================
    # Put your code below:
    result = []
    for i in x:
        if all(j % 2 != 0 for j in [int(x) for x in str(i)]):
            result.append(i)
    return sorted(result)


if __name__ == "__main__":
    try:
        with open("test.txt") as f:
            l = f.readlines()
            x = [int(i) for i in l[0].strip().split(',')]
            print(unique_digits(x))
    except IOError:
        print('Error: Could not open "test.txt"')
