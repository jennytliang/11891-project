def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: judge
	Do not include these tokens in the code: has _ even _ digit
	"""


  # Write your code here
    for i in x:
        if '0' in str(i) or '2' in str(i) or '4' in str(i) or '6' in str(i) or '8' in str(i):
            x.remove(i)
    return sorted(x)


print(unique_digits([15, 33, 1422, 1]))
print(unique_digits([152, 323, 1422, 10]))
