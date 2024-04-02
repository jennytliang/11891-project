def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    return sum([i for i in lst if i % 2 == 0 if lst.index(i) % 2 == 1])


# Testing
lst = [5, 8, 7, 1]
print(solution(lst))

lst = [3, 3, 3, 3, 3]
print(solution(lst))

lst = [30, 13, 24, 321]
print(solution(lst))