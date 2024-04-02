def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Do not include these tokens in the code: lst = map ( lambda x :
	"""
    sum_of_odd_elements = 0
    for i in range(len(lst)):
        if i%2==0 and lst[i]%2!=0:
            sum_of_odd_elements+=lst[i]
    return sum_of_odd_elements



print(solution([5, 8, 7, 1]))
print(solution([3, 3, 3, 3, 3]))
print(solution([30, 13, 24, 321]))
print(solution([5, 8, 7, 1, 2, 3, 4, 5]))