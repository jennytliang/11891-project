def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return
	"""
    odd_even_sum = 0
    for i in range(0, len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 1:
            odd_even_sum += lst[i]
    return odd_even_sum


solution([5, 8, 7, 1])
solution([3, 3, 3, 3, 3])
solution([30, 13, 24, 321])
