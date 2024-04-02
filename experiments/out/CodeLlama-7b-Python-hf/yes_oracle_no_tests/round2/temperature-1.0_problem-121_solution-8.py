def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return sum ( lst [ i ]
	Do not include these tokens in the code: total = 0
	"""
    odds = []
    for i in range(0, len(lst)):
        if i%2 == 0:
            sum = lst[i]
        else:
            odds.append(lst[i])
            
    result = 0

    for o in odds:
        if o % 2 != 0:
            result += o
    return result


solution([5,4,3,2,1])