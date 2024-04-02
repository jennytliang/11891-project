def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    lst = map(lambda x: int(x), lst)
    return sum(list(filter(lambda x: x % 2 == 1, lst))[::2])
    pass


def solution_2(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    lst = map(lambda x: int(x), lst)
    return sum([x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1])
    pass


# solution([5, 8, 7, 1])
# solution([3, 3, 3, 3, 3])
# solution([30, 13, 24, 321])

# solution_2([5, 8, 7, 1])
# solution_2([3, 3, 3, 3, 3])
# solution_2([30, 13, 24, 321])
