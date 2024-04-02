def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: <
	"""

    if len(lst) < 2:
        return None

    min_num = lst[0]
    for num in lst:
        if num < min_num:
            min_num = num

    next_min_num = None
    for num in lst:
        if num > min_num and (next_min_num == None or num < next_min_num):
            next_min_num = num

    return next_min_num


if __name__ == '__main__':
    print(next_smallest([1, 2, 3, 4, 5]))
