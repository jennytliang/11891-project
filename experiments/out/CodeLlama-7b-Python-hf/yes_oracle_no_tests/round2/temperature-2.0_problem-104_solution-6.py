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
	"""
    # 1.
    # unique_digits = []
    # for i in x:
    #     for j in str(i):
    #         if int(j) % 2 == 1:
    #             unique_digits.append(i)
    # return unique_digits

    # 2.
    # unique_digits = []
    # for i in x:
    #     flag = True
    #     for j in str(i):
    #         if int(j) % 2 == 0:
    #             flag = False
    #             break
    #     if flag:
    #         unique_digits.append(i)
    # return unique_digits

    # 3.
    # unique_digits = []
    # for i in x:
    #     flag = True
    #     for j in str(i):
    #         if int(j) % 2 == 0:
    #             flag = False
    #             break
    #     if flag:
    #         unique_digits.append(i)
    # return unique_digits

    # 4.
    # return [i for i in x if not any(int(j) % 2 == 0 for j in str(i))]

    # 5.
    # return list(filter(lambda i: all(int(j) % 2 == 1 for j in str(i)), x))

    # 6.
    return list(filter(lambda i: not any(int(j) % 2 == 0 for j in str(i)), x))
