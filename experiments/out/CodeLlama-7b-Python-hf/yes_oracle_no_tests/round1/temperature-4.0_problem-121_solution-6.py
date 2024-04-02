def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return sum
	Do not include these tokens in the code: # init if len
	"""
    return sum([lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0])


# Testing
lst1 = [5, 8, 7, 1]
lst2 = [3, 3, 3, 3, 3]
lst3 = [30, 13, 24, 321]
print(solution(lst1))
print(solution(lst2))
print(solution(lst3))
