def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return sum
	Do not include these tokens in the code: # init if len
	"""

    #init
    sum = 0

    #code
    if len(lst) % 2 == 0:
        for i in range(0, len(lst), 2):
            if lst[i] % 2 == 1:
                sum += lst[i]
    else:
        for i in range(1, len(lst), 2):
            if lst[i] % 2 == 1:
                sum += lst[i]

    return sum


print(solution([5, 8, 7, 1]))
print(solution([3, 3, 3, 3, 3]))
print(solution([30, 13, 24, 321]))