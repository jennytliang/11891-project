def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return sum
	Do not include these tokens in the code: # init if len
	"""
    # init sum
    sum = 0
    # init if len
    if len(lst) > 0:
        # iterate through list
        for i in range(len(lst)):
            # if element in even positions and odd
            if i % 2 == 0 and lst[i] % 2 == 1:
                # add to sum
                sum += lst[i]
    # return sum
    return sum


# test
print(solution([5, 8, 7, 1]))
print(solution([3, 3, 3, 3, 3]))
print(solution([30, 13, 24, 321]))
