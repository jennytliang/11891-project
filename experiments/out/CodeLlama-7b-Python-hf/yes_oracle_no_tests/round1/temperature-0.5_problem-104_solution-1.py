def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code:  def judge ( x ): 
	"""

    # Create a list with all the digits
    digits = [int(i) for i in str(x)]
    # Create a list with the digits that are even
    evens = [i for i in digits if i % 2 == 0]
    # Create a list with the digits that are odd
    odds = [i for i in digits if i % 2 != 0]
    # If the list of evens is empty, return the original list
    if len(evens) == 0:
        return x
    # If the list of odds is empty, return the list of evens
    elif len(odds) == 0:
        return evens
    # If the list of evens is not empty and the list of odds is not empty, return empty
    else:
        return []


print(unique_digits([15, 33, 1422, 1]))
print(unique_digits([152, 323, 1422, 10]))
