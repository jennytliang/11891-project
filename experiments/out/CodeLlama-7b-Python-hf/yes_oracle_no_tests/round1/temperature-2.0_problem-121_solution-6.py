def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    return sum([n for i, n in enumerate(lst) if i % 2 == 0 and n % 2 == 1])


# TESTS
assert solution([5, 8, 7, 1]) == 12
assert solution([3, 3, 3, 3, 3]) == 9
assert solution([30, 13, 24, 321]) == 0
assert solution([1, 2]) == 0
assert solution([1, 2, 3, 4]) == 0
assert solution([1, 2, 3, 4, 5]) == 6
assert solution([1, 2, 3, 4, 5, 6]) == 12
