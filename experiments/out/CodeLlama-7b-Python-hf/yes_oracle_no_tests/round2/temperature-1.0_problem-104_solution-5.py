def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Do not include these tokens in the code: digits _ set = {}
	"""

    ### YOUR CODE HERE
    x.sort()
    new=[]
    for i in x:
        for j in range(9):
            if str(i) in str(i)[j]:
                break
        else:
            new += [i]
    return new
    ### END YOUR CODE


if __name__ == "__main__":
    x = [int(i) for i in input("x: ").split()]
    result = unique_digits(x)
    print("result = {result}")
