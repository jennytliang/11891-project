def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""

    return sum([lst[i] for i in range(len(lst)) if i % 2  == 0 and lst[i] % 2 != 0])


    return sum(lst[i] for i in range(1, len(lst), 2) if lst[i] %2 != 0)

print(solution([5, 8, 7, 1]))
#{ 12, 8, 7, 5, 1 }
#{ 1, 3, 5, 7, 9 }
print(solution([30, 13, 24, 321]))
#{ 30, 3, 3, 3 }
#{ 12, 18, 0, 0, 1 }