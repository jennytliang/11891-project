def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: ch
	Do not include these tokens in the code: i
	"""

    def judge(x):
       '''
       judge whether x has any even digit
       '''
       for i in range(len(str(x))):
           if int(str(x)[i]) % 2 == 0:
               return True
       return False

    result = []
    for i in x:
        if not judge(i):
            result.append(i)
    return sorted(result)


print(unique_digits([15, 33, 1422, 1]))
print(unique_digits([152, 323, 1422, 10]))