def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: i
	Do not include these tokens in the code: idx
	"""

    return sum(ele for j in range(0, len(lst), 2) for ele in lst[j] if ele % 2 != 0)

# [5,8,7,1] = 12
# [3,3,3,3,3] = 9
# [30,13,24,321] = 0

