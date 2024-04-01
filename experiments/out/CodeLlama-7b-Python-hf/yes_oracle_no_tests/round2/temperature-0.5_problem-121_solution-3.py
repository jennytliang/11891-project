def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return 0
    elif len(lst) == 2:
        return 0
    elif len(lst) == 3:
        return 0
    else:
        return sum(lst[i] for i in range(0, len(lst)) if i % 2 == 0 and lst[i] % 2 == 1)


# lst = [5, 8, 7, 1]
lst = [30, 13, 24, 321]
print(solution(lst))
