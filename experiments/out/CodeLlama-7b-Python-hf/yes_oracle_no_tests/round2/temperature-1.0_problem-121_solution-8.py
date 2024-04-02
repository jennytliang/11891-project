def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Do not include these tokens in the code: ([ i for i in lst if i % 2
	"""

    returnee = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            returnee += lst[i]
    return returnee


print(solution([5, 8, 7, 1]))
print(solution([3, 3, 3, 3, 3]))
print(solution([30, 13, 24, 321]))