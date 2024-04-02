def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	Do not include these tokens in the code: # init
	"""
    # init
    sum = 0
    
    # Core Code
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            sum += lst[i]
    
    # return
    return sum


# print(solution([5, 8, 7, 1]))
# print(solution([3, 3, 3, 3, 3]))
# print(solution([30, 13, 24, 321]))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def solution2(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	Do not include these tokens in the code: # init
	"""
    # init
    sum = 0
    
    # Core Code
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            sum += lst[i]
    
    # return
    return sum


# print(solution2([5, 8, 7, 1]))
# print(solution2([3, 3, 3, 3, 3]))
# print(solution2([30, 13, 24, 321]))
# print(solution2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def solution3(lst):
    """Given a non-empty list of integers, return the