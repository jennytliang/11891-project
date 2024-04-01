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

    # =============================================================================
    # if x==[]:
    #     return []
    # else:
    #     for i in x:
    #         if i==[]:
    #             return []
    #         else:
    #             for j in i:
    #                 if j==[]:
    #                     return []
    #                 else:
    #                     for k in j:
    #                         if k==[]:
    #                             return []
    #                         else:
    #                             return i
    # =============================================================================
    if x == []:
        return []
    else:
        return [i for i in x if not any(j in str(i) for j in '2468')]


if __name__ == '__main__':
    print("Example:")
    print(unique_digits([15, 33, 1422, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([152, 323, 1422, 10]) == []
    assert unique_digits([]) == []
    assert unique_digits([1]) == [1]
    assert unique_digits([1, 3, 5]) == [1, 3, 5]
    assert unique_digits([3, 33, 44, 55]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
